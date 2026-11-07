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

# Assets
HOOK_03_PATH = os.path.join(PROJECT_DIR, "instagram-studio", "05-Dancing-Hook-Options", "Hook-Option-03-Over-Shoulder-Twirl.mp4")
REEL_04_RAW = os.path.join(PROJECT_DIR, "instagram-studio", "02-Organic-Reels", "Reel-04-Raw-iPhone-Realism-Secret-Organic.mp4")
AD_01_RAW = os.path.join(PROJECT_DIR, "ads-ready", "01-India-INR-Ads", "Ad-01-Curiosity-Reveal-INR-9x16.mp4")

# Character Assets (Saree + Lifestyle)
ASSET_CLOSEUP = os.path.join(PROJECT_DIR, "assets", "insta_profile_saree_square_hd.jpg")
ASSET_SAREE = os.path.join(PROJECT_DIR, "assets", "insta_saree_full_portrait_hd.jpg")
ASSET_CAFE = os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "03-demo-girl-emerald-cafe.jpg")
ASSET_DUBAI = os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "04-demo-girl-dubai-rooftop.jpg")
ASSET_GYM = os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "02-demo-girl-gym-activewear.jpg")
ASSET_HERO = os.path.join(PROJECT_DIR, "assets", "images", "hero_showcase.jpg")
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

def grade_image(img_pil, brightness=0.87, contrast=1.20, color=1.06, sharpness=1.30):
    b = ImageEnhance.Brightness(img_pil).enhance(brightness)
    c = ImageEnhance.Contrast(b).enhance(contrast)
    col = ImageEnhance.Color(c).enhance(color)
    s = ImageEnhance.Sharpness(col).enhance(sharpness)
    return s

def crop_fill(img, target_w, target_h, align_y=0.18):
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

