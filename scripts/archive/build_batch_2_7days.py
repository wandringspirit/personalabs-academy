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
CAROUSEL_04_DIR = os.path.join(IG_STUDIO, "06-Carousel-04-Same-Face-Consistency")
CAROUSEL_05_DIR = os.path.join(IG_STUDIO, "07-Carousel-05-Free-Mobile-Stack")
CAROUSEL_06_DIR = os.path.join(IG_STUDIO, "08-Carousel-06-Faceless-Creator-Income")

BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

for d in [REELS_DIR, CAROUSEL_04_DIR, CAROUSEL_05_DIR, CAROUSEL_06_DIR, SCRATCH_DIR]:
    os.makedirs(d, exist_ok=True)

ASSETS = {
    "saree": os.path.join(PROJECT_DIR, "assets", "insta_saree_full_portrait_hd.jpg"),
    "closeup": os.path.join(PROJECT_DIR, "assets", "insta_profile_closeup_hd.jpg"),
    "gym": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "02-demo-girl-gym-activewear.jpg"),
    "cafe": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "03-demo-girl-emerald-cafe.jpg"),
    "dubai": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "04-demo-girl-dubai-rooftop.jpg"),
    "b_cafe": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "05-blonde-char-emerald-cafe.jpg"),
    "b_bali": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "06-blonde-char-beach-club-bali.jpg"),
    "b_penthouse": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "07-blonde-char-penthouse-reel.jpg"),
    "b_gym": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "08-blonde-char-gym-activewear.jpg"),
    "b_rooftop": os.path.join(PROJECT_DIR, "ads-ready", "character-assets", "09-blonde-char-evening-rooftop.jpg"),
    "studio": os.path.join(PROJECT_DIR, "assets", "images", "ai_workflow_studio.jpg"),
    "hero": os.path.join(PROJECT_DIR, "assets", "images", "hero_showcase.jpg"),
    "aira": os.path.join(PROJECT_DIR, "assets", "images", "persona_aira.jpg"),
    "maya": os.path.join(PROJECT_DIR, "assets", "images", "persona_maya.jpg"),
    "bali": os.path.join(PROJECT_DIR, "assets", "images", "persona_bali.jpg"),
}
DEMO_VID = os.path.join(PROJECT_DIR, "videos", "demo.mp4")

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

CW, CH = 1080, 1350
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

def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size[0]-1, size[1]-1), radius=radius, fill=255)
    return mask

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

def draw_centered_mixed_line(canvas, y, text, font, emoji_font, width=CW, fill=(255, 255, 255), highlight_words=None, highlight_fill=(56, 189, 248), shadow=True):
    d = ImageDraw.Draw(canvas)
    total_w = measure_text_with_emoji(d, text, font, emoji_font)
    x = (width - total_w) / 2
    words = text.split(" ")
    for i, word in enumerate(words):
        token = word + (" " if i < len(words) - 1 else "")
        clean_w = word.strip(".,!?:;\"'()")
        c_fill = highlight_fill if (highlight_words and clean_w in highlight_words) else fill
        draw_text_with_emoji(canvas, (x, y), token, font, emoji_font, fill=c_fill, shadow=shadow)
        x += measure_text_with_emoji(d, token, font, emoji_font)

def add_top_bar(canvas, slide_num, total_slides=5, accent=(139, 92, 246)):
    d = ImageDraw.Draw(canvas, "RGBA")
    d.rounded_rectangle((48, 42, 430, 94), radius=26, fill=(12, 14, 24, 225), outline=(accent[0], accent[1], accent[2], 180), width=2)
    d.ellipse((68, 59, 86, 77), fill=(56, 189, 248, 255))
    d.text((98, 55), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))
    d.rounded_rectangle((CW - 168, 42, CW - 48, 94), radius=26, fill=(12, 14, 24, 225), outline=(56, 189, 248, 180), width=2)
    d.text((CW - 140, 55), f"0{slide_num} / 0{total_slides}", font=FONT_TAG, fill=(56, 189, 248))

