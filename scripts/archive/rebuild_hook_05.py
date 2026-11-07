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
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return 9.0

async def synth_voice(tts_text, out_mp3):
    comm = edge_tts.Communicate(tts_text, "en-US-AvaMultilingualNeural", rate="+10%", pitch="+0Hz")
    await comm.save(out_mp3)
    return get_audio_dur(out_mp3)

def rebuild_hook_05():
    out_name = "Hottest_Hook_05_Bollywood_Rooftop_Sway.mp4"
    out_path = os.path.join(AD_HOOKS_DIR, out_name)
    raw_video = os.path.join(RAW_DIR, "clip_05_wine_saree_rooftop_dance.mp4")
    
    top_hook = "AI MODELS ARE OFFICIALLY DANCING NOW"
    sub_hook = "NO EXPENSIVE GEAR • JUST PROMPTS"
    voice_text = "AI models are officially dancing! Fluid motion, zero face glitching, and perfect Indian facial consistency. Tap Visit Profile to get the 5-day prompt blueprint for just 199 rupees today!"
    bottom_p1 = "100% AI Character Dance Motion\nZero camera gear needed!"
    bottom_p2 = "Build Your AI Influencer Today (₹199)\nTap 'Visit Profile' on @personalabsacademy!"
    accent = (236, 72, 153)

    print("[1/5] Synthesizing Voiceover...")
    voice_mp3 = os.path.join(SCRATCH_DIR, "hook05_voice.mp3")
    dur = asyncio.run(synth_voice(voice_text, voice_mp3))
    total_dur = max(9.5, min(10.0, dur + 0.5))
    print(f"      Voice duration: {dur:.2f}s -> Target: {total_dur:.2f}s")

    print("[2/5] Creating Dynamic BGM Track...")
    sr = 44100
    t = np.linspace(0, total_dur, int(sr * total_dur), endpoint=False)
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.2 * t) ** 4
    synth_pad = (0.30 * np.sin(2 * np.pi * 146.83 * t) + 0.20 * np.sin(2 * np.pi * 220.00 * t)) * (0.05 * beat_env)
    stereo_bgm = np.column_stack([synth_pad, synth_pad]).astype(np.float32)
    bgm_wav = os.path.join(SCRATCH_DIR, "hook05_bgm.wav")
    import wave
    with wave.open(bgm_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((stereo_bgm * 32767).astype(np.int16).tobytes())

    mixed_audio = os.path.join(SCRATCH_DIR, "hook05_mixed.m4a")
    subprocess.run([
        FFMPEG_EXE, "-y", "-i", voice_mp3, "-i", bgm_wav,
        "-filter_complex", "[0:a]volume=1.35[v];[1:a]volume=0.85[b];[v][b]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", mixed_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("[3/5] Loading Raw Frames...")
    cap = cv2.VideoCapture(raw_video)
    raw_frames = []
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
        raw_frames.append(resized)
    cap.release()
    print(f"      Total raw frames loaded: {len(raw_frames)}")

    print("[4/5] Re-ordering Clips with Close-Up Smile as Opening Hook...")
    # Clip breakdown (240 frames total):
    # - Segment 2: Close-up approach & radiant direct smile (user requested hook): frames 65 to 125 (61 frames)
    # - Segment 3: Profile turn by the balcony: frames 126 to 175 (50 frames)
    # - Segment 4: Ocean breeze clutch pose: frames 176 to 239 (64 frames)
    # - Segment 1: Catwalk entrance: frames 0 to 64 (65 frames)
    
    reordered_frames = []
    # Opening hook (0:00 to ~2.6s): The radiant close-up smile
    reordered_frames.extend(raw_frames[65:126])
    # Glamour profile turn (~2.6s to 4.7s)
    reordered_frames.extend(raw_frames[126:176])
    # Golden hour seaside pose (~4.7s to 7.3s)
    reordered_frames.extend(raw_frames[176:240])
    # Runway catwalk & CTA resolution (~7.3s to 10.0s)
    reordered_frames.extend(raw_frames[0:65])
    
    print(f"      Reordered frame sequence count: {len(reordered_frames)}")

    print("[5/5] Encoding High-Fidelity Master MP4...")
    fps = 24
    total_frames = int(round(total_dur * fps))
    switch_frame = int(round(total_frames * 0.45))

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", mixed_audio,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", "-shortest", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    for f_idx in range(total_frames):
        src_f = reordered_frames[f_idx % len(reordered_frames)]
        active_bottom = bottom_p1 if f_idx < switch_frame else bottom_p2
        decorated = decorate_ad_frame(src_f, top_hook, sub_hook, active_bottom, accent=accent)
        proc.stdin.write(decorated.tobytes())
        
    proc.stdin.close()
    proc.wait()

    # Clean up temp audio files
    for f in [voice_mp3, bgm_wav, mixed_audio]:
        if os.path.exists(f):
            os.remove(f)

    file_size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"[DONE] Successfully rebuilt {out_name}: {file_size_mb:.2f} MB")

if __name__ == "__main__":
    rebuild_hook_05()
