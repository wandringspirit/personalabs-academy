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
import concurrent.futures

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

def process_single_hook(cfg):
    hook_id = cfg["id"]
    out_name = cfg["out_name"]
    out_path = os.path.join(AD_HOOKS_DIR, out_name)
    raw_video = os.path.join(RAW_DIR, cfg["raw_file"])
    
    prefix = os.path.join(SCRATCH_DIR, f"par_{hook_id}")
    voice_mp3 = f"{prefix}_voice.mp3"
    bgm_wav = f"{prefix}_bgm.wav"
    mixed_audio = f"{prefix}_mixed.m4a"

    print(f"[Hook {hook_id}] 1/4 Synthesizing Voiceover...")
    dur = asyncio.run(synth_voice(cfg["voice_text"], voice_mp3))
    total_dur = max(9.5, min(10.0, dur + 0.5))

    print(f"[Hook {hook_id}] 2/4 Synthesizing Dynamic BGM...")
    sr = 44100
    t = np.linspace(0, total_dur, int(sr * total_dur), endpoint=False)
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.2 * t) ** 4
    synth_pad = (0.30 * np.sin(2 * np.pi * 146.83 * t) + 0.20 * np.sin(2 * np.pi * 220.00 * t)) * (0.05 * beat_env)
    stereo_bgm = np.column_stack([synth_pad, synth_pad]).astype(np.float32)
    
    import wave
    with wave.open(bgm_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((stereo_bgm * 32767).astype(np.int16).tobytes())

    subprocess.run([
        FFMPEG_EXE, "-y", "-i", voice_mp3, "-i", bgm_wav,
        "-filter_complex", "[0:a]volume=1.35[v];[1:a]volume=0.85[b];[v][b]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", mixed_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[Hook {hook_id}] 3/4 Loading & Slicing Video Frames...")
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

    reordered_frames = []
    for s_start, s_end in cfg["slices"]:
        reordered_frames.extend(raw_frames[s_start:s_end])

    print(f"[Hook {hook_id}] 4/4 Encoding Final Master Video ({len(reordered_frames)} frames)...")
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
        active_bottom = cfg["bottom_p1"] if f_idx < switch_frame else cfg["bottom_p2"]
        decorated = decorate_ad_frame(src_f, cfg["top_hook"], cfg["sub_hook"], active_bottom, accent=cfg["accent"])
        proc.stdin.write(decorated.tobytes())
        
    proc.stdin.close()
    proc.wait()

    for f in [voice_mp3, bgm_wav, mixed_audio]:
        if os.path.exists(f):
            os.remove(f)

    file_size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"[Hook {hook_id} DONE] Saved {out_name} ({file_size_mb:.2f} MB)")
    return out_name, file_size_mb

def main():
    configs = [
        {
            "id": 1,
            "out_name": "Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4",
            "raw_file": "clip_02_wine_saree_mudra_dance.mp4",
            "top_hook": "WAIT TILL THE TURN...",
            "sub_hook": "SHE DOESN'T ACTUALLY EXIST",
            "voice_text": "Wait for the turn! Look at her hands and waist. She looks 100 percent real, but this virtual Indian model was created on a phone in 15 minutes. Tap Visit Profile to get the full 5-day prompt launch kit for just 199 rupees!",
            "bottom_p1": "100% AI Indian Model Dance\nZero real models or studio fees!",
            "bottom_p2": "Tap 'Visit Profile' for the ₹199 Kit\n250+ Character DNA Prompts & Workflow!",
            "accent": (236, 72, 153),
            # Slices:
            # 1. Opening Hook: Radiant over-the-shoulder sunset smile (191:240)
            # 2. Mudra dance hand movements (0:107)
            # 3. Saree waist twirl by the ocean (107:191)
            "slices": [(191, 240), (0, 107), (107, 191)]
        },
        {
            "id": 2,
            "out_name": "Hottest_Hook_02_Emerald_Satin_Backless_Turn.mp4",
            "raw_file": "clip_03_emerald_satin_backless_turn.mp4",
            "top_hook": "STOP SCROLLING: SHE IS 100% AI",
            "sub_hook": "ZERO PHOTOSHOOT FEES • ZERO REAL MODELS",
            "voice_text": "Stop scrolling! Traditional agency photoshoots cost 50,000 rupees. We built this luxury virtual model drinking coffee on a smartphone. Visit our profile to copy our exact prompt system for 199 rupees!",
            "bottom_p1": "High-Fashion Luxury Persona\nLiquid Satin Rooftop Evening Look",
            "bottom_p2": "Unlock the 5-Day Launch Kit (Only ₹199)\nTap 'Visit Profile' on @personalabsacademy!",
            "accent": (16, 185, 129),
            # Slices:
            # 1. Opening Hook: Smooth turn & direct eye gaze with candlelight bokeh (126:240)
            # 2. Catwalk backless gown silhouette stroll (0:126)
            "slices": [(126, 240), (0, 126)]
        },
        {
            "id": 3,
            "out_name": "Hottest_Hook_03_Champagne_Corset_VIP_Club.mp4",
            "raw_file": "clip_07_champagne_corset_vip_lounge.mp4",
            "top_hook": "CAN YOU SPOT THE AI GLITCH?",
            "sub_hook": "WATCH HER EYES & CORSET CLOSELY...",
            "voice_text": "Can you spot the AI glitch in this video? Zero warping, perfect skin texture, and locked bone structure. We teach you how to build your own virtual creator straight from your phone. Tap Visit Profile to get started today!",
            "bottom_p1": "Notice the facial consistency\nBone structure stays 100% locked!",
            "bottom_p2": "Launch Your Virtual Model in 5 Days (₹199)\nTap 'Visit Profile' on @personalabsacademy!",
            "accent": (245, 158, 11),
            # Slices:
            # 1. Opening Hook: Close-up walking radiant direct smile (60:116)
            # 2. Glamour side turn towards lounge (116:161)
            # 3. Velvet barstool seated glamour pose (161:240)
            # 4. VIP entrance hallway walk (0:60)
            "slices": [(60, 116), (116, 161), (161, 240), (0, 60)]
        },
        {
            "id": 4,
            "out_name": "Hottest_Hook_04_Mediterranean_Resort_Smile.mp4",
            "raw_file": "clip_04_terracotta_resort_sun_smile.mp4",
            "top_hook": "HUMAN OR AI? 97% GET THIS WRONG",
            "sub_hook": "MEET INDIA'S FIRST VIRTUAL RESORT MODEL",
            "voice_text": "Human or AI? 97% of people can't tell the difference. This luxury travel model was created on an iPhone without booking a single flight. Tap Visit Profile to grab the 199 rupee launch kit right now!",
            "bottom_p1": "Luxury Travel Influencer Aesthetic\nBougainvillea Sun-Dappled Realism",
            "bottom_p2": "Get the Instant Prompt Vault for ₹199\nTap 'Visit Profile' on @personalabsacademy!",
            "accent": (6, 182, 212),
            # Slices:
            # 1. Opening Hook: Close-up sun-dappled bougainvillea radiant smile (36:109)
            # 2. Villa terrace balcony turn (109:149)
            # 3. Mediterranean garden walkway stroll (149:216)
            # 4. Sunlit entrance catwalk & CTA (216:240) + (0:36)
            "slices": [(36, 109), (109, 149), (149, 216), (216, 240), (0, 36)]
        }
    ]

    print(f"=== LAUNCHING PARALLEL HOOK RE-SEQUENCING (4 WORKERS) ===")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_hook, configs))

    print("\n=== ALL HOOKS SUCCESSFULLY RE-SEQUENCED & RENDERED ===")
    for name, size in results:
        print(f"  • {name}: {size:.2f} MB")

if __name__ == "__main__":
    main()
