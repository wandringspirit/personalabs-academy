import os
import sys
import asyncio
import subprocess
import cv2
import numpy as np
import imageio_ffmpeg
import edge_tts
from PIL import Image, ImageDraw, ImageFont

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
AD_HOOKS_DIR = os.path.join(PROJECT_DIR, "ads-ready", "dancing-ad-hooks")
RAW_HOOKS_DIR = os.path.join(PROJECT_DIR, "instagram-studio", "05-Dancing-Hook-Options")
NEW_PERSONAS_DIR = os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "new-personas")
BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

os.makedirs(AD_HOOKS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

RW, RH = 1080, 1920

def get_font(name, size):
    font_dir = r"C:\Windows\Fonts"
    candidates = [name, "segoeuib.ttf", "arialbd.ttf", "SegoeUI.ttf", "arial.ttf"]
    for c in candidates:
        p = os.path.join(font_dir, c)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_HEAD = get_font("arialbd.ttf", 46)
FONT_SUB = get_font("segoeuib.ttf", 30)
FONT_TAG = get_font("segoeuib.ttf", 22)
FONT_BTN = get_font("arialbd.ttf", 36)

def crop_fill(img, target_w, target_h, align_y=0.3):
    iw, ih = img.size
    target_ratio = target_w / target_h
    src_ratio = iw / ih
    if src_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        left = (iw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        top = int((ih - new_h) * align_y)
        top = max(0, min(ih - new_h, top))
        img = img.crop((0, top, iw, top + new_h))
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

def decorate_ad_frame(frame_bgr, top_hook, sub_hook, bottom_text, accent=(236, 72, 153)):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(0, 280):
        prog = (280 - y) / 280.0
        alpha = int(min(225, prog * 235))
        gd.line([(0, y), (RW, y)], fill=(8, 10, 20, alpha))
    for y in range(RH - 460, RH):
        prog = (y - (RH - 460)) / 460.0
        alpha = int(min(240, prog * 250))
        gd.line([(0, y), (RW, y)], fill=(8, 10, 20, alpha))
    pil.alpha_composite(grad)

    d = ImageDraw.Draw(pil, "RGBA")
    # Top profile tag
    d.rounded_rectangle((48, 54, 430, 106), radius=26, fill=(12, 14, 24, 230), outline=(accent[0], accent[1], accent[2], 200), width=2)
    d.ellipse((68, 71, 86, 89), fill=accent)
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    # Top hook banner
    d.rounded_rectangle((48, 126, RW - 48, 222), radius=24, fill=(10, 14, 26, 235), outline=(accent[0], accent[1], accent[2], 220), width=2)
    d.text((RW // 2, 174), top_hook, font=FONT_HEAD, fill=(255, 255, 255), anchor="mm")

    # Pattern interrupt sub-hook pill
    if sub_hook:
        d.rounded_rectangle((RW // 2 - 380, 244, RW // 2 + 380, 314), radius=20, fill=(accent[0], accent[1], accent[2], 245))
        d.text((RW // 2, 279), sub_hook, font=FONT_SUB, fill=(10, 14, 26), anchor="mm")

    # Bottom Call to Action box
    if bottom_text:
        lines = bottom_text.split("\n")
        line_h = 44
        total_h = len(lines) * line_h + 36
        d.rounded_rectangle((48, RH - 280, RW - 48, RH - 280 + total_h), radius=24, fill=(12, 16, 28, 235), outline=(56, 189, 248, 200), width=2)
        ty = RH - 280 + 20 + line_h // 2
        for ln in lines:
            d.text((RW // 2, ty), ln, font=FONT_SUB, fill=(255, 255, 255), anchor="mm")
            ty += line_h

    return cv2.cvtColor(np.array(pil.convert("RGB")), cv2.COLOR_RGB2BGR)

def get_audio_dur(path):
    res = subprocess.run([FFMPEG_EXE, "-i", path], capture_output=True, text=True)
    import re
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return 4.0

async def synth_voice(tts_text, out_mp3):
    comm = edge_tts.Communicate(tts_text, "en-US-AvaMultilingualNeural", rate="+10%", pitch="+0Hz")
    await comm.save(out_mp3)
    return get_audio_dur(out_mp3)

def render_ad_video(out_name, top_hook, sub_hook, voice_text, video_source, still_image_path, bottom_p1, bottom_p2, accent=(236, 72, 153)):
    out_path = os.path.join(AD_HOOKS_DIR, out_name)
    prefix = os.path.join(SCRATCH_DIR, f"tts_{out_name}")
    voice_mp3 = f"{prefix}_voice.mp3"
    
    dur = asyncio.run(synth_voice(voice_text, voice_mp3))
    total_dur = max(10.0, dur + 1.0)
    
    # Synth upbeat rhythmic background audio
    sr = 44100
    t = np.linspace(0, total_dur, int(sr * total_dur), endpoint=False)
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.2 * t) ** 4
    synth_pad = (0.30 * np.sin(2 * np.pi * 146.83 * t) + 0.20 * np.sin(2 * np.pi * 220.00 * t)) * (0.05 * beat_env)
    stereo_bgm = np.column_stack([synth_pad, synth_pad]).astype(np.float32)
    bgm_wav = f"{prefix}_bgm.wav"
    import wave
    with wave.open(bgm_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((stereo_bgm * 32767).astype(np.int16).tobytes())
        
    mixed_audio = f"{prefix}_mixed.m4a"
    subprocess.run([
        FFMPEG_EXE, "-y", "-i", voice_mp3, "-i", bgm_wav,
        "-filter_complex", "[0:a]volume=1.35[v];[1:a]volume=0.85[b];[v][b]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", mixed_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    fps = 30
    total_frames = int(round(total_dur * fps))
    dance_phase_frames = int(round(4.0 * fps)) # 4 seconds of dance motion
    
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", mixed_audio,
        "-c:v", "libx264", "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", "-shortest", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 1. Dance video capture
    cap = cv2.VideoCapture(video_source)
    cap_frames = []
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        # Resize to 1080x1920 if needed
        if frame.shape[0] != RH or frame.shape[1] != RW:
            frame = cv2.resize(frame, (RW, RH))
        cap_frames.append(frame)
    cap.release()
    
    # 2. Still image model capture
    still_pil = Image.open(still_image_path).convert("RGB")
    still_pil = crop_fill(still_pil, RW, RH, align_y=0.25)
    still_bgr = cv2.cvtColor(np.array(still_pil), cv2.COLOR_RGB2BGR)

    for f_idx in range(total_frames):
        if f_idx < dance_phase_frames and cap_frames:
            base_frame = cap_frames[f_idx % len(cap_frames)].copy()
            active_bottom = bottom_p1
        else:
            # Subtle gentle zoom on still model for cinematic liveliness
            prog = (f_idx - dance_phase_frames) / max(1, total_frames - dance_phase_frames)
            scale = 1.0 + 0.04 * np.sin(prog * np.pi)
            zw, zh = int(RW * scale), int(RH * scale)
            zoomed = cv2.resize(still_bgr, (zw, zh))
            x_off = (zw - RW) // 2
            y_off = (zh - RH) // 2
            base_frame = zoomed[y_off:y_off+RH, x_off:x_off+RW]
            active_bottom = bottom_p2
            
        ad_frame = decorate_ad_frame(base_frame, top_hook, sub_hook, active_bottom, accent=accent)
        proc.stdin.write(ad_frame.tobytes())
        
    proc.stdin.close()
    proc.wait()
    
    for f in [voice_mp3, bgm_wav, mixed_audio]:
        if os.path.exists(f):
            os.remove(f)
    print(f"[OK] Generated: {out_name} ({os.path.getsize(out_path):,} bytes)")

def main():
    print("=== RENDERING HIGH-CONVERTING DANCING AD HOOKS ===")
    
    # Ad 1: Indian Model - Saree Dance Sway to Wine Saree Reveal
    render_ad_video(
        out_name="Ad_Hook_01_Indian_Model_Dance_Reveal.mp4",
        top_hook="WAIT TILL THE TURN... 😳",
        sub_hook="SHE DOESN'T ACTUALLY EXIST 💃",
        voice_text="Wait for the turn! She looks 100 percent real, but this entire virtual model was generated on a phone in 15 minutes. Tap Visit Profile to get the full 5-day prompt launch kit for just 199 rupees today!",
        video_source=os.path.join(RAW_HOOKS_DIR, "Hook-Option-04-Bollywood-Welcoming-Sway.mp4"),
        still_image_path=os.path.join(NEW_PERSONAS_DIR, "indian_model_look_b_wine_saree_glamour.jpg"),
        bottom_p1="100% AI Generated Dance Motion 💃\nZero real models or expensive gear!",
        bottom_p2="Tap 'Visit Profile' to grab the ₹199 Kit 👇\n250+ Character DNA Prompts & Workflow!",
        accent=(236, 72, 153)
    )

    # Ad 2: Curvaceous Athleisure - Over-Shoulder Dance Twirl to Balcony Reveal
    render_ad_video(
        out_name="Ad_Hook_02_Curvaceous_Athleisure_Dance_Twirl.mp4",
        top_hook="CAN YOU SPOT THE AI GLITCH? 🤔",
        sub_hook="WATCH HER WAIST & HAIR CLOSELY...",
        voice_text="Can you spot the AI glitch in her dance? Zero warping, perfect facial consistency, and smooth skin. We show you how to build your own virtual creator straight from your phone. Tap Visit Profile to get started today!",
        video_source=os.path.join(RAW_HOOKS_DIR, "Hook-Option-03-Over-Shoulder-Twirl.mp4"),
        still_image_path=os.path.join(NEW_PERSONAS_DIR, "persona_05_remake_fair_busty_athleisure.jpg"),
        bottom_p1="Notice the facial consistency 🧬\nBone structure stays 100% locked!",
        bottom_p2="Unlock the 5-Day Launch Kit (Only ₹199) 📱\nTap 'Visit Profile' on @personalabsacademy!",
        accent=(168, 85, 247)
    )

    # Ad 3: Emerald Satin Luxury Evening - Turn Around Hook to Rooftop Reveal
    render_ad_video(
        out_name="Ad_Hook_03_Emerald_Satin_Turn_Reveal.mp4",
        top_hook="STOP SCROLLING: SHE IS 100% AI 📸",
        sub_hook="ZERO CAMERAS • ZERO PHOTOSHOOT FEES",
        voice_text="Stop scrolling! Traditional photoshoots cost 50,000 rupees. We built this luxury virtual persona while drinking coffee on a smartphone. Visit our profile to copy our exact prompt vault!",
        video_source=os.path.join(RAW_HOOKS_DIR, "Hook-Option-05-Original-Turn-Around.mp4"),
        still_image_path=os.path.join(NEW_PERSONAS_DIR, "indian_model_look_a_evening_glamour.jpg"),
        bottom_p1="15 Minutes on a Smartphone ☕📱\n100% Consistent AI Influencer Persona!",
        bottom_p2="Instant Access to 250+ Master DNA Prompts 🚀\nTap 'Visit Profile' & DM 'LAUNCH'!",
        accent=(16, 185, 129)
    )

if __name__ == "__main__":
    main()
