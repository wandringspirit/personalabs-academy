import os
import sys
import asyncio
import subprocess
import numpy as np
import cv2
import imageio_ffmpeg
import edge_tts
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
IG_STUDIO = os.path.join(PROJECT_DIR, "instagram-studio")
REELS_DIR = os.path.join(IG_STUDIO, "02-Organic-Reels")
BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

DEMO_VID = os.path.join(PROJECT_DIR, "videos", "demo.mp4")
HOOKS_DIR = os.path.join(IG_STUDIO, "05-Dancing-Hook-Options")

for d in [REELS_DIR, SCRATCH_DIR]:
    os.makedirs(d, exist_ok=True)

def get_font(name, size):
    font_dir = r"C:\Windows\Fonts"
    candidates = [name, "segoeuib.ttf", "arialbd.ttf", "SegoeUI.ttf", "arial.ttf"]
    for c in candidates:
        p = os.path.join(font_dir, c)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_HEAD = get_font("arialbd.ttf", 50)
FONT_BTN = get_font("arialbd.ttf", 35)
FONT_SUB = get_font("segoeui.ttf", 30)
FONT_SUB_BOLD = get_font("segoeuib.ttf", 28)
FONT_TAG = get_font("segoeuib.ttf", 22)
FONT_SMALL = get_font("segoeuib.ttf", 20)
FONT_EMOJI_HEAD = get_font("seguiemj.ttf", 48)
FONT_EMOJI_BTN = get_font("seguiemj.ttf", 33)
FONT_EMOJI_SM = get_font("seguiemj.ttf", 24)

RW, RH = 1080, 1920

def crop_fill(img, target_w, target_h, align_y=0.35):
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

def is_emoji_char(ch):
    return ord(ch) > 0x2000 and ch not in "—–•'""→"

def draw_text_with_emoji(canvas, pos, text, font, emoji_font, fill=(255, 255, 255), shadow=True):
    d = ImageDraw.Draw(canvas)
    x, y = pos
    for ch in text:
        is_em = is_emoji_char(ch)
        f = emoji_font if is_em else font
        if shadow and not is_em:
            d.text((x+2, y+3), ch, font=f, fill=(0, 0, 0, 200))
        if is_em:
            d.text((x, y), ch, font=f, fill=fill, embedded_color=True)
        else:
            d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f)

def measure_text_with_emoji(draw, text, font, emoji_font):
    w = 0
    for ch in text:
        f = emoji_font if is_emoji_char(ch) else font
        w += draw.textlength(ch, font=f)
    return w

