import os
import subprocess
import cv2
import numpy as np
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
OUT_9X16_DIR = os.path.join(PROJECT_DIR, "ads-ready", "01-India-INR-Ads")
OUT_4X5_DIR = os.path.join(PROJECT_DIR, "ads-ready", "02-India-INR-Feed-4x5")
SCRATCH_DIR = os.path.join(PROJECT_DIR, "instagram-studio", ".tmp_ad04")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Hook Option 03 (User Approved: Over-the-Shoulder Teasing Twirl)
HOOK_03_PATH = os.path.join(PROJECT_DIR, "instagram-studio", "05-Dancing-Hook-Options", "Hook-Option-03-Over-Shoulder-Twirl.mp4")
REEL_04_RAW = os.path.join(PROJECT_DIR, "instagram-studio", "02-Organic-Reels", "Reel-04-Raw-iPhone-Realism-Secret-Organic.mp4")
AD_01_RAW = os.path.join(PROJECT_DIR, "ads-ready", "01-India-INR-Ads", "Ad-01-Curiosity-Reveal-INR-9x16.mp4")
BG_ASSET = os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "05-blonde-char-emerald-cafe.jpg")

os.makedirs(OUT_9X16_DIR, exist_ok=True)
os.makedirs(OUT_4X5_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

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

FONT_HEAD = get_font("arialbd.ttf", 50)
FONT_BTN = get_font("arialbd.ttf", 34)
FONT_SUB_BOLD = get_font("segoeuib.ttf", 28)
FONT_TAG = get_font("segoeuib.ttf", 22)
FONT_EMOJI_HEAD = get_font("seguiemj.ttf", 48)
FONT_EMOJI_BTN = get_font("seguiemj.ttf", 32)
FONT_EMOJI_SM = get_font("seguiemj.ttf", 24)

def crop_fill(img, target_w, target_h, align_y=0.28):
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
    return ord(ch) > 0x2000 and ch not in "—–•'\"’“”→"

def draw_text_with_emoji(canvas, pos, text, font, emoji_font, fill=(255, 255, 255), shadow=True):
    d = ImageDraw.Draw(canvas)
    x, y = pos
    for ch in text:
        is_em = is_emoji_char(ch)
        f = emoji_font if is_em else font
        if shadow and not is_em:
            d.text((x + 2, y + 3), ch, font=f, fill=(0, 0, 0, 220))
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

def draw_centered_mixed_line(canvas, y, text, font, emoji_font, width=1080, fill=(255, 255, 255), highlight_words=None, highlight_fill=(56, 189, 248), shadow=True):
    d = ImageDraw.Draw(canvas)
    total_w = measure_text_with_emoji(d, text, font, emoji_font)
    x = (width - total_w) / 2
    words = text.split(" ")
    for i, word in enumerate(words):
        token = word + (" " if i < len(words) - 1 else "")
        clean_w = word.strip(".,!?:;\"'()⚡🔥🚀")
        c_fill = highlight_fill if (highlight_words and clean_w in highlight_words) else fill
        draw_text_with_emoji(canvas, (x, y), token, font, emoji_font, fill=c_fill, shadow=shadow)
        x += measure_text_with_emoji(d, token, font, emoji_font)

def create_paid_endcard_image(width, height):
    base_pil = crop_fill(Image.open(BG_ASSET).convert("RGB"), width, height, align_y=0.25).filter(ImageFilter.GaussianBlur(18))
    base_pil = ImageEnhance.Brightness(base_pil).enhance(0.24).convert("RGBA")
    de = ImageDraw.Draw(base_pil, "RGBA")

    is_9x16 = (height > 1500)
    card_y1 = int(height * 0.18) if is_9x16 else int(height * 0.11)
    card_y2 = int(height * 0.86) if is_9x16 else int(height * 0.91)
    card_x1 = 36
    card_x2 = width - 36

    # Floating Card Container
    de.rounded_rectangle((card_x1, card_y1, card_x2, card_y2), radius=36, fill=(10, 14, 26, 250), outline=(139, 92, 246, 255), width=4)

    # 1. Flash Offer Badge
    pill_w = 460
    px1 = (width - pill_w) // 2
    py1 = card_y1 + 24
    de.rounded_rectangle((px1, py1, px1 + pill_w, py1 + 50), radius=25, fill=(16, 185, 129, 255))
    draw_centered_mixed_line(base_pil, py1 + 12, "⚡ 90% OFF FLASH LAUNCH OFFER", FONT_TAG, FONT_EMOJI_SM, width=width, fill=(5, 46, 22), shadow=False)

    # 2. Hero Headline
    f_h1 = get_font("arialbd.ttf", 48 if is_9x16 else 42)
    f_em_h1 = get_font("seguiemj.ttf", 44 if is_9x16 else 38)
    h_y = py1 + 72
    draw_centered_mixed_line(base_pil, h_y, "INSTANT AI INFLUENCER", f_h1, f_em_h1, width=width, fill=(255, 255, 255))
    draw_centered_mixed_line(base_pil, h_y + 54, "PROMPT VAULT & LAUNCH KIT 🧬", f_h1, f_em_h1, width=width, fill=(56, 189, 248))

    # 3. Features checkmarks
    perks = [
        "✓  250+ Character DNA & Face-Lock Prompts",
        "✓  1-Click Face-Lock Mobile Pipeline",
        "✓  Turn 1 Photo into 4K Looping Viral Reels",
        "✓  Bonus: 23 HD Step-by-Step Video Lessons",
        "✓  100% Runs on Phone • Zero PC/GPU Needed"
    ]
    perk_y = h_y + 130
    step_y = 52 if is_9x16 else 44
    for p in perks:
        draw_text_with_emoji(base_pil, (card_x1 + 40, perk_y), p, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(235, 245, 255), shadow=False)
        perk_y += step_y

    # 4. Price Anchor Box (Crisp 'Rs.' typography)
    price_y = perk_y + 14
    pbox_w = width - 110
    pbx1 = (width - pbox_w) // 2
    de.rounded_rectangle((pbx1, price_y, pbx1 + pbox_w, price_y + 70), radius=20, fill=(18, 24, 42, 255), outline=(56, 189, 248, 220), width=2)
    draw_centered_mixed_line(base_pil, price_y + 18, "REGULAR Rs. 1,999   •   TODAY ONLY: Rs. 199", FONT_BTN, FONT_EMOJI_BTN, width=width, fill=(250, 204, 21), shadow=False)

    # 5. Pulsing CTA Button
    btn_y = price_y + 90
    btn_w = width - 90
    bx1 = (width - btn_w) // 2
    de.rounded_rectangle((bx1, btn_y, bx1 + btn_w, btn_y + 90), radius=28, fill=(124, 58, 237, 255), outline=(216, 180, 254, 255), width=3)
    draw_centered_mixed_line(base_pil, btn_y + 24, "⚡ TAP 'LEARN MORE' — ONLY Rs. 199 →", FONT_BTN, FONT_EMOJI_BTN, width=width, fill=(255, 255, 255), shadow=False)

    # 6. Bottom trust caption
    draw_centered_mixed_line(base_pil, btn_y + 106, "🔒 Instant Google Drive & Portal Access • 7-Day Guarantee", FONT_TAG, FONT_EMOJI_SM, width=width, fill=(180, 195, 220), shadow=False)

    return base_pil.convert("RGB")

def build_ad(aspect="9x16"):
    is_9x16 = (aspect == "9x16")
    w, h = (1080, 1920) if is_9x16 else (1080, 1350)
    out_dir = OUT_9X16_DIR if is_9x16 else OUT_4X5_DIR
    out_file = os.path.join(out_dir, f"Ad-04-Raw-iPhone-Realism-INR-{aspect}.mp4")

    print(f"\n>>> Assembling Master Creative #04 [{aspect}] ({w}x{h}) with Dancing Hook #03")

    # 1. Save crisp endcard image
    endcard_img = os.path.join(SCRATCH_DIR, f"endcard_{aspect}.png")
    create_paid_endcard_image(w, h).save(endcard_img, quality=98)

    # 2. Extract Hook (0.0s to 4.0s) from Hook-Option-03
    tmp_v_hook = os.path.join(SCRATCH_DIR, f"v_hook_{aspect}.mp4")
    if is_9x16:
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-t", "4.0",
            "-i", HOOK_03_PATH,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", "30", "-an", tmp_v_hook
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # 4x5 uses blurred background padding
        filter_pad = "split[a][b];[a]scale=1080:1350:force_original_aspect_ratio=increase,crop=1080:1350,boxblur=25:5[bg];[b]scale=759:1350[fg];[bg][fg]overlay=(W-w)/2:0"
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-t", "4.0",
            "-i", HOOK_03_PATH,
            "-filter_complex", filter_pad,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", "30", "-an", tmp_v_hook
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Extract Body (4.0s to 22.5s) from Reel 04
    tmp_v_body = os.path.join(SCRATCH_DIR, f"v_body_{aspect}.mp4")
    if is_9x16:
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-ss", "4.0", "-to", "22.5",
            "-i", REEL_04_RAW,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", "30", "-an", tmp_v_body
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        filter_pad = "split[a][b];[a]scale=1080:1350:force_original_aspect_ratio=increase,crop=1080:1350,boxblur=25:5[bg];[b]scale=759:1350[fg];[bg][fg]overlay=(W-w)/2:0"
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-ss", "4.0", "-to", "22.5",
            "-i", REEL_04_RAW,
            "-filter_complex", filter_pad,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", "30", "-an", tmp_v_body
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 4. Extract 7.5s Endcard Video Loop
    tmp_v_end = os.path.join(SCRATCH_DIR, f"v_end_{aspect}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-loop", "1", "-t", "7.5",
        "-i", endcard_img,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", "30", "-an", tmp_v_end
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Concat video parts
    concat_txt = os.path.join(SCRATCH_DIR, f"v_concat_{aspect}.txt")
    with open(concat_txt, "w") as f:
        f.write(f"file '{tmp_v_hook}'\n")
        f.write(f"file '{tmp_v_body}'\n")
        f.write(f"file '{tmp_v_end}'\n")

    tmp_v_full = os.path.join(SCRATCH_DIR, f"v_full_{aspect}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy", tmp_v_full
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 6. Audio Concat (0-22.5s from Reel 04 + 7.5s from Ad 01)
    tmp_a1 = os.path.join(SCRATCH_DIR, f"a1_{aspect}.wav")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-ss", "0.0", "-to", "22.5",
        "-i", REEL_04_RAW,
        "-ar", "44100", "-ac", "2", tmp_a1
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    tmp_a2 = os.path.join(SCRATCH_DIR, f"a2_{aspect}.wav")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-ss", "23.0", "-to", "30.5",
        "-i", AD_01_RAW,
        "-ar", "44100", "-ac", "2", tmp_a2
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    concat_a_txt = os.path.join(SCRATCH_DIR, f"a_concat_{aspect}.txt")
    with open(concat_a_txt, "w") as f:
        f.write(f"file '{tmp_a1}'\n")
        f.write(f"file '{tmp_a2}'\n")

    tmp_a_full = os.path.join(SCRATCH_DIR, f"a_full_{aspect}.m4a")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_a_txt,
        "-c:a", "aac", "-b:a", "192k", tmp_a_full
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 7. Final Mux
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-i", tmp_v_full,
        "-i", tmp_a_full,
        "-c:v", "copy",
        "-c:a", "copy",
        "-movflags", "+faststart",
        "-shortest",
        out_file
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[SUCCESS] Finished Creative #04 [{aspect}]: {out_file} ({os.path.getsize(out_file):,} bytes)")

def main():
    print("=== PRODUCING MASTER CREATIVE #04 (DANCING HOOK #03 + RAW IPHONE REALISM) ===")
    build_ad("9x16")
    build_ad("4x5")
    print("=== ALL MASTER ASSETS GENERATED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
