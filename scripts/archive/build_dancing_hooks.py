import os
import subprocess
import cv2
import numpy as np
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
DEMO_VID = os.path.join(PROJECT_DIR, "videos", "demo.mp4")
CHINESE_VID = r"C:\Users\piyus\Downloads\Generating_Realistic_Chinese_Dress_Dance_Video.mp4"
REEL4_AUD = os.path.join(PROJECT_DIR, "instagram-studio", ".tmp_ad04", "reel4_hook_aud.wav")
OUT_DIR = os.path.join(PROJECT_DIR, "instagram-studio", "05-Dancing-Hook-Options")
ARTIFACT_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

RW, RH = 1080, 1920

def get_font(name, size):
    font_dir = r"C:\Windows\Fonts"
    for c in [name, "segoeuib.ttf", "arialbd.ttf", "SegoeUI.ttf", "arial.ttf"]:
        p = os.path.join(font_dir, c)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

F_HOOK = get_font("arialbd.ttf", 40)
F_SUB = get_font("segoeuib.ttf", 38)
F_PILL = get_font("segoeuib.ttf", 22)

def overlay_decorations(frame_bgr, subtitle_text):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    d = ImageDraw.Draw(pil, "RGBA")

    # 1. Top Hook Banner (Crisp typography, no glitchy emoji boxes)
    d.rounded_rectangle((50, 90, RW - 50, 205), radius=28, fill=(12, 16, 28, 235), outline=(168, 85, 247, 255), width=3)
    d.text((RW // 2, 148), "WHY 99% OF AI PHOTOS LOOK FAKE (3-WORD FIX)", font=F_HOOK, fill=(255, 255, 255), anchor="mm")

    # 2. Pill badges
    # Left pill: Optics feature
    d.rounded_rectangle((50, 222, 630, 286), radius=20, fill=(14, 18, 32, 245), outline=(56, 189, 248, 225), width=2)
    d.text((340, 254), "RAW IPHONE OPTICS • ZERO CGI GLOW", font=F_PILL, fill=(56, 189, 248), anchor="mm")

    # Right pill: Account Handle
    d.rounded_rectangle((655, 222, RW - 50, 286), radius=20, fill=(14, 18, 32, 245), outline=(168, 85, 247, 220), width=2)
    d.ellipse((680, 245, 698, 263), fill=(56, 189, 248, 255))
    d.text((710, 238), "@personalabsacademy", font=F_PILL, fill=(240, 248, 255))

    # 3. Bottom Subtitle
    if subtitle_text:
        bw, bh = 880, 84
        bx1 = (RW - bw) // 2
        by1 = 1560
        d.rounded_rectangle((bx1, by1, bx1 + bw, by1 + bh), radius=24, fill=(12, 16, 28, 235), outline=(56, 189, 248, 160), width=2)
        d.text((RW // 2, by1 + bh // 2 + 2), subtitle_text, font=F_SUB, fill=(0, 0, 0, 220), anchor="mm")
        d.text((RW // 2, by1 + bh // 2), subtitle_text, font=F_SUB, fill=(255, 255, 255), anchor="mm")

    return cv2.cvtColor(np.array(pil.convert("RGB")), cv2.COLOR_RGB2BGR)

def render_hook_video(source_video, start_sec, duration_sec, out_name, snap_name, is_landscape=False):
    out_path = os.path.join(OUT_DIR, out_name)
    snap_path = os.path.join(ARTIFACT_DIR, snap_name)
    fps = 30
    total_frames = int(round(duration_sec * fps))

    print(f"\n>>> Rendering [{out_name}]")
    cap = cv2.VideoCapture(source_video)
    src_fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(round(start_sec * src_fps))
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{RW}x{RH}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-i", REEL4_AUD,
        "-t", str(duration_sec),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    snap_frame_idx = int(round(1.8 * fps))

    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            ret, frame = cap.read()
            if not ret:
                break

        h, w = frame.shape[:2]
        scale = max(RW / w, RH / h)
        nw, nh = int(round(w * scale)), int(round(h * scale))
        resized = cv2.resize(frame, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
        x0 = (nw - RW) // 2
        y0 = (nh - RH) // 2
        cropped = resized[y0:y0+RH, x0:x0+RW]

        sub = "Why do 99% of AI influencer photos..." if i < int(fps * 2.1) else "...immediately scream 'FAKE PLASTIC'?"
        final_frame = overlay_decorations(cropped, sub)

        if i == snap_frame_idx:
            cv2.imwrite(snap_path, final_frame)
            print(f"  Saved clean snapshot: {snap_name}")

        proc.stdin.write(final_frame.tobytes())

    cap.release()
    proc.stdin.close()
    proc.wait()
    print(f"[SUCCESS] Created {out_name}: {os.path.getsize(out_path):,} bytes")

def main():
    options = [
        (DEMO_VID, 3.5, 4.0, "Hook-Option-01-Classical-Mudra.mp4", "hook_opt_1_classical_mudra.jpg", False),
        (DEMO_VID, 7.8, 4.0, "Hook-Option-02-Emotional-Sway.mp4", "hook_opt_2_emotional_sway.jpg", False),
        (DEMO_VID, 12.0, 4.0, "Hook-Option-03-Over-Shoulder-Twirl.mp4", "hook_opt_3_over_shoulder.jpg", False),
        (DEMO_VID, 19.2, 4.0, "Hook-Option-04-Bollywood-Welcoming-Sway.mp4", "hook_opt_4_bollywood_welcome.jpg", False),
        (DEMO_VID, 0.0, 3.5, "Hook-Option-05-Original-Turn-Around.mp4", "hook_opt_5_original_ad01.jpg", False),
    ]

    if os.path.exists(CHINESE_VID):
        options.append((CHINESE_VID, 1.0, 4.0, "Hook-Option-06-Red-Silk-Cheongsam.mp4", "hook_opt_6_cheongsam.jpg", True))

    for src, st, dur, name, snap, is_land in options:
        render_hook_video(src, st, dur, name, snap, is_land)

    print("\n=== ALL CLEAN HOOK VIDEOS AND SNAPSHOTS READY ===")

if __name__ == "__main__":
    main()
