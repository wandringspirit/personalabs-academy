import os
import sys
import re
import asyncio
import subprocess
import cv2
import numpy as np
import imageio_ffmpeg
import edge_tts
from PIL import Image, ImageDraw, ImageFont

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
AD_HOOKS_DIR = os.path.join(PROJECT_DIR, "ads-ready", "dancing-ad-hooks")
RAW_DIR = os.path.join(PROJECT_DIR, "ads-ready", "raw-gemini-videos")
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

def clean_text(text):
    if not text:
        return ""
    # Strip non-ascii / emoji characters that cause square glyphs in standard Windows fonts
    cleaned = re.sub(r'[^\x00-\x7F\u2022\u20B9]+', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def decorate_ad_frame(frame_bgr, top_hook, sub_hook, bottom_text, accent=(236, 72, 153)):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(0, 300):
        prog = (300 - y) / 300.0
        alpha = int(min(225, prog * 235))
        gd.line([(0, y), (RW, y)], fill=(8, 10, 20, alpha))
    for y in range(RH - 440, RH):
        prog = (y - (RH - 440)) / 440.0
        alpha = int(min(240, prog * 250))
        gd.line([(0, y), (RW, y)], fill=(8, 10, 20, alpha))
    pil.alpha_composite(grad)

    d = ImageDraw.Draw(pil, "RGBA")
    # Top profile pill
    d.rounded_rectangle((48, 54, 430, 106), radius=26, fill=(12, 14, 24, 230), outline=(accent[0], accent[1], accent[2], 200), width=2)
    d.ellipse((68, 71, 86, 89), fill=accent)
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    # Top hook banner
    clean_head = clean_text(top_hook)
    d.rounded_rectangle((48, 126, RW - 48, 222), radius=24, fill=(10, 14, 26, 235), outline=(accent[0], accent[1], accent[2], 220), width=2)
    d.text((RW // 2, 174), clean_head, font=FONT_HEAD, fill=(255, 255, 255), anchor="mm")

    # Sub-hook pattern interrupt pill
    if sub_hook:
        clean_sub = clean_text(sub_hook)
        d.rounded_rectangle((RW // 2 - 380, 244, RW // 2 + 380, 314), radius=20, fill=(accent[0], accent[1], accent[2], 245))
        d.text((RW // 2, 279), clean_sub, font=FONT_SUB, fill=(10, 14, 26), anchor="mm")

    # Bottom CTA Box
    if bottom_text:
        raw_lines = bottom_text.split("\n")
        lines = [clean_text(l) for l in raw_lines]
        line_h = 44
        total_h = len(lines) * line_h + 36
        d.rounded_rectangle((48, RH - 270, RW - 48, RH - 270 + total_h), radius=24, fill=(12, 16, 28, 235), outline=(56, 189, 248, 200), width=2)
        ty = RH - 270 + 20 + line_h // 2
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
    return 8.0

async def synth_voice(tts_text, out_mp3):
    comm = edge_tts.Communicate(tts_text, "en-US-AvaMultilingualNeural", rate="+10%", pitch="+0Hz")
    await comm.save(out_mp3)
    return get_audio_dur(out_mp3)

def render_gemini_ad(out_name, top_hook, sub_hook, voice_text, video_source, bottom_p1, bottom_p2, accent=(236, 72, 153)):
    out_path = os.path.join(AD_HOOKS_DIR, out_name)
    prefix = os.path.join(SCRATCH_DIR, f"tts_{out_name}")
    voice_mp3 = f"{prefix}_voice.mp3"
    
    dur = asyncio.run(synth_voice(voice_text, voice_mp3))
    total_dur = max(9.5, min(10.0, dur + 0.5))
    
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
    
    cap = cv2.VideoCapture(video_source)
    video_frames = []
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        h, w = frame.shape[:2]
        target_ratio = RW / RH
        cur_ratio = w / h
        if cur_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            cropped = frame[:, left:left+new_w]
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            cropped = frame[top:top+new_h, :]
        resized = cv2.resize(cropped, (RW, RH), interpolation=cv2.INTER_LANCZOS4)
        video_frames.append(resized)
    cap.release()
    
    if not video_frames:
        print(f"[ERROR] No frames from {video_source}")
        return

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", mixed_audio,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", "-shortest", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    switch_frame = int(round(total_frames * 0.45))
    for f_idx in range(total_frames):
        src_f = video_frames[f_idx % len(video_frames)]
        active_bottom = bottom_p1 if f_idx < switch_frame else bottom_p2
        decorated = decorate_ad_frame(src_f, top_hook, sub_hook, active_bottom, accent=accent)
        proc.stdin.write(decorated.tobytes())
        
    proc.stdin.close()
    proc.wait()
    
    for f in [voice_mp3, bgm_wav, mixed_audio]:
        if os.path.exists(f):
            os.remove(f)
    print(f"[OK] Generated: {out_name} ({os.path.getsize(out_path):,} bytes)")

def main():
    print("=== RENDERING HOTTEST HOOKS (ZERO GLYPH BOXES) ===")
    
    # Hook 1: Hypnotic Wine Saree Mudra Dance
    render_gemini_ad(
        out_name="Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4",
        top_hook="WAIT TILL THE TURN...",
        sub_hook="SHE DOESN'T ACTUALLY EXIST",
        voice_text="Wait for the turn! Look at her hands and waist. She looks 100 percent real, but this virtual Indian model was created on a phone in 15 minutes. Tap Visit Profile to get the full 5-day prompt launch kit for just 199 rupees!",
        video_source=os.path.join(RAW_DIR, "clip_02_wine_saree_mudra_dance.mp4"),
        bottom_p1="100% AI Indian Model Dance\nZero real models or studio fees!",
        bottom_p2="Tap 'Visit Profile' for the ₹199 Kit\n250+ Character DNA Prompts & Workflow!",
        accent=(236, 72, 153)
    )

    # Hook 2: Emerald Satin Rooftop Backless Turn
    render_gemini_ad(
        out_name="Hottest_Hook_02_Emerald_Satin_Backless_Turn.mp4",
        top_hook="STOP SCROLLING: SHE IS 100% AI",
        sub_hook="ZERO PHOTOSHOOT FEES • ZERO REAL MODELS",
        voice_text="Stop scrolling! Traditional agency photoshoots cost 50,000 rupees. We built this luxury virtual model drinking coffee on a smartphone. Visit our profile to copy our exact prompt system for 199 rupees!",
        video_source=os.path.join(RAW_DIR, "clip_03_emerald_satin_backless_turn.mp4"),
        bottom_p1="High-Fashion Luxury Persona\nLiquid Satin Rooftop Evening Look",
        bottom_p2="Unlock the 5-Day Launch Kit (Only ₹199)\nTap 'Visit Profile' on @personalabsacademy!",
        accent=(16, 185, 129)
    )

    # Hook 3: Champagne Corset VIP Nightclub Reveal
    render_gemini_ad(
        out_name="Hottest_Hook_03_Champagne_Corset_VIP_Club.mp4",
        top_hook="CAN YOU SPOT THE AI GLITCH?",
        sub_hook="WATCH HER EYES & CORSET CLOSELY...",
        voice_text="Can you spot the AI glitch in this video? Zero warping, perfect skin texture, and locked bone structure. We teach you how to build your own virtual creator straight from your phone. Tap Visit Profile to get started today!",
        video_source=os.path.join(RAW_DIR, "clip_07_champagne_corset_vip_lounge.mp4"),
        bottom_p1="Notice the facial consistency\nBone structure stays 100% locked!",
        bottom_p2="Launch Your Virtual Model in 5 Days (₹199)\nTap 'Visit Profile' on @personalabsacademy!",
        accent=(245, 158, 11)
    )

    # Hook 4: Mediterranean Resort Sun-Kissed Smile
    render_gemini_ad(
        out_name="Hottest_Hook_04_Mediterranean_Resort_Smile.mp4",
        top_hook="HUMAN OR AI? 97% GET THIS WRONG",
        sub_hook="MEET INDIA'S FIRST VIRTUAL RESORT MODEL",
        voice_text="Human or AI? 97% of people can't tell the difference. This luxury travel model was created on an iPhone without booking a single flight. Tap Visit Profile to grab the 199 rupee launch kit right now!",
        video_source=os.path.join(RAW_DIR, "clip_04_terracotta_resort_sun_smile.mp4"),
        bottom_p1="Luxury Travel Influencer Aesthetic\nBougainvillea Sun-Dappled Realism",
        bottom_p2="Get the Instant Prompt Vault for ₹199\nTap 'Visit Profile' on @personalabsacademy!",
        accent=(6, 182, 212)
    )

    # Hook 5: Full Bollywood Rooftop Saree Sway
    render_gemini_ad(
        out_name="Hottest_Hook_05_Bollywood_Rooftop_Sway.mp4",
        top_hook="AI MODELS ARE OFFICIALLY DANCING NOW",
        sub_hook="NO EXPENSIVE GEAR • JUST PROMPTS",
        voice_text="AI models are officially dancing! Fluid motion, zero face glitching, and perfect Indian facial consistency. Tap Visit Profile to get the 5-day prompt blueprint for just 199 rupees today!",
        video_source=os.path.join(RAW_DIR, "clip_05_wine_saree_rooftop_dance.mp4"),
        bottom_p1="100% AI Character Dance Motion\nZero camera gear needed!",
        bottom_p2="Build Your AI Influencer Today (₹199)\nTap 'Visit Profile' on @personalabsacademy!",
        accent=(236, 72, 153)
    )

if __name__ == "__main__":
    main()