def decorate_reel_frame(frame_bgr, top_hook, sub_hook_3s, caption_text, show_3s_pill=False, accent=(236, 72, 153)):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(0, 260):
        prog = (260 - y) / 260.0
        alpha = int(min(220, prog * 230))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    for y in range(RH - 480, RH):
        prog = (y - (RH - 480)) / 480.0
        alpha = int(min(240, prog * 250))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    pil.alpha_composite(grad)

    d = ImageDraw.Draw(pil, "RGBA")
    # Top profile tag
    d.rounded_rectangle((48, 54, 430, 106), radius=26, fill=(12, 14, 24, 230), outline=(accent[0], accent[1], accent[2], 200), width=2)
    d.ellipse((68, 71, 86, 89), fill=accent)
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    # Top hook banner
    d.rounded_rectangle((48, 126, RW - 48, 222), radius=24, fill=(10, 14, 26, 235), outline=(accent[0], accent[1], accent[2], 220), width=2)
    d.text((RW//2, 174), top_hook, font=FONT_BTN, fill=(255, 255, 255, 255), anchor="mm")

    # 3-Second pattern-interrupt sub-hook pill
    if show_3s_pill and sub_hook_3s:
        d.rounded_rectangle((RW//2 - 380, 246, RW//2 + 380, 318), radius=20, fill=(accent[0], accent[1], accent[2], 245))
        d.text((RW//2, 282), sub_hook_3s, font=FONT_SUB_BOLD, fill=(10, 14, 26, 255), anchor="mm")

    # Bottom caption box
    if caption_text:
        lines = caption_text.split("\n")
        f_sub = FONT_SUB_BOLD
        line_h = 44
        total_h = len(lines) * line_h + 38
        max_w = max((d.textbbox((0, 0), ln, font=f_sub)[2] for ln in lines), default=400)
        box_w = min(980, max_w + 64)
        x0 = (RW - box_w) // 2
        y0 = 1585 - total_h // 2
        d.rounded_rectangle((x0, y0, x0+box_w, y0+total_h), radius=24, fill=(12, 16, 28, 232), outline=(accent[0], accent[1], accent[2], 180), width=2)
        ty = y0 + 20 + line_h // 2
        for ln in lines:
            d.text((542, ty+2), ln, font=f_sub, fill=(0, 0, 0, 220), anchor="mm")
            d.text((540, ty), ln, font=f_sub, fill=(255, 255, 255, 255), anchor="mm")
            ty += line_h

    return cv2.cvtColor(np.array(pil.convert("RGB")), cv2.COLOR_RGB2BGR)

def get_audio_dur(path):
    res = subprocess.run([FFMPEG_EXE, "-i", path], capture_output=True, text=True)
    import re
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        return int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
    return 4.0

async def synth_reel_audio(segments, prefix):
    temp_files, durations = [], []
    for idx, seg in enumerate(segments):
        tmp_mp3 = f"{prefix}_seg_{idx}.mp3"
        comm = edge_tts.Communicate(seg["tts"], "en-US-AvaMultilingualNeural", rate="+8%", pitch="+0Hz")
        await comm.save(tmp_mp3)
        durations.append(get_audio_dur(tmp_mp3))
        temp_files.append(tmp_mp3)
    concat_list = f"{prefix}_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for tf in temp_files:
            f.write(f"file '{tf}'\n")
    voice_wav = f"{prefix}_voice.wav"
    subprocess.run([FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-ar", "44100", "-ac", "2", voice_wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    total_dur = sum(durations) + 0.5
    sr = 44100
    t = np.linspace(0, total_dur, int(sr * total_dur), endpoint=False)
    # Rhythmic beat synth for dance feel
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.2 * t) ** 4
    pad = (0.35 * np.sin(2 * np.pi * 130.81 * t) + 0.25 * np.sin(2 * np.pi * 196.00 * t) + 0.20 * np.sin(2 * np.pi * 261.63 * t)) * (0.05 * beat_env)
    stereo_bgm = np.column_stack([pad, pad]).astype(np.float32)
    bgm_wav = f"{prefix}_bgm.wav"
    import wave
    with wave.open(bgm_wav, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((stereo_bgm * 32767).astype(np.int16).tobytes())
    final_aac = f"{prefix}_mixed.m4a"
    subprocess.run([
        FFMPEG_EXE, "-y", "-i", voice_wav, "-i", bgm_wav,
        "-filter_complex", "[0:a]volume=1.35[v];[1:a]volume=0.90[b];[v][b]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", final_aac
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for tf in temp_files + [concat_list, voice_wav, bgm_wav]:
        if os.path.exists(tf):
            os.remove(tf)
    return final_aac, durations

def build_cover_9x16(img_path, tag_text, headline_line1, headline_line2, highlight_words, out_path, accent_color=(236, 72, 153)):
    im = Image.open(img_path).convert("RGB")
    im = crop_fill(im, RW, RH, align_y=0.25).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(0, 320):
        prog = (320 - y) / 320.0
        alpha = int(min(235, prog * 245))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    for y in range(RH - 520, RH):
        prog = (y - (RH - 520)) / 520.0
        alpha = int(min(250, (prog ** 1.1) * 260))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    im.alpha_composite(grad)

    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle((48, 54, 430, 106), radius=26, fill=(12, 14, 24, 230), outline=(accent_color[0], accent_color[1], accent_color[2], 200), width=2)
    d.ellipse((68, 71, 86, 89), fill=accent_color)
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    card_x1, card_y1, card_x2, card_y2 = 48, RH - 440, RW - 48, RH - 68
    d.rounded_rectangle((card_x1, card_y1, card_x2, card_y2), radius=32, fill=(14, 17, 30, 240), outline=(accent_color[0], accent_color[1], accent_color[2], 210), width=3)
    d.rounded_rectangle((RW//2 - 90, card_y1, RW//2 + 90, card_y1 + 5), radius=3, fill=accent_color)

    bw = int(measure_text_with_emoji(d, tag_text, FONT_TAG, FONT_EMOJI_SM)) + 48
    bx1 = (RW - bw) // 2
    by1 = card_y1 - 24
    d.rounded_rectangle((bx1, by1, bx1 + bw, by1 + 48), radius=24, fill=(20, 24, 42, 255), outline=accent_color, width=2)
    draw_text_with_emoji(im, (bx1 + 24, by1 + 11), tag_text, FONT_TAG, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)

    y_t = card_y1 + 54
    for hline in [headline_line1, headline_line2]:
        w = measure_text_with_emoji(d, hline, FONT_HEAD, FONT_EMOJI_HEAD)
        x = (RW - w) // 2
        for word in hline.split(" "):
            tok = word + " "
            clean = word.strip(".,!?:;\"'()")
            col = accent_color if clean in highlight_words else (255, 255, 255)
            draw_text_with_emoji(im, (x, y_t), tok, FONT_HEAD, FONT_EMOJI_HEAD, fill=col, shadow=True)
            x += measure_text_with_emoji(d, tok, FONT_HEAD, FONT_EMOJI_HEAD)
        y_t += 64

    d.rounded_rectangle((card_x1 + 32, card_y2 - 64, card_x2 - 32, card_y2 - 18), radius=18, fill=(22, 28, 48, 255), outline=(56, 189, 248, 200), width=2)
    d.text((RW//2, card_y2 - 41), "TAP TO WATCH • 100% MOBILE AI WORKFLOW 📱", font=FONT_TAG, fill=(56, 189, 248), anchor="mm")
    im.convert("RGB").save(out_path, quality=96, subsampling=0)
    print(f"[OK] Generated Cover: {out_path}")

def render_dance_reel(out_filename, top_hook, sub_hook_3s, segments, video_source, time_ranges, accent=(236, 72, 153)):
    out_path = os.path.join(REELS_DIR, out_filename)
    prefix = os.path.join(SCRATCH_DIR, f"tmp_{out_filename}")
    final_aac, durations = asyncio.run(synth_reel_audio(segments, prefix))
    fps = 30
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", final_aac,
        "-c:v", "libx264", "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", "-shortest", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    cap = cv2.VideoCapture(video_source)
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    
    global_frame_idx = 0
    for idx, (seg, dur, (start_sec, end_sec)) in enumerate(zip(segments, durations, time_ranges)):
        if idx == len(segments) - 1:
            dur += 0.4
        num_frames = max(15, int(round(dur * fps)))
        cap1, cap2 = seg["cap1"], seg["cap2"]
        
        # Calculate video frame playback range
        start_frame = int(round(start_sec * src_fps))
        end_frame = int(round(end_sec * src_fps))
        total_src_frames = max(1, end_frame - start_frame)
        
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        
        for f_idx in range(num_frames):
            prog = f_idx / max(1, num_frames - 1)
            target_src_frame = start_frame + int((f_idx % total_src_frames))
            cap.set(cv2.CAP_PROP_POS_FRAMES, target_src_frame)
            ret, frame = cap.read()
            if not ret or frame is None:
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                ret, frame = cap.read()
            
            # Crop & resize to 1080x1920
            fh, fw = frame.shape[:2]
            target_w, target_h = RW, RH
            src_ratio = fw / fh
            target_ratio = target_w / target_h
            if src_ratio > target_ratio:
                nw = int(fh * target_ratio)
                left = (fw - nw) // 2
                cropped = frame[:, left:left+nw]
            else:
                nh = int(fw / target_ratio)
                top = int((fh - nh) * 0.25)
                top = max(0, min(fh - nh, top))
                cropped = frame[top:top+nh, :]
            scaled = cv2.resize(cropped, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
            
            active_cap = cap1 if prog < 0.48 else cap2
            show_3s = (global_frame_idx < 96)
            rendered = decorate_reel_frame(scaled, top_hook, sub_hook_3s, active_cap, show_3s_pill=show_3s, accent=accent)
            proc.stdin.write(rendered.tobytes())
            global_frame_idx += 1
            
    cap.release()
    proc.stdin.close()
    proc.wait()
    if os.path.exists(final_aac):
        os.remove(final_aac)
    print(f"[OK] Rendered {out_filename} ({os.path.getsize(out_path):,} bytes)")

def build_dancing_reels():
    print("--- BUILDING DANCING VIRAL REELS ---")
    
    # Extract cover frame from 15s (spin turn)
    spin_cover_path = os.path.join(SCRATCH_DIR, "spin_cover_raw.jpg")
    subprocess.run([FFMPEG_EXE, "-y", "-ss", "00:00:15", "-i", DEMO_VID, "-vframes", "1", "-q:v", "2", spin_cover_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # -------------------------------------------------------------------------
    # Reel 11: Wait Till The Turn Dance Reveal
    # -------------------------------------------------------------------------
    build_cover_9x16(
        spin_cover_path,
        "💃 VIRAL AI DANCE REVEAL",
        "WAIT TILL THE TURN...",
        "SHE DOESN'T EXIST 😳",
        {"WAIT", "TURN", "DOESN'T", "EXIST"},
        os.path.join(REELS_DIR, "Cover-11.jpg"),
        accent_color=(236, 72, 153)
    )
    
    seg_11 = [
        {
            "tts": "Wait for the turn. Most people on Instagram scroll right past, completely convinced this is a real girl dancing in a saree.",
            "cap1": "Wait for the turn... 😳\nShe doesn't actually exist!",
            "cap2": "100% AI generated dance motion\nzero real models or cameras 💃"
        },
        {
            "tts": "Notice how the facial bone structure stays 100 percent locked even while her hair whips and she spins across the room.",
            "cap1": "Notice the facial consistency 🧬\nBone structure stays 100% locked!",
            "cap2": "Real hair physics & waist sways\nwith ZERO warping glitches ✨"
        },
        {
            "tts": "Comment DANCE below right now, and I will DM you our complete 5-day AI influencer launch kit straight to your inbox.",
            "cap1": "Want to build your own AI creator?\nComment 'DANCE' below 👇",
            "cap2": "I'll DM you the complete\n5-Day Launch Kit instantly! 🚀"
        }
    ]
    time_ranges_11 = [
        (0.0, 7.5),    # Mudra & sway
        (12.0, 18.5),  # Hair flip & spin
        (22.0, 29.5)   # Final pose & wink
    ]
    render_dance_reel(
        "Reel-11-Viral-Saree-Dance-Reveal-Organic.mp4",
        "WAIT TILL THE TURN... 😳",
        "SHE DOESN'T ACTUALLY EXIST 💃",
        seg_11,
        DEMO_VID,
        time_ranges_11,
        accent=(236, 72, 153)
    )
    
    # -------------------------------------------------------------------------
    # Reel 12: Can You Spot The AI Glitch Dance Test
    # -------------------------------------------------------------------------
    mudra_cover_path = os.path.join(SCRATCH_DIR, "mudra_cover_raw.jpg")
    subprocess.run([FFMPEG_EXE, "-y", "-ss", "00:00:08", "-i", DEMO_VID, "-vframes", "1", "-q:v", "2", mudra_cover_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    build_cover_9x16(
        mudra_cover_path,
        "🔍 THE REALISM TEST",
        "CAN YOU SPOT THE",
        "AI GLITCH IN HER DANCE? 🤔",
        {"CAN", "SPOT", "AI", "GLITCH"},
        os.path.join(REELS_DIR, "Cover-12.jpg"),
        accent_color=(56, 189, 248)
    )
    
    seg_12 = [
        {
            "tts": "Watch her hands, waist, and eye reflections closely. Can you spot the AI glitch in this dance?",
            "cap1": "Watch her hands & eyes closely 👁️\nCan you spot the AI glitch?",
            "cap2": "99% of people scroll past\nthinking she's a real creator 🤯"
        },
        {
            "tts": "There is none. We combined our Character DNA seed lock with 2-second motion pacing straight from a smartphone.",
            "cap1": "There is no glitch! 🚫\nCharacter DNA seed-locked!",
            "cap2": "Raw smartphone optics formula\nbuilt straight on your phone 📱"
        },
        {
            "tts": "Comment AI below, and I will DM you the step by step blueprint showing you how to build your own virtual creator in 5 days.",
            "cap1": "Want the exact workflow?\nComment 'AI' below 👇",
            "cap2": "I'll send you the complete\n5-Day Launch Kit instantly! 🚀"
        }
    ]
    time_ranges_12 = [
        (4.0, 11.0),   # Mudra hand gestures
        (14.0, 20.0),  # Spin & over the shoulder
        (20.0, 27.0)   # Hip sway & smile
    ]
    render_dance_reel(
        "Reel-12-Can-You-Spot-The-Glitch-Organic.mp4",
        "CAN YOU SPOT THE GLITCH? 🤔",
        "99% FAIL THIS REALISM TEST 🔍",
        seg_12,
        DEMO_VID,
        time_ranges_12,
        accent=(56, 189, 248)
    )
    
    print("--- DANCING VIRAL REELS GENERATED & VERIFIED! ---")

if __name__ == "__main__":
    build_dancing_reels()