def decorate_ad_frame(pil_img, top_hook, sub_hook, caption, width=1080, height=1920):
    d = ImageDraw.Draw(pil_img, "RGBA")
    is_9x16 = (height > 1500)
    
    f_hook = get_font("arialbd.ttf", 38 if is_9x16 else 32)
    f_sub = get_font("segoeuib.ttf", 38 if is_9x16 else 32)
    f_pill = get_font("segoeuib.ttf", 22 if is_9x16 else 19)

    # 1. Top Hook Pill
    if top_hook:
        y1, y2 = (95, 205) if is_9x16 else (45, 135)
        d.rounded_rectangle((55, y1, width - 55, y2), radius=28, fill=(15, 23, 42, 235), outline=(168, 85, 247, 255), width=3)
        d.text((width // 2, (y1 + y2) // 2), top_hook, font=f_hook, fill=(255, 255, 255, 255), anchor="mm")

    # 2. Sub Hook Pills
    py1, py2 = (222, 286) if is_9x16 else (148, 206)
    d.rounded_rectangle((width - 415, py1, width - 50, py2), radius=20, fill=(14, 17, 30, 245), outline=(168, 85, 247, 220), width=2)
    d.ellipse((width - 392, py1 + 23, width - 374, py1 + 41), fill=(56, 189, 248, 255))
    d.text((width - 362, py1 + 16), "@personalabsacademy", font=f_pill, fill=(240, 248, 255))

    if sub_hook:
        d.rounded_rectangle((50, py1, width - 435, py2), radius=20, fill=(14, 17, 30, 248), outline=(56, 189, 248, 225), width=2)
        d.text(((50 + width - 435) // 2, (py1 + py2) // 2), sub_hook, font=f_pill, fill=(56, 189, 248), anchor="mm")

    # 3. Caption Box (Pure clean typography, zero broken emojis)
    if caption:
        words = caption.split()
        lines, cur = [], ""
        max_line_w = int(width * 0.80)
        for w in words:
            test = (cur + " " + w).strip()
            bb = d.textbbox((0, 0), test, font=f_sub)
            if bb[2] - bb[0] > max_line_w and cur:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur:
            lines.append(cur)
        
        line_h = 52 if is_9x16 else 46
        total_h = len(lines) * line_h + 36
        max_w = max((d.textbbox((0, 0), ln, font=f_sub)[2] for ln in lines), default=400)
        box_w = min(width - 100, max_w + 64)
        x0 = (width - box_w) // 2
        y_center = int(height * 0.83) if is_9x16 else int(height * 0.82)
        y0 = y_center - total_h // 2
        
        d.rounded_rectangle((x0, y0, x0 + box_w, y0 + total_h), radius=24, fill=(12, 16, 28, 235), outline=(56, 189, 248, 180), width=2)
        ty = y0 + 18 + line_h // 2
        for ln in lines:
            d.text((width // 2 + 2, ty + 2), ln, font=f_sub, fill=(0, 0, 0, 220), anchor="mm")
            d.text((width // 2, ty), ln, font=f_sub, fill=(255, 255, 255, 255), anchor="mm")
            ty += line_h

    return pil_img

def apply_subtle_ken_burns(pil_img, prog, mode="zoom_in"):
    w, h = pil_img.size
    if mode == "zoom_in":
        scale = 1.0 + 0.04 * prog
        cx, cy = w * 0.5, h * (0.46 - 0.02 * prog)
    elif mode == "zoom_out":
        scale = 1.04 - 0.04 * prog
        cx, cy = w * 0.5, h * (0.44 + 0.02 * prog)
    else:
        scale = 1.02
        cx, cy = w * (0.48 + 0.03 * prog), h * 0.46
    
    cw, ch = w / scale, h / scale
    x1 = max(0, min(w - cw, cx - cw / 2))
    y1 = max(0, min(h - ch, cy - ch / 2))
    cropped = pil_img.crop((int(x1), int(y1), int(x1 + cw), int(y1 + ch)))
    return cropped.resize((w, h), Image.Resampling.LANCZOS)

def build_hero_consistency_slide(width, height):
    base = crop_fill(Image.open(ASSET_CAFE).convert("RGB"), width, height, align_y=0.20).filter(ImageFilter.GaussianBlur(16))
    base = ImageEnhance.Brightness(base).enhance(0.28).convert("RGBA")
    d = ImageDraw.Draw(base, "RGBA")

    is_9x16 = (height > 1500)
    card_x1, card_x2 = 36, width - 36
    card_y1 = int(height * 0.22) if is_9x16 else int(height * 0.16)
    card_y2 = int(height * 0.86) if is_9x16 else int(height * 0.90)

    d.rounded_rectangle((card_x1, card_y1, card_x2, card_y2), radius=32, fill=(12, 16, 30, 248), outline=(168, 85, 247, 240), width=3)

    # Top Tag
    f_tag = get_font("arialbd.ttf", 26 if is_9x16 else 22)
    d.text((width // 2, card_y1 + 36), "100% FACE-LOCK ACROSS ALL SCENES", font=f_tag, fill=(56, 189, 248), anchor="mm")

    # Center Hero Graphic
    hero_raw = Image.open(ASSET_HERO).convert("RGB")
    hero_w = width - 110
    hero_h = int(hero_w * (hero_raw.height / hero_raw.width))
    hero_resized = hero_raw.resize((hero_w, hero_h), Image.Resampling.LANCZOS)
    hero_y = card_y1 + 75
    base.paste(hero_resized, ((width - hero_w) // 2, hero_y))

    # Bottom Proof Badge
    f_badge = get_font("arialbd.ttf", 32 if is_9x16 else 26)
    f_sub_badge = get_font("segoeuib.ttf", 24 if is_9x16 else 20)
    b_box_y = hero_y + hero_h + 24
    d.rounded_rectangle((card_x1 + 30, b_box_y, card_x2 - 30, b_box_y + 115), radius=20, fill=(20, 26, 48, 255), outline=(56, 189, 248, 180), width=2)
    d.text((width // 2, b_box_y + 36), "23 HD STEP-BY-STEP VIDEO LESSONS", font=f_badge, fill=(255, 255, 255), anchor="mm")
    d.text((width // 2, b_box_y + 78), "[+] 100% Face-Lock  [+] 7-Day Guarantee  [+] Zero PC Needed", font=f_sub_badge, fill=(56, 189, 248), anchor="mm")

    return base.convert("RGB")

def render_body_video(out_path, width, height, fps=30):
    total_sec = 18.5  # 4.0s to 22.5s
    total_frames = int(round(total_sec * fps))

    # 1. Graded Saree Closeup (Rich contrast, warm tone, non-blown highlights)
    im_close_raw = Image.open(ASSET_CLOSEUP).convert("RGB")
    img_closeup = crop_fill(grade_image(im_close_raw, 0.86, 1.20, 1.06, 1.35), width, height, align_y=0.14)

    # 2. Graded Full Saree Portrait (Deep crimson silk, balanced exposure)
    im_saree_raw = Image.open(ASSET_SAREE).convert("RGB")
    img_saree = crop_fill(grade_image(im_saree_raw, 0.87, 1.22, 1.08, 1.30), width, height, align_y=0.12)

    # 3. Emerald Cafe Portrait (Outdoor natural daylight)
    img_cafe = crop_fill(Image.open(ASSET_CAFE).convert("RGB"), width, height, align_y=0.22)

    # 4. Dubai Rooftop Evening (Twilight skyline contrast)
    img_dubai = crop_fill(Image.open(ASSET_DUBAI).convert("RGB"), width, height, align_y=0.22)

    # 5. Gym Activewear (iPhone mirror selfie)
    img_gym = crop_fill(Image.open(ASSET_GYM).convert("RGB"), width, height, align_y=0.22)

    # 6. Hero 3-Persona Consistency Proof
    img_hero = build_hero_consistency_slide(width, height)

    # Sequence of 6 Shots over 18.5s:
    # Shot 1: Saree Closeup (0.0 to 2.5s | 2.5s)
    # Shot 2: Full Saree Portrait (2.5 to 5.0s | 2.5s)
    # Shot 3: Emerald Cafe (5.0 to 8.5s | 3.5s)
    # Shot 4: Dubai Rooftop (8.5 to 12.0s | 3.5s)
    # Shot 5: Gym Activewear (12.0 to 15.0s | 3.0s)
    # Shot 6: 100% Face Consistency Proof (15.0 to 18.5s | 3.5s)
    shots = [
        (0.0, 2.5, img_closeup, "zoom_in", "...immediately scream 'FAKE PLASTIC'?"),
        (2.5, 5.0, img_saree, "zoom_out", "Beginners type '8K render' which forces fake CGI plastic skin..."),
        (5.0, 8.5, img_cafe, "zoom_in", "Use our Raw Smartphone Optics formula: 24mm lens + natural pores"),
        (8.5, 12.0, img_dubai, "zoom_out", "24mm iPhone lens + natural pores + candid light"),
        (12.0, 15.0, img_gym, "zoom_in", "100% Face Consistency across Sarees, Cafes & Rooftops"),
        (15.0, 18.5, img_hero, "static", "No camera, no studio, and no expensive models.")
    ]

    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{width}x{height}", "-pix_fmt", "bgr24", "-r", str(fps), "-i", "-",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", str(fps), "-an", out_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    top_hook = "WHY 99% OF AI PHOTOS LOOK FAKE (3-WORD FIX)"
    sub_hook = "RAW IPHONE OPTICS • ZERO CGI GLOW"

    for f_idx in range(total_frames):
        t_sec = f_idx / fps
        active_shot = next(s for s in shots if s[0] <= t_sec <= s[1] or s == shots[-1])
        s_start, s_end, base_img, kb_mode, caption = active_shot
        s_dur = max(0.1, s_end - s_start)
        prog = min(1.0, max(0.0, (t_sec - s_start) / s_dur))

        if kb_mode == "static":
            frame_pil = base_img.copy()
        else:
            frame_pil = apply_subtle_ken_burns(base_img, prog, mode=kb_mode)

        decorated = decorate_ad_frame(frame_pil, top_hook, sub_hook, caption, width=width, height=height)
        bgr = cv2.cvtColor(np.array(decorated), cv2.COLOR_RGB2BGR)
        proc.stdin.write(bgr.tobytes())

    proc.stdin.close()
    proc.wait()
    print(f"[OK] Rendered pristine body video (both saree + lifestyle): {out_path} ({os.path.getsize(out_path):,} bytes)")

def build_ad(aspect="9x16"):
    is_9x16 = (aspect == "9x16")
    w, h = (1080, 1920) if is_9x16 else (1080, 1350)
    out_dir = OUT_9X16_DIR if is_9x16 else OUT_4X5_DIR
    out_file = os.path.join(out_dir, f"Ad-04-Raw-iPhone-Realism-INR-{aspect}.mp4")

    print(f"\n=======================================================")
    print(f">>> Assembling Master Creative #04 [{aspect}] ({w}x{h})")
    print(f"=======================================================")

    # 1. Endcard Image
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
        filter_pad = "split[a][b];[a]scale=1080:1350:force_original_aspect_ratio=increase,crop=1080:1350,boxblur=25:5[bg];[b]scale=759:1350[fg];[bg][fg]overlay=(W-w)/2:0"
        subprocess.run([
            FFMPEG_EXE, "-y",
            "-t", "4.0",
            "-i", HOOK_03_PATH,
            "-filter_complex", filter_pad,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", "30", "-an", tmp_v_hook
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Render Pristine Body (4.0s to 22.5s = 18.5s)
    tmp_v_body = os.path.join(SCRATCH_DIR, f"v_body_pristine_{aspect}.mp4")
    render_body_video(tmp_v_body, w, h, fps=30)

    # 4. Endcard Video Loop (7.5s)
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
    print("=== BUILDING MASTER CREATIVE #04 (DANCING HOOK #03 + BOTH SAREE & LIFESTYLE REALISM) ===")
    build_ad("9x16")
    build_ad("4x5")
    print("=== ALL MASTER ASSETS GENERATED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