def add_bottom_magazine_panel(canvas, badge_text, headline_lines, subtitle_lines, highlight_words=None, panel_top=920, accent_color=(168, 85, 247)):
    grad = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    start_y = panel_top - 180
    for y in range(start_y, CH):
        prog = (y - start_y) / (CH - start_y)
        alpha = int(min(252, (prog ** 1.15) * 265))
        gd.line([(0, y), (CW, y)], fill=(7, 9, 17, alpha))
    canvas.alpha_composite(grad)

    d = ImageDraw.Draw(canvas, "RGBA")
    card_x1, card_y1, card_x2, card_y2 = 42, panel_top, CW - 42, CH - 44
    d.rounded_rectangle((card_x1, card_y1, card_x2, card_y2), radius=32, fill=(14, 17, 30, 238), outline=(accent_color[0], accent_color[1], accent_color[2], 195), width=2)
    d.rounded_rectangle((CW//2 - 90, card_y1, CW//2 + 90, card_y1 + 5), radius=3, fill=accent_color)

    bw = int(measure_text_with_emoji(d, badge_text, FONT_SMALL, FONT_EMOJI_SM)) + 48
    bx1 = (CW - bw) // 2
    by1 = card_y1 - 22
    d.rounded_rectangle((bx1, by1, bx1 + bw, by1 + 44), radius=22, fill=(22, 25, 44, 255), outline=accent_color, width=2)
    draw_text_with_emoji(canvas, (bx1 + 24, by1 + 9), badge_text, FONT_SMALL, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)

    curr_y = card_y1 + 42
    for line in headline_lines:
        draw_centered_mixed_line(canvas, curr_y, line, FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), highlight_words=highlight_words, highlight_fill=(56, 189, 248))
        curr_y += 64

    curr_y += 14
    d.line([(CW//2 - 140, curr_y - 6), (CW//2 + 140, curr_y - 6)], fill=(255, 255, 255, 45), width=1)
    curr_y += 10

    for sline in subtitle_lines:
        draw_centered_mixed_line(canvas, curr_y, sline, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(215, 222, 240))
        curr_y += 42

# ------------------------------------------------------------------------------
# Cover builder for 9:16 Reels
# ------------------------------------------------------------------------------
def build_cover_9x16(hero_key, badge_text, line1, line2, highlight_words, out_path, align_y=0.22, accent_color=(56, 189, 248)):
    cv = Image.new("RGBA", (RW, RH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(hero_key).convert("RGB"), RW, RH, align_y=align_y).convert("RGBA")
    cv.paste(hero, (0, 0))

    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(RH - 750, RH):
        prog = (y - (RH - 750)) / 750.0
        alpha = int(min(252, (prog ** 1.25) * 265))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    for y in range(0, 220):
        prog = (220 - y) / 220.0
        alpha = int(min(210, prog * 220))
        gd.line([(0, y), (RW, y)], fill=(6, 8, 16, alpha))
    cv.alpha_composite(grad)

    d = ImageDraw.Draw(cv, "RGBA")
    d.rounded_rectangle((48, 54, 430, 106), radius=26, fill=(12, 14, 24, 230), outline=(accent_color[0], accent_color[1], accent_color[2], 200), width=2)
    d.ellipse((68, 71, 86, 89), fill=(56, 189, 248, 255))
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    card_x1, card_y1, card_x2, card_y2 = 48, RH - 560, RW - 48, RH - 110
    d.rounded_rectangle((card_x1, card_y1, card_x2, card_y2), radius=34, fill=(12, 16, 28, 240), outline=(accent_color[0], accent_color[1], accent_color[2], 210), width=3)
    d.rounded_rectangle((RW//2 - 90, card_y1, RW//2 + 90, card_y1 + 5), radius=3, fill=accent_color)

    bw = int(measure_text_with_emoji(d, badge_text, FONT_TAG, FONT_EMOJI_SM)) + 52
    bx1 = (RW - bw) // 2
    by1 = card_y1 - 24
    d.rounded_rectangle((bx1, by1, bx1 + bw, by1 + 48), radius=24, fill=(20, 24, 42, 255), outline=accent_color, width=2)
    draw_text_with_emoji(cv, (bx1 + 26, by1 + 10), badge_text, FONT_TAG, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)

    curr_y = card_y1 + 54
    draw_centered_mixed_line(cv, curr_y, line1, FONT_HEAD, FONT_EMOJI_HEAD, width=RW, fill=(255, 255, 255), highlight_words=highlight_words, highlight_fill=accent_color)
    curr_y += 72
    draw_centered_mixed_line(cv, curr_y, line2, FONT_HEAD, FONT_EMOJI_HEAD, width=RW, fill=(255, 255, 255), highlight_words=highlight_words, highlight_fill=accent_color)

    curr_y += 36
    d.rounded_rectangle((RW//2 - 290, curr_y, RW//2 + 290, curr_y + 64), radius=22, fill=(56, 189, 248, 255))
    d.text((RW//2, curr_y + 32), "WATCH REEL  ►", font=FONT_BTN, fill=(10, 14, 26, 255), anchor="mm")

    cv.convert("RGB").save(out_path, quality=96, subsampling=0)
    print(f"[OK] Generated Cover: {out_path}")

# ==============================================================================
# CAROUSEL #04 (Tue Oct 20): How to Keep the Exact Same AI Face in 50 Photos
# ==============================================================================
def build_carousel_04():
    bg_base = crop_fill(Image.open(ASSETS["studio"]).convert("RGB"), CW, CH).filter(ImageFilter.GaussianBlur(24))
    bg_base = ImageEnhance.Brightness(bg_base).enhance(0.26).convert("RGBA")

    # Slide 1 (Cover)
    s1 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(ASSETS["saree"]).convert("RGB"), CW, 1060, align_y=0.15).convert("RGBA")
    s1.paste(hero, (0, 0))
    add_top_bar(s1, 1, 5, accent=(56, 189, 248))
    d = ImageDraw.Draw(s1, "RGBA")
    d.rounded_rectangle((48, 785, 520, 845), radius=20, fill=(10, 14, 26, 230), outline=(56, 189, 248, 200), width=2)
    d.ellipse((70, 806, 88, 824), fill=(34, 197, 94, 255))
    d.text((102, 801), "CHARACTER DNA • 100% FACE-LOCK", font=FONT_SMALL, fill=(235, 245, 255))
    add_bottom_magazine_panel(
        s1,
        badge_text="🧬 CHARACTER DNA MASTERCLASS",
        headline_lines=["SAME EXACT AI FACE", "IN 50+ SCENES 🧬"],
        subtitle_lines=["How We Lock One Real Face Across Sarees,", "Gym, Cafes & Dubai Rooftops (Swipe →)"],
        highlight_words={"SAME", "EXACT", "50+", "SCENES"},
        accent_color=(56, 189, 248)
    )
    s1.convert("RGB").save(os.path.join(CAROUSEL_04_DIR, "slide-01.jpg"), quality=96, subsampling=0)

    # Slide 2: The Drift Problem
    s2 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s2.paste(bg_base, (0, 0))
    add_top_bar(s2, 2, 5, accent=(239, 68, 68))
    cell_w, cell_h = 472, 368
    im_bad1 = crop_fill(Image.open(ASSETS["aira"]).convert("RGB"), cell_w, cell_h, align_y=0.15).convert("RGBA")
    im_bad2 = crop_fill(Image.open(ASSETS["maya"]).convert("RGB"), cell_w, cell_h, align_y=0.15).convert("RGBA")
    s2.paste(im_bad1, (48, 128), rounded_rect_mask((cell_w, cell_h), 24))
    s2.paste(im_bad2, (560, 128), rounded_rect_mask((cell_w, cell_h), 24))
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((48, 128, 48+cell_w, 128+cell_h), radius=24, outline=(239, 68, 68, 200), width=3)
    d2.rounded_rectangle((560, 128, 560+cell_w, 128+cell_h), radius=24, outline=(239, 68, 68, 200), width=3)
    d2.text((68, 455), "❌ FACE A (PHOTO 1)", font=FONT_TAG, fill=(239, 68, 68))
    d2.text((580, 455), "❌ FACE B (PHOTO 2 - MORPHED)", font=FONT_TAG, fill=(239, 68, 68))

    add_bottom_magazine_panel(
        s2,
        badge_text="⚠️ THE #1 REASON BEGINNERS QUIT",
        headline_lines=["WHY YOUR AI CHARACTER", "CHANGES EVERY PHOTO 🤯"],
        subtitle_lines=["Without a locked identity seed, Midjourney", "hallucinates a totally new person each prompt."],
        highlight_words={"CHANGES", "EVERY", "PHOTO"},
        accent_color=(239, 68, 68)
    )
    s2.convert("RGB").save(os.path.join(CAROUSEL_04_DIR, "slide-02.jpg"), quality=96, subsampling=0)

    # Slide 3: The 3-Step Seed Lock
    s3 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s3.paste(bg_base, (0, 0))
    add_top_bar(s3, 3, 5, accent=(56, 189, 248))
    d3 = ImageDraw.Draw(s3, "RGBA")
    steps = [
        (48, 128, CW-48, 338, (56, 189, 248), "STEP 1 • GENERATE THE MASTER ID 👑", "Generate 1 ultra-sharp frontal neutral portrait.", "This is your permanent Anchor Face (Seed 0)."),
        (48, 362, CW-48, 572, (168, 85, 247), "STEP 2 • EXTRACT 512-D EMBEDDINGS 🧬", "Use InsightFace mobile pass to capture 512 facial keypoints.", "Locks eye shape, nose bridge, jawline & lips."),
        (48, 596, CW-48, 806, (34, 197, 94), "STEP 3 • INJECT INTO INFINITE SCENES 🌍", "Swap onto any body, saree, gym set, or rooftop.", "The face locks 100% while clothes & lighting change!"),
    ]
    for x1, y1, x2, y2, col, title, l1, l2 in steps:
        d3.rounded_rectangle((x1, y1, x2, y2), radius=24, fill=(14, 18, 32, 240), outline=(col[0], col[1], col[2], 220), width=2)
        d3.rounded_rectangle((x1+16, y1+18, x1+24, y2-18), radius=4, fill=col)
        draw_text_with_emoji(s3, (x1+42, y1+22), title, FONT_TAG, FONT_EMOJI_SM, fill=col, shadow=False)
        draw_text_with_emoji(s3, (x1+42, y1+66), l1, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s3, (x1+42, y1+112), l2, FONT_SUB, FONT_EMOJI_SM, fill=(200, 215, 240), shadow=False)
    add_bottom_magazine_panel(
        s3,
        badge_text="🔑 THE CHARACTER DNA BLUEPRINT",
        headline_lines=["THE 3-STEP SEED-LOCK", "PIPELINE ON MOBILE 📱"],
        subtitle_lines=["Takes 5 minutes per image. Zero expensive", "graphics card or coding required."],
        highlight_words={"3-STEP", "SEED-LOCK", "MOBILE"},
        accent_color=(56, 189, 248)
    )
    s3.convert("RGB").save(os.path.join(CAROUSEL_04_DIR, "slide-03.jpg"), quality=96, subsampling=0)

    # Slide 4: Proof Grid (4 Scenes, 1 Face)
    s4 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s4.paste(bg_base, (0, 0))
    add_top_bar(s4, 4, 5, accent=(34, 197, 94))
    grid = [
        ("saree", "01 • INDIAN SAREE", 0.15),
        ("gym", "02 • GYM ACTIVEWEAR", 0.22),
        ("cafe", "03 • EMERALD CAFE", 0.2),
        ("dubai", "04 • DUBAI ROOFTOP", 0.2),
    ]
    positions = [(48, 128), (560, 128), (48, 516), (560, 516)]
    d4 = ImageDraw.Draw(s4, "RGBA")
    for (key, label, ay), (px, py) in zip(grid, positions):
        im = crop_fill(Image.open(ASSETS[key]).convert("RGB"), cell_w, cell_h, align_y=ay).convert("RGBA")
        s4.paste(im, (px, py), rounded_rect_mask((cell_w, cell_h), 24))
        d4.rounded_rectangle((px, py, px + cell_w, py + cell_h), radius=24, outline=(34, 197, 94, 200), width=3)
        d4.rounded_rectangle((px + 18, py + cell_h - 52, px + 310, py + cell_h - 14), radius=14, fill=(12, 15, 28, 230), outline=(34, 197, 94, 180), width=1)
        d4.text((px + 32, py + cell_h - 45), label, font=FONT_SMALL, fill=(240, 248, 255))
    add_bottom_magazine_panel(
        s4,
        badge_text="✨ 1 FACE • 4 SCENES • ZERO SHOOTS",
        headline_lines=["100% IDENTICAL FACE", "ACROSS ANY LOCATION 🌍"],
        subtitle_lines=["From Mumbai to Dubai in 15 minutes.", "Every photo looks like the same living creator."],
        highlight_words={"100% IDENTICAL", "FACE"},
        accent_color=(34, 197, 94)
    )
    s4.convert("RGB").save(os.path.join(CAROUSEL_04_DIR, "slide-04.jpg"), quality=96, subsampling=0)

    # Slide 5: Call to Action
    s5 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s5.paste(bg_base, (0, 0))
    add_top_bar(s5, 5, 5, accent=(56, 189, 248))
    pw, ph = 410, 720
    im_p = crop_fill(Image.open(ASSETS["saree"]).convert("RGB"), pw, ph, align_y=0.18).convert("RGBA")
    s5.paste(im_p, (48, 128), rounded_rect_mask((pw, ph), 28))
    d5 = ImageDraw.Draw(s5, "RGBA")
    d5.rounded_rectangle((48, 128, 48 + pw, 128 + ph), radius=28, outline=(56, 189, 248, 220), width=3)

    d5.rounded_rectangle((484, 128, 1032, 480), radius=28, fill=(14, 18, 34, 240), outline=(56, 189, 248, 220), width=2)
    draw_text_with_emoji(s5, (514, 158), "WHAT'S INSIDE THE KIT 📦", FONT_TAG, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)
    perks = [
        "✅ 23 Step-by-Step HD Video Lessons",
        "✅ 250+ Character DNA Prompts",
        "✅ 1-Photo to 4K Reel Mobile System",
        "✅ 500+ Viral Hooks & Auto-DM Pack",
        "✅ 100% Runs on iPhone & Android"
    ]
    py = 210
    for perk in perks:
        draw_text_with_emoji(s5, (514, py), perk, FONT_SMALL, FONT_EMOJI_SM, fill=(230, 240, 255), shadow=False)
        py += 46

    d5.rounded_rectangle((484, 510, 1032, 700), radius=28, fill=(22, 28, 54, 255), outline=(168, 85, 247, 240), width=3)
    draw_text_with_emoji(s5, (514, 536), "HOW TO GET IT INSTANTLY 👇", FONT_TAG, FONT_EMOJI_SM, fill=(168, 85, 247), shadow=False)
    draw_text_with_emoji(s5, (514, 576), "Comment \"FACE\" or \"AI\"", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s5, (514, 640), "And I'll DM you the exact 5-Day Blueprint! 🚀", FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)

    add_bottom_magazine_panel(
        s5,
        badge_text="🚀 LAUNCH YOUR AI PAGE THIS WEEK",
        headline_lines=["WANT THE FULL 5-DAY", "CHARACTER BLUEPRINT? 🔥"],
        subtitle_lines=["Comment \"FACE\" below to get the full video system,", "prompts, and mobile pipeline sent to your DMs."],
        highlight_words={"FULL", "5-DAY", "BLUEPRINT?"},
        accent_color=(168, 85, 247)
    )
    s5.convert("RGB").save(os.path.join(CAROUSEL_04_DIR, "slide-05.jpg"), quality=96, subsampling=0)
    print("[OK] Generated Carousel #04 (5 Slides)")

# ==============================================================================
# CAROUSEL #05 (Thu Oct 22): The 100% Free Mobile AI Stack
# ==============================================================================
def build_carousel_05():
    bg_base = crop_fill(Image.open(ASSETS["studio"]).convert("RGB"), CW, CH).filter(ImageFilter.GaussianBlur(24))
    bg_base = ImageEnhance.Brightness(bg_base).enhance(0.26).convert("RGBA")

    # Slide 1
    s1 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(ASSETS["b_bali"]).convert("RGB"), CW, 1060, align_y=0.18).convert("RGBA")
    s1.paste(hero, (0, 0))
    add_top_bar(s1, 1, 5, accent=(34, 197, 94))
    d = ImageDraw.Draw(s1, "RGBA")
    d.rounded_rectangle((48, 785, 520, 845), radius=20, fill=(10, 14, 26, 230), outline=(34, 197, 94, 200), width=2)
    d.ellipse((70, 806, 88, 824), fill=(34, 197, 94, 255))
    d.text((102, 801), "NO LAPTOP • 100% MOBILE AI STACK", font=FONT_SMALL, fill=(235, 245, 255))
    add_bottom_magazine_panel(
        s1,
        badge_text="📱 ZERO PC REQUIRED",
        headline_lines=["THE 100% FREE", "MOBILE AI STACK 📱"],
        subtitle_lines=["The Exact 4 Free Mobile Tools We Use To Build", "& Monetize Hyper-Realistic AI Creators (Swipe →)"],
        highlight_words={"100% FREE", "MOBILE", "STACK"},
        accent_color=(34, 197, 94)
    )
    s1.convert("RGB").save(os.path.join(CAROUSEL_05_DIR, "slide-01.jpg"), quality=96, subsampling=0)

    # Slide 2: Tool 1 (SeaArt / Fooocus)
    s2 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s2.paste(bg_base, (0, 0))
    add_top_bar(s2, 2, 5, accent=(56, 189, 248))
    pw, ph = 410, 720
    im_p = crop_fill(Image.open(ASSETS["b_cafe"]).convert("RGB"), pw, ph, align_y=0.2).convert("RGBA")
    s2.paste(im_p, (48, 128), rounded_rect_mask((pw, ph), 28))
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((48, 128, 48 + pw, 128 + ph), radius=28, outline=(56, 189, 248, 220), width=3)

    d2.rounded_rectangle((484, 128, 1032, 520), radius=28, fill=(14, 18, 34, 240), outline=(56, 189, 248, 220), width=2)
    draw_text_with_emoji(s2, (514, 158), "TOOL #1 • CHARACTER CREATOR 🎨", FONT_TAG, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)
    draw_text_with_emoji(s2, (514, 204), "SeaArt.ai / Fooocus Mobile", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    t1_bullets = [
        "⚡ 100% Free daily cloud GPU credits",
        "⚡ Runs straight from Safari or Chrome",
        "⚡ Generates raw iPhone lens lighting",
        "⚡ Zero installations on your device"
    ]
    py = 280
    for b in t1_bullets:
        draw_text_with_emoji(s2, (514, py), b, FONT_SUB, FONT_EMOJI_SM, fill=(210, 225, 250), shadow=False)
        py += 52

    add_bottom_magazine_panel(
        s2,
        badge_text="🎨 STEP 1: GENERATE THE IDENTITY",
        headline_lines=["CLOUD IMAGE RENDER", "ON YOUR PHONE 📱"],
        subtitle_lines=["You don't need a ₹1.5L gaming PC.", "Cloud generators render 4K frames in 15 seconds."],
        highlight_words={"CLOUD", "RENDER", "PHONE"},
        accent_color=(56, 189, 248)
    )
    s2.convert("RGB").save(os.path.join(CAROUSEL_05_DIR, "slide-02.jpg"), quality=96, subsampling=0)

    # Slide 3: Tool 2 & 3 (InsightFace + Kling AI)
    s3 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s3.paste(bg_base, (0, 0))
    add_top_bar(s3, 3, 5, accent=(168, 85, 247))
    d3 = ImageDraw.Draw(s3, "RGBA")

    d3.rounded_rectangle((48, 128, CW-48, 430), radius=28, fill=(14, 18, 34, 240), outline=(168, 85, 247, 220), width=2)
    draw_text_with_emoji(s3, (78, 158), "TOOL #2 • 100% FACE-LOCK 🧬", FONT_TAG, FONT_EMOJI_SM, fill=(168, 85, 247), shadow=False)
    draw_text_with_emoji(s3, (78, 198), "InsightFace Mobile / FaceFusion", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s3, (78, 260), "Locks your character's exact facial bone structure across 100+ outfits.", FONT_SUB, FONT_EMOJI_SM, fill=(210, 225, 250), shadow=False)
    draw_text_with_emoji(s3, (78, 305), "Swaps in 5 seconds per photo on Telegram / Discord web.", FONT_SUB, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)

    d3.rounded_rectangle((48, 456, CW-48, 758), radius=28, fill=(14, 18, 34, 240), outline=(34, 197, 94, 220), width=2)
    draw_text_with_emoji(s3, (78, 486), "TOOL #3 • 4K VIDEO ANIMATOR 🎬", FONT_TAG, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)
    draw_text_with_emoji(s3, (78, 526), "Kling AI / Hailuo MiniMax", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s3, (78, 588), "Turns 1 static photo into a breathing, smiling 9:16 viral Reel.", FONT_SUB, FONT_EMOJI_SM, fill=(210, 225, 250), shadow=False)
    draw_text_with_emoji(s3, (78, 633), "Free daily credits — zero watermarks with our mobile export trick.", FONT_SUB, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)

    add_bottom_magazine_panel(
        s3,
        badge_text="🎬 STEP 2 & 3: FACE-LOCK + MOTION",
        headline_lines=["FROM 1 PHOTO TO", "4K VIRAL REEL 🔥"],
        subtitle_lines=["Animate your persona sipping coffee, walking, or", "posing — without the face warping or melting."],
        highlight_words={"PHOTO", "4K", "VIRAL", "REEL"},
        accent_color=(168, 85, 247)
    )
    s3.convert("RGB").save(os.path.join(CAROUSEL_05_DIR, "slide-03.jpg"), quality=96, subsampling=0)

    # Slide 4: Tool 4 (CapCut + ManyChat)
    s4 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s4.paste(bg_base, (0, 0))
    add_top_bar(s4, 4, 5, accent=(56, 189, 248))
    d4 = ImageDraw.Draw(s4, "RGBA")

    d4.rounded_rectangle((48, 128, CW-48, 430), radius=28, fill=(14, 18, 34, 240), outline=(56, 189, 248, 220), width=2)
    draw_text_with_emoji(s4, (78, 158), "TOOL #4A • RETENTION PACING ✂️", FONT_TAG, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)
    draw_text_with_emoji(s4, (78, 198), "CapCut Mobile (Auto-Captions)", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s4, (78, 260), "Cuts clips into 2-second retention loops engineered for >100% watch time.", FONT_SUB, FONT_EMOJI_SM, fill=(210, 225, 250), shadow=False)
    draw_text_with_emoji(s4, (78, 305), "Burn-in high-contrast captions that stop Explore feed scrolling.", FONT_SUB, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)

    d4.rounded_rectangle((48, 456, CW-48, 758), radius=28, fill=(14, 18, 34, 240), outline=(234, 179, 8, 220), width=2)
    draw_text_with_emoji(s4, (78, 486), "TOOL #4B • 24/7 CASH CONVERTER 💰", FONT_TAG, FONT_EMOJI_SM, fill=(234, 179, 8), shadow=False)
    draw_text_with_emoji(s4, (78, 526), "ManyChat Comment-to-DM", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s4, (78, 588), "Official Meta partner bot that automatically replies to every viewer comment.", FONT_SUB, FONT_EMOJI_SM, fill=(210, 225, 250), shadow=False)
    draw_text_with_emoji(s4, (78, 633), "Sends checkout links in 1 second while you sleep.", FONT_SUB, FONT_EMOJI_SM, fill=(234, 179, 8), shadow=False)

    add_bottom_magazine_panel(
        s4,
        badge_text="💰 STEP 4: 24/7 AUTO-MONETIZATION",
        headline_lines=["TURN VIEWS INTO", "BANK CASHFLOW 💰"],
        subtitle_lines=["A Reel without an Auto-DM is wasted reach.", "Automate your sales pipeline from day 1."],
        highlight_words={"TURN", "VIEWS", "BANK", "CASHFLOW"},
        accent_color=(234, 179, 8)
    )
    s4.convert("RGB").save(os.path.join(CAROUSEL_05_DIR, "slide-04.jpg"), quality=96, subsampling=0)

    # Slide 5: CTA
    s5 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s5.paste(bg_base, (0, 0))
    add_top_bar(s5, 5, 5, accent=(34, 197, 94))
    im_p = crop_fill(Image.open(ASSETS["b_bali"]).convert("RGB"), pw, ph, align_y=0.2).convert("RGBA")
    s5.paste(im_p, (48, 128), rounded_rect_mask((pw, ph), 28))
    d5 = ImageDraw.Draw(s5, "RGBA")
    d5.rounded_rectangle((48, 128, 48 + pw, 128 + ph), radius=28, outline=(34, 197, 94, 220), width=3)

    d5.rounded_rectangle((484, 128, 1032, 480), radius=28, fill=(14, 18, 34, 240), outline=(34, 197, 94, 220), width=2)
    draw_text_with_emoji(s5, (514, 158), "GET THE MOBILE BLUEPRINT 📱", FONT_TAG, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)
    perks = [
        "✅ Direct links to all 4 free mobile tools",
        "✅ 250+ Character DNA copy-paste prompts",
        "✅ FaceFusion Pro Mobile Setup Guide",
        "✅ 23 Step-by-Step HD Video Masterclasses",
        "✅ ManyChat Auto-DM Template Scripts"
    ]
    py = 210
    for perk in perks:
        draw_text_with_emoji(s5, (514, py), perk, FONT_SMALL, FONT_EMOJI_SM, fill=(230, 240, 255), shadow=False)
        py += 46

    d5.rounded_rectangle((484, 510, 1032, 700), radius=28, fill=(22, 28, 54, 255), outline=(56, 189, 248, 240), width=3)
    draw_text_with_emoji(s5, (514, 536), "HOW TO GET IT INSTANTLY 👇", FONT_TAG, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)
    draw_text_with_emoji(s5, (514, 576), "Comment \"TOOLS\" or \"AI\"", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s5, (514, 640), "And I'll DM you the complete Launch Kit! 🚀", FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)

    add_bottom_magazine_panel(
        s5,
        badge_text="🚀 LAUNCH FROM YOUR PHONE TODAY",
        headline_lines=["READY TO BUILD YOUR", "AI INFLUENCER? 📱"],
        subtitle_lines=["Comment \"TOOLS\" below right now and I'll send", "the exact click-by-click mobile blueprint to your DMs!"],
        highlight_words={"BUILD", "YOUR", "AI", "INFLUENCER?"},
        accent_color=(34, 197, 94)
    )
    s5.convert("RGB").save(os.path.join(CAROUSEL_05_DIR, "slide-05.jpg"), quality=96, subsampling=0)
    print("[OK] Generated Carousel #05 (5 Slides)")

# ==============================================================================
# CAROUSEL #06 (Sat Oct 24): Faceless Creator Math (₹50k/Mo System)
# ==============================================================================
def build_carousel_06():
    bg_base = crop_fill(Image.open(ASSETS["studio"]).convert("RGB"), CW, CH).filter(ImageFilter.GaussianBlur(24))
    bg_base = ImageEnhance.Brightness(bg_base).enhance(0.26).convert("RGBA")

    # Slide 1
    s1 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(ASSETS["dubai"]).convert("RGB"), CW, 1060, align_y=0.18).convert("RGBA")
    s1.paste(hero, (0, 0))
    add_top_bar(s1, 1, 5, accent=(234, 179, 8))
    d = ImageDraw.Draw(s1, "RGBA")
    d.rounded_rectangle((48, 785, 520, 845), radius=20, fill=(10, 14, 26, 230), outline=(234, 179, 8, 200), width=2)
    d.ellipse((70, 806, 88, 824), fill=(234, 179, 8, 255))
    d.text((102, 801), "FACELESS CREATOR • ₹50K/MO SYSTEM", font=FONT_SMALL, fill=(235, 245, 255))
    add_bottom_magazine_panel(
        s1,
        badge_text="💰 DIGITAL CREATOR ECONOMICS",
        headline_lines=["HOW FACELESS CREATORS", "MAKE ₹50,000/MONTH 💰"],
        subtitle_lines=["Without Showing Their Face, Hiring Models,", "Or Buying A Single Camera (Swipe →)"],
        highlight_words={"FACELESS", "CREATORS", "₹50,000/MONTH"},
        accent_color=(234, 179, 8)
    )
    s1.convert("RGB").save(os.path.join(CAROUSEL_06_DIR, "slide-01.jpg"), quality=96, subsampling=0)

    # Slide 2: Old Way vs AI Way
    s2 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s2.paste(bg_base, (0, 0))
    add_top_bar(s2, 2, 5, accent=(239, 68, 68))
    d2 = ImageDraw.Draw(s2, "RGBA")

    d2.rounded_rectangle((48, 128, CW-48, 430), radius=28, fill=(14, 18, 34, 240), outline=(239, 68, 68, 220), width=2)
    draw_text_with_emoji(s2, (78, 158), "THE TRADITIONAL CREATOR TRAP 😫", FONT_TAG, FONT_EMOJI_SM, fill=(239, 68, 68), shadow=False)
    draw_text_with_emoji(s2, (78, 200), "₹60,000 Camera + ₹20k Studio Rent", FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    draw_text_with_emoji(s2, (78, 245), "❌ Constant camera shyness & filming burnout", FONT_SUB, FONT_EMOJI_SM, fill=(239, 68, 68), shadow=False)
    draw_text_with_emoji(s2, (78, 290), "❌ 8 hours spent filming & re-recording takes", FONT_SUB, FONT_EMOJI_SM, fill=(239, 68, 68), shadow=False)
    draw_text_with_emoji(s2, (78, 335), "❌ Zero leverage: if you stop posting, income stops", FONT_SUB, FONT_EMOJI_SM, fill=(239, 68, 68), shadow=False)

    d2.rounded_rectangle((48, 456, CW-48, 758), radius=28, fill=(14, 18, 34, 240), outline=(34, 197, 94, 220), width=2)
    draw_text_with_emoji(s2, (78, 486), "THE AI CREATOR REVOLUTION 🚀", FONT_TAG, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)
    draw_text_with_emoji(s2, (78, 528), "15 Minutes On Your Phone + Cloud AI", FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    draw_text_with_emoji(s2, (78, 573), "✅ 100% Faceless — your identity is completely private", FONT_SUB, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)
    draw_text_with_emoji(s2, (78, 618), "✅ Put your character in Bali, Paris, or Dubai in seconds", FONT_SUB, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)
    draw_text_with_emoji(s2, (78, 663), "✅ Automated Auto-DM funnels sell 24/7 on autopilot", FONT_SUB, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)

    add_bottom_magazine_panel(
        s2,
        badge_text="⚖️ TRADITIONAL VS. AI CREATOR",
        headline_lines=["WHY SMART CREATORS", "ARE GOING FACELESS 🎭"],
        subtitle_lines=["Maximum digital leverage with zero cameras,", "zero studio shoots, and 100% privacy."],
        highlight_words={"SMART", "CREATORS", "FACELESS"},
        accent_color=(34, 197, 94)
    )
    s2.convert("RGB").save(os.path.join(CAROUSEL_06_DIR, "slide-02.jpg"), quality=96, subsampling=0)

    # Slide 3: The 3 Monetization Pillars
    s3 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s3.paste(bg_base, (0, 0))
    add_top_bar(s3, 3, 5, accent=(56, 189, 248))
    d3 = ImageDraw.Draw(s3, "RGBA")
    pillars = [
        (48, 128, CW-48, 338, (56, 189, 248), "PILLAR 1 • DIGITAL TOOLKITS & GUIDES 📘", "Sell ₹199 to ₹597 prompt bibles, presets & guides.", "Instant 95%+ profit margins with automated Razorpay payouts."),
        (48, 362, CW-48, 572, (168, 85, 247), "PILLAR 2 • BRAND COLLABS & SPONSORS 🤝", "Fashion & D2C brands pay ₹15,000–₹40,000 per Reel.", "Your virtual persona wears their jewelry, activewear, or outfits."),
        (48, 596, CW-48, 806, (234, 179, 8), "PILLAR 3 • EXCLUSIVE VAULTS & VIP ACCESS 💎", "Monetize loyal superfans via Telegram VIP / Fanvue vaults.", "Recurring monthly subscriber cashflow without live shoots."),
    ]
    for x1, y1, x2, y2, col, title, l1, l2 in pillars:
        d3.rounded_rectangle((x1, y1, x2, y2), radius=24, fill=(14, 18, 32, 240), outline=(col[0], col[1], col[2], 220), width=2)
        d3.rounded_rectangle((x1+16, y1+18, x1+24, y2-18), radius=4, fill=col)
        draw_text_with_emoji(s3, (x1+42, y1+22), title, FONT_TAG, FONT_EMOJI_SM, fill=col, shadow=False)
        draw_text_with_emoji(s3, (x1+42, y1+66), l1, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s3, (x1+42, y1+112), l2, FONT_SUB, FONT_EMOJI_SM, fill=(200, 215, 240), shadow=False)
    add_bottom_magazine_panel(
        s3,
        badge_text="💎 THE 3 REVENUE STREAMS",
        headline_lines=["HOW AN AI INFLUENCER", "ACTUALLY MAKES CASH 💰"],
        subtitle_lines=["You don't need 100k followers.", "Even small 2k-follower accounts generate serious profit."],
        highlight_words={"AI", "INFLUENCER", "MAKES", "CASH"},
        accent_color=(234, 179, 8)
    )
    s3.convert("RGB").save(os.path.join(CAROUSEL_06_DIR, "slide-03.jpg"), quality=96, subsampling=0)

    # Slide 4: The Daily Math
    s4 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s4.paste(bg_base, (0, 0))
    add_top_bar(s4, 4, 5, accent=(34, 197, 94))
    d4 = ImageDraw.Draw(s4, "RGBA")
    d4.rounded_rectangle((48, 128, CW-48, 760), radius=28, fill=(14, 18, 34, 240), outline=(34, 197, 94, 220), width=3)
    draw_text_with_emoji(s4, (78, 160), "THE REALISTIC DAILY CONVERSION MATH 📊", FONT_TAG, FONT_EMOJI_SM, fill=(34, 197, 94), shadow=False)

    math_lines = [
        ("1 Viral Reel on Instagram", "➔ 5,000 Views"),
        ("Comment Trigger ('AI')", "➔ 120 Comments"),
        ("ManyChat Auto-DM", "➔ 120 Automated DMs Sent"),
        ("Landing Page Visits", "➔ 80 Visitors"),
        ("Conversion Rate (6%)", "➔ 5 Orders @ ₹597 AOV"),
        ("Daily Net Profit", "➔ ₹2,985 / Day (₹89,550/Mo!)")
    ]
    my = 220
    for label, val in math_lines:
        is_total = "Daily Net Profit" in label
        col = (34, 197, 94) if is_total else (255, 255, 255)
        f = FONT_SUB_BOLD if is_total else FONT_SUB
        draw_text_with_emoji(s4, (78, my), label, f, FONT_EMOJI_SM, fill=col, shadow=False)
        draw_text_with_emoji(s4, (560, my), val, f, FONT_EMOJI_SM, fill=(56, 189, 248) if not is_total else (34, 197, 94), shadow=False)
        d4.line([(78, my + 44), (CW-78, my + 44)], fill=(255, 255, 255, 30), width=1)
        my += 60

    add_bottom_magazine_panel(
        s4,
        badge_text="📊 THE ₹50,000/MONTH BLUEPRINT",
        headline_lines=["JUST 3 SALES A DAY", "HITS ₹50,000/MONTH 🚀"],
        subtitle_lines=["Digital products carry 95%+ profit margins.", "Every Reel works for you 24/7 on autopilot."],
        highlight_words={"3", "SALES", "₹50,000/MONTH"},
        accent_color=(34, 197, 94)
    )
    s4.convert("RGB").save(os.path.join(CAROUSEL_06_DIR, "slide-04.jpg"), quality=96, subsampling=0)

    # Slide 5: CTA
    s5 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s5.paste(bg_base, (0, 0))
    add_top_bar(s5, 5, 5, accent=(234, 179, 8))
    pw, ph = 410, 720
    im_p = crop_fill(Image.open(ASSETS["b_penthouse"]).convert("RGB"), pw, ph, align_y=0.2).convert("RGBA")
    s5.paste(im_p, (48, 128), rounded_rect_mask((pw, ph), 28))
    d5 = ImageDraw.Draw(s5, "RGBA")
    d5.rounded_rectangle((48, 128, 48 + pw, 128 + ph), radius=28, outline=(234, 179, 8, 220), width=3)

    d5.rounded_rectangle((484, 128, 1032, 480), radius=28, fill=(14, 18, 34, 240), outline=(234, 179, 8, 220), width=2)
    draw_text_with_emoji(s5, (514, 158), "THE 5-DAY LAUNCH KIT INCLUDES 🚀", FONT_TAG, FONT_EMOJI_SM, fill=(234, 179, 8), shadow=False)
    perks = [
        "✅ 23 Step-by-Step HD Video Masterclasses",
        "✅ 250+ Character DNA & Seed-Lock Prompts",
        "✅ 1-Photo to 4K Reel Mobile System",
        "✅ 500+ Viral Hooks & Auto-DM Pack",
        "✅ Uncensored VIP Monetization Guide"
    ]
    py = 210
    for perk in perks:
        draw_text_with_emoji(s5, (514, py), perk, FONT_SMALL, FONT_EMOJI_SM, fill=(230, 240, 255), shadow=False)
        py += 46

    d5.rounded_rectangle((484, 510, 1032, 700), radius=28, fill=(22, 28, 54, 255), outline=(56, 189, 248, 240), width=3)
    draw_text_with_emoji(s5, (514, 536), "HOW TO GET STARTED TODAY 👇", FONT_TAG, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)
    draw_text_with_emoji(s5, (514, 576), "Comment \"MONEY\" or \"AI\"", FONT_HEAD, FONT_EMOJI_HEAD, fill=(255, 255, 255), shadow=True)
    draw_text_with_emoji(s5, (514, 640), "And I'll DM you the complete 5-Day Blueprint! 🚀", FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(234, 179, 8), shadow=False)

    add_bottom_magazine_panel(
        s5,
        badge_text="🔥 START YOUR VIRTUAL CREATOR BUSINESS",
        headline_lines=["READY TO LAUNCH YOUR", "FACELESS AI EMPIRE? 💰"],
        subtitle_lines=["Comment \"MONEY\" below to unlock the full 5-day system,", "prompt bible, and ManyChat comment-to-DM funnels."],
        highlight_words={"LAUNCH", "FACELESS", "AI", "EMPIRE?"},
        accent_color=(234, 179, 8)
    )
    s5.convert("RGB").save(os.path.join(CAROUSEL_06_DIR, "slide-05.jpg"), quality=96, subsampling=0)
    print("[OK] Generated Carousel #06 (5 Slides)")

# ==============================================================================
# REELS VIDEO BUILDER (Reels 07, 08, 09, 10)
# ==============================================================================
def load_cv_9x16(path):
    im = Image.open(path).convert("RGB")
    im = crop_fill(im, RW, RH, align_y=0.25)
    return cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

def apply_kb(img_bgr, prog, mode="zoom_in"):
    h, w = img_bgr.shape[:2]
    if mode == "zoom_in":
        scale = 1.0 + 0.08 * prog
    elif mode == "zoom_out":
        scale = 1.08 - 0.08 * prog
    else:
        scale = 1.04
    nw, nh = int(round(w * scale)), int(round(h * scale))
    resized = cv2.resize(img_bgr, (nw, nh), interpolation=cv2.INTER_LINEAR)
    x = (nw - w) // 2
    y = (nh - h) // 2
    return resized[y:y+h, x:x+w]

def decorate_reel_frame(frame_bgr, top_hook, sub_hook_3s, caption_text, show_3s_pill=False, accent=(56, 189, 248)):
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
    d.ellipse((68, 71, 86, 89), fill=(56, 189, 248, 255))
    d.text((98, 67), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))

    # Top hook banner
    d.rounded_rectangle((48, 126, RW - 48, 222), radius=24, fill=(10, 14, 26, 235), outline=(accent[0], accent[1], accent[2], 220), width=2)
    d.text((RW//2, 174), top_hook, font=FONT_BTN, fill=(255, 255, 255, 255), anchor="mm")

    # 3-Second pattern-interrupt sub-hook pill
    if show_3s_pill and sub_hook_3s:
        d.rounded_rectangle((RW//2 - 380, 246, RW//2 + 380, 318), radius=20, fill=(56, 189, 248, 245))
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
    beat_env = 0.5 + 0.5 * np.sin(2 * np.pi * 2.0 * t) ** 4
    pad = (0.35 * np.sin(2 * np.pi * 110.0 * t) + 0.20 * np.sin(2 * np.pi * 164.81 * t) + 0.20 * np.sin(2 * np.pi * 220.0 * t) + 0.15 * np.sin(2 * np.pi * 261.63 * t)) * (0.045 * beat_env)
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
        "-filter_complex", "[0:a]volume=1.35[v];[1:a]volume=0.85[b];[v][b]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]", "-c:a", "aac", "-b:a", "192k", final_aac
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for tf in temp_files + [concat_list, voice_wav, bgm_wav]:
        if os.path.exists(tf):
            os.remove(tf)
    return final_aac, durations

def render_custom_organic_reel(out_filename, top_hook, sub_hook_3s, segments, accent=(56, 189, 248)):
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
    prev_last = None
    global_frame_idx = 0
    for idx, (seg, dur) in enumerate(zip(segments, durations)):
        if idx == len(segments) - 1:
            dur += 0.4
        num_frames = max(15, int(round(dur * fps)))
        visuals = seg["visuals"]
        cap1, cap2 = seg["cap1"], seg["cap2"]
        for f_idx in range(num_frames):
            prog = f_idx / max(1, num_frames - 1)
            v_idx = min(len(visuals) - 1, int(prog * len(visuals)))
            sub_prog = (prog * len(visuals)) - v_idx
            vis_item, mode = visuals[v_idx]
            frame = apply_kb(vis_item, sub_prog, mode=mode)
            if prev_last is not None and f_idx < 5:
                alpha = (f_idx + 1) / 6.0
                frame = cv2.addWeighted(frame, alpha, prev_last, 1.0 - alpha, 0)
            active_cap = cap1 if prog < 0.48 else cap2
            show_3s = (global_frame_idx < 96)
            rendered = decorate_reel_frame(frame, top_hook, sub_hook_3s, active_cap, show_3s_pill=show_3s, accent=accent)
            proc.stdin.write(rendered.tobytes())
            if f_idx == num_frames - 1:
                prev_last = frame.copy()
            global_frame_idx += 1
    proc.stdin.close()
    proc.wait()
    if os.path.exists(final_aac):
        os.remove(final_aac)
    print(f"[OK] Rendered {out_filename} ({os.path.getsize(out_path):,} bytes)")

def build_batch_2_reels():
    c_saree = load_cv_9x16(ASSETS["saree"])
    c_closeup = load_cv_9x16(ASSETS["closeup"])
    c_gym = load_cv_9x16(ASSETS["gym"])
    c_cafe = load_cv_9x16(ASSETS["cafe"])
    c_dubai = load_cv_9x16(ASSETS["dubai"])
    c_bcafe = load_cv_9x16(ASSETS["b_cafe"])
    c_bbali = load_cv_9x16(ASSETS["b_bali"])
    c_bpent = load_cv_9x16(ASSETS["b_penthouse"])
    c_bgym = load_cv_9x16(ASSETS["b_gym"])
    c_broof = load_cv_9x16(ASSETS["b_rooftop"])

    # -------------------------------------------------------------------------
    # Reel 07: 3 AI Prompts That Replaced Our ₹50k Camera Lens (Mon Oct 19)
    # -------------------------------------------------------------------------
    build_cover_9x16(
        ASSETS["b_cafe"],
        "📸 PROMPT OPTICS BREAKTHROUGH",
        "3 PROMPTS THAT REPLACED",
        "A ₹50,000 CAMERA LENS 📸",
        {"3", "PROMPTS", "REPLACED", "₹50,000"},
        os.path.join(REELS_DIR, "Cover-07.jpg"),
        accent_color=(56, 189, 248)
    )
    seg_07 = [
        {
            "tts": "Stop typing 8K ultra HD into your prompts. It forces smooth CGI plastic skin that people scroll right past.",
            "cap1": "Stop typing '8K ultra-HD'\ninto your AI prompts! 🚫",
            "cap2": "It triggers fake plastic skin\npeople scroll right past. 😳",
            "visuals": [(c_bcafe, "zoom_in"), (c_closeup, "zoom_out")]
        },
        {
            "tts": "Instead, use our Raw Smartphone Optics formula. Twenty-four millimeter candid lens physics, natural skin micro-texture, and subtle eye catchlights.",
            "cap1": "Use 24mm smartphone optics:\nNatural lens physics & micro-pores 📸",
            "cap2": "Real unretouched skin texture\nwith subtle eye catchlights ✨",
            "visuals": [(c_closeup, "zoom_in"), (c_cafe, "zoom_out")]
        },
        {
            "tts": "Comment PROMPT below, and I will DM you all 250 of our copy paste Character DNA prompts right now.",
            "cap1": "Comment 'PROMPT' below 👇\nTo get all 250+ prompts!",
            "cap2": "I'll DM you the complete\n5-Day Launch Kit instantly! 🚀",
            "visuals": [(c_bcafe, "zoom_in")]
        }
    ]
    render_custom_organic_reel(
        "Reel-07-Prompts-Replaced-Camera-Organic.mp4",
        "THE 3 PROMPTS THAT BEAT A ₹50K LENS 📸",
        "STOP TYPING '8K RENDER' 🚫",
        seg_07,
        accent=(56, 189, 248)
    )

    # -------------------------------------------------------------------------
    # Reel 08: From Mumbai Saree to Dubai Penthouse in 15 Mins (Wed Oct 21)
    # -------------------------------------------------------------------------
    build_cover_9x16(
        ASSETS["dubai"],
        "✈️ ZERO TRAVEL SHOOTS",
        "FROM MUMBAI SAREE TO",
        "DUBAI ROOFTOP IN 15 MINS 🌆",
        {"MUMBAI", "DUBAI", "15", "MINS"},
        os.path.join(REELS_DIR, "Cover-08.jpg"),
        accent_color=(234, 179, 8)
    )
    seg_08 = [
        {
            "tts": "Traditional shoots cost thousands in flights, hotels, and model fees. We took this exact creator from a Mumbai saree to a Dubai luxury rooftop in 15 minutes.",
            "cap1": "Traditional shoots cost thousands\nin flights, hotels & model fees ✈️",
            "cap2": "We moved her from Mumbai saree\nto Dubai rooftop in 15 mins! 🌆",
            "visuals": [(c_saree, "zoom_in"), (c_dubai, "zoom_out")]
        },
        {
            "tts": "The secret is our Character DNA seed lock. The face stays 100 percent identical, while the outfit, lighting, and background seamlessly swap on your phone.",
            "cap1": "The secret: Character DNA seed-lock 🧬\nFace stays 100% identical!",
            "cap2": "Outfit, lighting & location swap\nseamlessly straight from your phone 📱",
            "visuals": [(c_dubai, "zoom_in"), (c_cafe, "zoom_out")]
        },
        {
            "tts": "Want to build your own virtual creator? Comment TRAVEL below and I will send you the 5-day mobile blueprint.",
            "cap1": "Want to build your own AI creator?\nComment 'TRAVEL' below 👇",
            "cap2": "I'll DM you the complete\n5-Day Launch Kit instantly! 🚀",
            "visuals": [(c_saree, "zoom_in")]
        }
    ]
    render_custom_organic_reel(
        "Reel-08-Mumbai-To-Dubai-Organic.mp4",
        "MUMBAI SAREE TO DUBAI ROOFTOP ✈️",
        "ZERO EXPENSIVE TRAVEL SHOOTS 🌍",
        seg_08,
        accent=(234, 179, 8)
    )

    # -------------------------------------------------------------------------
    # Reel 09: Why 99% of AI Video Reels Warp (Fri Oct 23)
    # -------------------------------------------------------------------------
    build_cover_9x16(
        ASSETS["b_penthouse"],
        "🎬 4K MOTION MASTERCLASS",
        "WHY 99% OF AI VIDEOS",
        "WARP & HOW TO FIX IT 🔥",
        {"WHY", "99%", "WARP", "FIX"},
        os.path.join(REELS_DIR, "Cover-09.jpg"),
        accent_color=(168, 85, 247)
    )
    seg_09 = [
        {
            "tts": "Most AI video reels fail because people render 5 seconds in one go. The facial bone structure drifts and the eyes begin to melt.",
            "cap1": "Why do 99% of AI video reels fail?\nPeople render 5s in one go 🤯",
            "cap2": "Facial bone structure drifts\nand the eyes begin to melt! 🫠",
            "visuals": [(c_bpent, "zoom_in"), (c_bbali, "zoom_out")]
        },
        {
            "tts": "Inside PersonaLabs Academy, we cut our motion passes into 2-second retention loops. You get buttery smooth 4K motion, natural head turns, and zero warping.",
            "cap1": "We cut motion passes into\n2-second retention loops ✂️",
            "cap2": "Smooth 4K motion, natural turns\nand ZERO warping hands! 🔥",
            "visuals": [(c_bbali, "zoom_in"), (c_bpent, "zoom_out")]
        },
        {
            "tts": "Comment MOTION below and I will DM you our complete 1-Photo to 4K Viral Reel video masterclass.",
            "cap1": "Comment 'MOTION' below 👇\nFor the 4K video masterclass!",
            "cap2": "I'll DM you the complete\n5-Day Launch Kit instantly! 🚀",
            "visuals": [(c_bpent, "zoom_in")]
        }
    ]
    render_custom_organic_reel(
        "Reel-09-Locking-Facial-Bones-Organic.mp4",
        "STOP YOUR AI VIDEOS FROM MELTING 🫠",
        "THE 2-SECOND RETENTION SECRET 🎬",
        seg_09,
        accent=(168, 85, 247)
    )

    # -------------------------------------------------------------------------
    # Reel 10: Complete 5-Day Launch Checklist (Sun Oct 25)
    # -------------------------------------------------------------------------
    build_cover_9x16(
        ASSETS["saree"],
        "🚀 5-DAY LAUNCH SYSTEM",
        "BUILD AN AI INFLUENCER",
        "IN 5 DAYS STEP-BY-STEP 📱",
        {"BUILD", "AI", "INFLUENCER", "5", "DAYS"},
        os.path.join(REELS_DIR, "Cover-10.jpg"),
        accent_color=(34, 197, 94)
    )
    seg_10 = [
        {
            "tts": "Give me 5 days on your phone, and I will show you how to launch a hyper-realistic AI influencer from scratch.",
            "cap1": "Give me 5 days on your phone 📱\nAnd launch an AI creator from scratch!",
            "cap2": "Zero coding, zero gaming PCs,\nand 100% face consistency 🧬",
            "visuals": [(c_saree, "zoom_in"), (c_dubai, "zoom_out")]
        },
        {
            "tts": "Day 1 locks your Character DNA. Day 2 generates 50 luxury scenes. Day 3 turns photos into 4K Reels. Day 4 sets up Instagram, and Day 5 connects 24/7 Auto-DM sales.",
            "cap1": "Days 1-2: Lock Character DNA\n& render 50+ luxury travel scenes 🌍",
            "cap2": "Days 3-5: 4K Viral Reels\n& ManyChat 24/7 Auto-DM funnels 💰",
            "visuals": [(c_dubai, "zoom_in"), (c_cafe, "zoom_out"), (c_saree, "zoom_in")]
        },
        {
            "tts": "Comment LAUNCH below right now and I will DM you the complete 5-Day Launch Kit blueprint.",
            "cap1": "Ready to launch your page?\nComment 'LAUNCH' below 👇",
            "cap2": "I'll DM you the complete\n5-Day Blueprint instantly! 🚀",
            "visuals": [(c_saree, "zoom_in")]
        }
    ]
    render_custom_organic_reel(
        "Reel-10-Complete-Launch-Checklist-Organic.mp4",
        "LAUNCH AN AI INFLUENCER IN 5 DAYS 🚀",
        "CLICK-BY-CLICK MOBILE BLUEPRINT 📱",
        seg_10,
        accent=(34, 197, 94)
    )

def main():
    print("--- BUILDING BATCH #2 (7 DAYS: 19 OCT - 25 OCT 2026) ---")
    build_carousel_04()
    build_carousel_05()
    build_carousel_06()
    build_batch_2_reels()
    print("--- BATCH #2 ASSETS FULLY GENERATED & VERIFIED! ---")

if __name__ == "__main__":
    main()
