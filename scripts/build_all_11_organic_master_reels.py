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
BGM_PATH = os.path.join(PROJECT_DIR, "ads-ready", "bgm_master.mp3")
BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch", "master_11_organic")
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

FONT_HEAD = get_font("arialbd.ttf", 44)
FONT_SUB = get_font("segoeuib.ttf", 28)
FONT_TAG = get_font("segoeuib.ttf", 22)
FONT_CTA = get_font("arialbd.ttf", 34)

def clean_text(text):
    if not text:
        return ""
    cleaned = re.sub(r'[^\x00-\x7F\u2022\u20B9\U0001F000-\U0001FAFF]+', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def decorate_frame(frame_bgr, top_hook, sub_hook, trigger_word, bottom_sub, accent=(236, 72, 153)):
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

    # Bottom Organic Engagement CTA Box
    card_top = RH - 300
    card_h = 175
    d.rounded_rectangle((48, card_top, RW - 48, card_top + card_h), radius=24, fill=(12, 16, 28, 235), outline=(56, 189, 248, 220), width=2)

    # Line 1: Comment Trigger Callout
    cta_l1 = f'Comment "{trigger_word}" & Follow'
    d.text((RW // 2, card_top + 45), cta_l1, font=FONT_CTA, fill=(56, 189, 248), anchor="mm")

    # Line 2: Benefit / Delivery Promise
    cta_l2 = clean_text(bottom_sub)
    d.text((RW // 2, card_top + 105), cta_l2, font=FONT_SUB, fill=(240, 240, 255), anchor="mm")

    # Line 3: Small Trust Badge
    d.text((RW // 2, card_top + 145), "Instant Auto-DM \u2022 100% Free Mobile Blueprint", font=FONT_TAG, fill=(160, 175, 200), anchor="mm")

    return cv2.cvtColor(np.array(pil.convert("RGB")), cv2.COLOR_RGB2BGR)

def get_audio_dur(path):
    res = subprocess.run([FFMPEG_EXE, "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return 10.0

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
    mixed_audio = f"{prefix}_mixed.m4a"

    print(f"[Hook {hook_id:02d}] 1/4 Synthesizing Organic Engagement Voiceover...")
    dur = asyncio.run(synth_voice(cfg["voice_text"], voice_mp3))
    total_dur = dur + 1.25  # Exact 1.25s outro musical beat

    print(f"[Hook {hook_id:02d}] 2/4 Mixing Studio BGM (Zero Synthetic Buzz, {total_dur:.2f}s)...")
    bgm_offset = cfg.get("bgm_offset", (hook_id * 8.5) % 95)
    fade_start = max(0.0, total_dur - 0.8)

    # Use real tropical house BGM, trimmed and ducked under voiceover
    filter_str = (
        f"[1:a]atrim=start={bgm_offset:.2f}:end={bgm_offset + total_dur:.2f},"
        f"asetpts=PTS-STARTPTS,volume=0.20,afade=t=out:st={fade_start:.2f}:d=0.8[bgm];"
        f"[0:a]volume=1.45[vox];"
        f"[vox][bgm]amix=inputs=2:duration=longest:dropout_transition=2[aout]"
    )

    subprocess.run([
        FFMPEG_EXE, "-y",
        "-i", voice_mp3,
        "-i", BGM_PATH,
        "-filter_complex", filter_str,
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k",
        "-t", f"{total_dur:.2f}", mixed_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[Hook {hook_id:02d}] 3/4 Loading & Cropping Video Frames...")
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

    if "slices" in cfg and cfg["slices"]:
        reordered = []
        for s_start, s_end in cfg["slices"]:
            reordered.extend(raw_frames[s_start:s_end])
        raw_frames = reordered

    print(f"[Hook {hook_id:02d}] 4/4 Encoding 9:16 Video ({total_dur:.2f}s, {len(raw_frames)} frames)...")
    fps = 24
    total_frames = int(round(total_dur * fps))
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
        dec = decorate_frame(
            src_f,
            cfg["top_hook"],
            cfg["sub_hook"],
            cfg["trigger"],
            cfg["bottom_sub"],
            accent=cfg["accent"]
        )
        proc.stdin.write(dec.tobytes())

    proc.stdin.close()
    proc.wait()

    for f in [voice_mp3, mixed_audio]:
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
        # --- REELS 01 TO 05 (PROVEN WINNERS, CONVERTED TO 100% ORGANIC CTA) ---
        {
            "id": 1,
            "out_name": "Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4",
            "raw_file": "clip_02_wine_saree_mudra_dance.mp4",
            "top_hook": "WAIT TILL THE TURN...",
            "sub_hook": "SHE DOESN'T ACTUALLY EXIST",
            "trigger": "PROMPT",
            "bottom_sub": "I'll DM you the 250+ Character DNA Prompts!",
            "voice_text": "Wait for the turn! Look at her waist and hands. She looks totally real, but this virtual model was made on a phone in 15 minutes. Comment PROMPT below, follow our page, and I will DM you the complete launch kit right now!",
            "accent": (236, 72, 153),
            "slices": [(191, 240), (0, 107), (107, 191)],
            "bgm_offset": 0.0
        },
        {
            "id": 2,
            "out_name": "Hottest_Hook_02_Emerald_Satin_Backless_Turn.mp4",
            "raw_file": "clip_03_emerald_satin_backless_turn.mp4",
            "top_hook": "STOP SCROLLING: SHE IS 100% AI",
            "sub_hook": "ZERO PHOTOSHOOT FEES • ZERO REAL MODELS",
            "trigger": "MODEL",
            "bottom_sub": "I'll DM you our exact mobile prompt system!",
            "voice_text": "Stop scrolling! Traditional agency photoshoots cost 50,000 rupees. We built this luxury virtual model drinking coffee on a smartphone. Comment MODEL below, like and share, and I will DM you our exact prompt system!",
            "accent": (16, 185, 129),
            "slices": [(126, 240), (0, 126)],
            "bgm_offset": 12.0
        },
        {
            "id": 3,
            "out_name": "Hottest_Hook_03_Champagne_Corset_VIP_Club.mp4",
            "raw_file": "clip_07_champagne_corset_vip_lounge.mp4",
            "top_hook": "CAN YOU SPOT THE AI GLITCH?",
            "sub_hook": "WATCH HER EYES & CORSET CLOSELY...",
            "trigger": "GLITCH",
            "bottom_sub": "I'll DM you the Step-by-Step Phone Blueprint!",
            "voice_text": "Can you spot the AI glitch in this video? Zero warping, lifelike skin texture, and locked bone structure. Comment GLITCH below, follow our page, and I will DM you the phone blueprint to build your own model today!",
            "accent": (245, 158, 11),
            "slices": [(82, 125), (125, 161), (161, 240), (0, 82)],
            "bgm_offset": 24.0
        },
        {
            "id": 4,
            "out_name": "Hottest_Hook_04_Mediterranean_Resort_Smile.mp4",
            "raw_file": "clip_04_terracotta_resort_sun_smile.mp4",
            "top_hook": "HUMAN OR AI? 97% GET THIS WRONG",
            "sub_hook": "MEET THE NEXT-GEN VIRTUAL RESORT MODEL",
            "trigger": "TRAVEL",
            "bottom_sub": "I'll DM you the Instant Travel Prompt Vault!",
            "voice_text": "Human or AI? 97 percent get this wrong! This luxury travel model was created on an iPhone without booking a single flight. Comment TRAVEL below, like and follow, and I will DM you the full prompt vault today!",
            "accent": (6, 182, 212),
            "slices": [(108, 149), (36, 108), (149, 216), (216, 240), (0, 36)],
            "bgm_offset": 36.0
        },
        {
            "id": 5,
            "out_name": "Hottest_Hook_05_Bollywood_Rooftop_Sway.mp4",
            "raw_file": "clip_05_wine_saree_rooftop_dance.mp4",
            "top_hook": "AI MODELS ARE OFFICIALLY DANCING NOW",
            "sub_hook": "NO EXPENSIVE GEAR • JUST PROMPTS",
            "trigger": "DANCE",
            "bottom_sub": "I'll DM you the 5-Day Influencer Blueprint!",
            "voice_text": "AI models are officially dancing! Fluid motion, zero face glitches, and locked consistency. Comment DANCE below, follow our page, and I will DM you our 5-day prompt blueprint right now!",
            "accent": (236, 72, 153),
            "slices": [(65, 126), (126, 176), (176, 240), (0, 65)],
            "bgm_offset": 48.0
        },

        # --- REELS 06 TO 11 (NEW GEMINI DANCING FOOTAGE OF APPROVED AVATARS) ---
        {
            "id": 6,
            "out_name": "Hottest_Hook_06_Over_Shoulder_Backless_Twirl.mp4",
            "raw_file": "clip_11_new_gemini_a15828bf.mp4",
            "top_hook": "WAIT FOR THE TWIRL...",
            "sub_hook": "SHE DOESN'T ACTUALLY EXIST • 100% AI",
            "trigger": "TWIRL",
            "bottom_sub": "I'll DM you the 250+ Character DNA Bible!",
            "voice_text": "Wait for the twirl! Notice her natural waistline, smooth skin texture, and fluid dress motion. This hyper-realistic AI creator was built in 15 minutes right from a phone. Comment TWIRL below, like and follow, and I will DM you our exact prompt system!",
            "accent": (168, 85, 247),
            "bgm_offset": 60.0
        },
        {
            "id": 7,
            "out_name": "Hottest_Hook_07_Emotional_Waist_Dance_Sway.mp4",
            "raw_file": "clip_09_new_gemini_227910a8.mp4",
            "top_hook": "WATCH HER WAIST & MOVEMENT...",
            "sub_hook": "FLAWLESS REAL-TIME MOTION • ZERO GLITCHES",
            "trigger": "CREATOR",
            "bottom_sub": "I'll DM you the Step-by-Step Launch Kit!",
            "voice_text": "Watch her waist and movement! Pure fluid motion, authentic eye contact, and locked facial consistency. You do not need a studio to launch a viral model. Comment CREATOR below, follow our page, and I will DM you our 5-day launch kit!",
            "accent": (245, 158, 11),
            "bgm_offset": 72.0
        },
        {
            "id": 8,
            "out_name": "Hottest_Hook_08_Red_Silk_Rhythm_Sway.mp4",
            "raw_file": "clip_10_new_gemini_db2a7b3f.mp4",
            "top_hook": "THIS IS NOT A REAL VACATION",
            "sub_hook": "BUILT ON A SMARTPHONE IN 15 MINUTES",
            "trigger": "VACATION",
            "bottom_sub": "I'll DM you the Full Mobile Blueprint!",
            "voice_text": "This is not a real vacation! No flight tickets, zero hotel fees. We generated this entire coastal scene with locked facial consistency on a phone. Comment VACATION below, like and follow, and I will DM you our exact workflow!",
            "accent": (239, 68, 68),
            "bgm_offset": 84.0
        },
        {
            "id": 9,
            "out_name": "Hottest_Hook_09_Bollywood_Welcoming_Sweep.mp4",
            "raw_file": "clip_08_new_gemini_b3f85702.mp4",
            "top_hook": "LOOK AT HER SKIN & LIGHTING...",
            "sub_hook": "ZERO EDITING • 100% AI GENERATED",
            "trigger": "SKIN",
            "bottom_sub": "I'll DM you the Master Prompt Templates!",
            "voice_text": "Look at her skin and lighting! Notice the natural hair flow and authentic studio shadows. You do not need expensive cameras to build an AI model. Comment SKIN below, like and follow, and I will DM you the prompt vault today!",
            "accent": (16, 185, 129),
            "bgm_offset": 16.0
        },
        {
            "id": 10,
            "out_name": "Hottest_Hook_10_Classical_Mudra_Grace.mp4",
            "raw_file": "clip_09_new_gemini_227910a8.mp4",
            "top_hook": "AI CHARACTERS CAN DANCE NOW",
            "sub_hook": "FLUID MUDRA TURNS • ZERO FACE WARP",
            "trigger": "LAUNCH",
            "bottom_sub": "I'll DM you the Step-by-Step Blueprint!",
            "voice_text": "AI characters are officially dancing! Look at her hand gestures, fluid rhythm, and perfect face lock. You can build your own digital brand from home. Comment LAUNCH below, follow our page, and I will DM you the 5-day system this week!",
            "accent": (59, 130, 246),
            "bgm_offset": 28.0
        },
        {
            "id": 11,
            "out_name": "Hottest_Hook_11_Sunset_Skyline_Radiant_Dance.mp4",
            "raw_file": "clip_11_new_gemini_a15828bf.mp4",
            "top_hook": "CAN YOU SPOT THE AI GLITCH?",
            "sub_hook": "WATCH HER DRESS & BACKLESS TURN",
            "trigger": "VIP",
            "bottom_sub": "I'll DM you Instant Access to the Vault!",
            "voice_text": "Can you spot the AI glitch? Liquid fabric motion, seamless 180-degree twirl, and high-fashion couture lighting. Comment VIP below, like and follow, and I will DM you instant access to our master creator vault right now!",
            "accent": (236, 72, 153),
            "bgm_offset": 40.0
        }
    ]

    print("=== LAUNCHING COMPILATION OF ALL 11 ORGANIC MASTER DANCING REELS ===")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(process_single_hook, configs))

    print("\n=== ALL 11 ORGANIC MASTER DANCING REELS COMPILED SUCCESSFULLY ===")
    for name, size, total_dur, v_dur in sorted(results, key=lambda x: x[0]):
        print(f"  • {name}: {size:.2f} MB | Voice: {v_dur:.2f}s | Video: {total_dur:.2f}s (Outro: +{total_dur - v_dur:.2f}s)")

if __name__ == "__main__":
    main()
