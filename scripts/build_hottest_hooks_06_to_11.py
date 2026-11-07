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
import wave
import concurrent.futures

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
AD_HOOKS_DIR = os.path.join(PROJECT_DIR, "ads-ready", "dancing-ad-hooks")
RAW_DIR = os.path.join(PROJECT_DIR, "ads-ready", "raw-gemini-videos")
BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch", "new_hooks_06_11")
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
    cleaned = re.sub(r'[^\x00-\x7F\u2022\u20B9]+', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def decorate_frame(frame_bgr, top_hook, sub_hook, bottom_text, accent=(236, 72, 153)):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(0, 320):
        prog = (320 - y) / 320.0
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

    # Top Hook Banner
    top_clean = clean_text(top_hook)
    if top_clean:
        tb = d.textbbox((0, 0), top_clean, font=FONT_HEAD)
        tw = tb[2] - tb[0]
        pill_w = min(RW - 80, tw + 48)
        pill_h = (tb[3] - tb[1]) + 26
        pill_x = (RW - pill_w) // 2
        pill_y = 135
        d.rounded_rectangle((pill_x, pill_y, pill_x + pill_w, pill_y + pill_h), radius=18, fill=(10, 14, 26, 235), outline=(accent[0], accent[1], accent[2], 220), width=2)
        d.text((RW // 2, pill_y + pill_h // 2), top_clean, font=FONT_HEAD, fill=(255, 255, 255), anchor="mm")

    # Sub-hook pattern interrupt pill
    if sub_hook:
        clean_sub = clean_text(sub_hook)
        d.rounded_rectangle((RW // 2 - 380, 240, RW // 2 + 380, 310), radius=20, fill=(accent[0], accent[1], accent[2], 245))
        d.text((RW // 2, 275), clean_sub, font=FONT_SUB, fill=(10, 14, 26), anchor="mm")

    # Bottom Callout Card
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
    comm = edge_tts.Communicate(tts_text, "en-US-AvaMultilingualNeural", rate="+12%", pitch="+0Hz")
    await comm.save(out_mp3)
    return get_audio_dur(out_mp3)

def process_single_hook(cfg):
    hook_id = cfg["id"]
    out_name = cfg["out_name"]
    out_path = os.path.join(AD_HOOKS_DIR, out_name)
    raw_video = os.path.join(RAW_DIR, cfg["raw_file"])

    prefix = os.path.join(SCRATCH_DIR, f"hook_{hook_id:02d}")
    voice_mp3 = f"{prefix}_voice.mp3"
    bgm_wav = f"{prefix}_bgm.wav"
    mixed_audio = f"{prefix}_mixed.m4a"

    print(f"[Hook {hook_id:02d}] 1/4 Synthesizing Voiceover...")
    dur = asyncio.run(synth_voice(cfg["voice_text"], voice_mp3))
    total_dur = dur + 1.25  # Clean 1.25s outro musical beat so voice is never cut off!

    print(f"[Hook {hook_id:02d}] 2/4 Synthesizing Dynamic BGM Track ({total_dur:.2f}s)...")
    sr = 44100
    t = np.linspace(0, total_dur, int(sr * total_dur), endpoint=False)
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.2 * t) ** 4
    freq = cfg.get("freq", 146.83)
    synth_pad = (0.30 * np.sin(2 * np.pi * freq * t) + 0.20 * np.sin(2 * np.pi * (freq * 1.5) * t)) * (0.05 * beat_env)
    stereo_bgm = np.column_stack([synth_pad, synth_pad]).astype(np.float32)

    with wave.open(bgm_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((stereo_bgm * 32767).astype(np.int16).tobytes())

    fade_start = max(0.0, total_dur - 0.8)
    subprocess.run([
        FFMPEG_EXE, "-y", "-i", voice_mp3, "-i", bgm_wav,
        "-filter_complex", f"[0:a]volume=1.35[v];[1:a]volume=0.85,afade=t=out:st={fade_start:.2f}:d=0.8[b];[v][b]amix=inputs=2:duration=longest:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", "-t", f"{total_dur:.2f}", mixed_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[Hook {hook_id:02d}] 3/4 Loading & Cropping Video Motion Frames...")
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

    if not raw_frames:
        raise ValueError(f"Could not load frames from {raw_video}")

    print(f"[Hook {hook_id:02d}] 4/4 Encoding Master Video ({total_dur:.2f}s, {len(raw_frames)} source frames)...")
    fps = 24
    total_frames = int(round(total_dur * fps))
    switch_frame = int(round(total_frames * 0.45))
    n_raw = len(raw_frames)

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", mixed_audio,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for f_idx in range(total_frames):
        src_f = raw_frames[f_idx % n_raw]
        active_bottom = cfg["bottom_p1"] if f_idx < switch_frame else cfg["bottom_p2"]
        dec = decorate_frame(src_f, cfg["top_hook"], cfg["sub_hook"], active_bottom, accent=cfg["accent"])
        proc.stdin.write(dec.tobytes())

    proc.stdin.close()
    proc.wait()

    for f in [voice_mp3, bgm_wav, mixed_audio]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass

    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"[Hook {hook_id:02d} DONE] {size_mb:.2f} MB -> {out_name}")
    return out_name, size_mb, total_dur, dur

def main():
    configs = [
        {
            "id": 6,
            "out_name": "Hottest_Hook_06_Over_Shoulder_Backless_Twirl.mp4",
            "raw_file": "clip_11_new_gemini_a15828bf.mp4",
            "top_hook": "WAIT FOR THE TWIRL...",
            "sub_hook": "SHE DOESN'T ACTUALLY EXIST • 100% AI",
            "voice_text": "Wait for the twirl! Notice her natural waistline, smooth skin texture, and fluid dress motion. This hyper-realistic AI creator was built in 15 minutes right from a phone. Tap below to copy our exact prompt system!",
            "bottom_p1": "100% Hyper-Realistic Virtual Creator\nZero photoshoot or camera crew fees!",
            "bottom_p2": "Tap Below for the Launch Kit\n250+ Character DNA Prompts & Workflow!",
            "accent": (168, 85, 247),
            "freq": 155.56
        },
        {
            "id": 7,
            "out_name": "Hottest_Hook_07_Emotional_Waist_Dance_Sway.mp4",
            "raw_file": "clip_09_new_gemini_227910a8.mp4",
            "top_hook": "WATCH HER WAIST & MOVEMENT...",
            "sub_hook": "FLAWLESS REAL-TIME MOTION • ZERO GLITCHES",
            "voice_text": "Watch her waist and movement! Pure fluid motion, authentic eye contact, and locked facial consistency. You do not need a high-end studio to launch a viral virtual model. Tap below to get our 5-day launch kit!",
            "bottom_p1": "Flawless Fluid Dance Motion\n100% locked facial consistency!",
            "bottom_p2": "Tap Below for the Launch Kit\nStep-by-step mobile cloud workflow!",
            "accent": (245, 158, 11),
            "freq": 164.81
        },
        {
            "id": 8,
            "out_name": "Hottest_Hook_08_Red_Silk_Rhythm_Sway.mp4",
            "raw_file": "clip_10_new_gemini_db2a7b3f.mp4",
            "top_hook": "THIS IS NOT A REAL VACATION",
            "sub_hook": "BUILT ON A SMARTPHONE IN 15 MINUTES",
            "voice_text": "This is not a real vacation! No flight tickets, no luxury resort bookings. We generated this entire coastal influencer scene with locked facial consistency on a phone. Tap below to copy our exact workflow!",
            "bottom_p1": "High-Converting Travel Persona\nZero travel or equipment expenses!",
            "bottom_p2": "Tap Below for Instant Access\nFull 5-Day Influencer Blueprint!",
            "accent": (239, 68, 68),
            "freq": 174.61
        },
        {
            "id": 9,
            "out_name": "Hottest_Hook_09_Bollywood_Welcoming_Sweep.mp4",
            "raw_file": "clip_08_new_gemini_b3f85702.mp4",
            "top_hook": "LOOK AT HER SKIN & LIGHTING...",
            "sub_hook": "ZERO EDITING • 100% AI GENERATED",
            "voice_text": "Look at her skin and lighting! Notice the natural hair flow and authentic studio shadows. Most people think you need expensive cameras, but this was generated entirely with prompts. Tap below to unlock the vault today!",
            "bottom_p1": "Pristine Luxury Lifestyle Aesthetic\n100% unretouched skin micro-texture!",
            "bottom_p2": "Tap Below to Grab the Prompts\nOver 250+ Master Production Templates!",
            "accent": (16, 185, 129),
            "freq": 185.00
        },
        {
            "id": 10,
            "out_name": "Hottest_Hook_10_Classical_Mudra_Grace.mp4",
            "raw_file": "clip_09_new_gemini_227910a8.mp4",
            "top_hook": "AI CHARACTERS CAN DANCE NOW",
            "sub_hook": "FLUID MUDRA TURNS • ZERO FACE WARP",
            "voice_text": "AI characters are officially dancing! Look at her hand gestures, fluid rhythm, and perfect face lock. You can build your own digital brand without ever showing your face on camera. Tap below to launch your model in 5 days!",
            "bottom_p1": "Rhythmic High-Energy Dance Motion\nNatural hand mudras and joyful eye contact!",
            "bottom_p2": "Tap Below for the 5-Day System\nLaunch your profitable model this week!",
            "accent": (59, 130, 246),
            "freq": 196.00
        },
        {
            "id": 11,
            "out_name": "Hottest_Hook_11_Sunset_Skyline_Radiant_Dance.mp4",
            "raw_file": "clip_11_new_gemini_a15828bf.mp4",
            "top_hook": "CAN YOU SPOT THE AI GLITCH?",
            "sub_hook": "WATCH HER DRESS & BACKLESS TURN",
            "voice_text": "Can you spot the AI glitch? Liquid fabric motion, seamless 180-degree twirl, and high-fashion couture lighting. Discover the exact mobile workflow top digital creators are using right now. Tap below to get instant access!",
            "bottom_p1": "Architectural Couture Night Silhouette\nZero glitching • Zero studio fees!",
            "bottom_p2": "Tap Below for Instant Access\nJoin @personalabsacademy Today!",
            "accent": (236, 72, 153),
            "freq": 207.65
        }
    ]

    print("=== LAUNCHING HOOKS 06 TO 11 WITH NEW GEMINI DANCING FOOTAGE ===")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(process_single_hook, configs))

    print("\n=== ALL 6 NEW DANCING HOOKS COMPILED SUCCESSFULLY ===")
    for name, size, total_dur, v_dur in results:
        print(f"  • {name}: {size:.2f} MB | Voice: {v_dur:.2f}s | Video: {total_dur:.2f}s (Outro: +{total_dur - v_dur:.2f}s)")

if __name__ == "__main__":
    main()
