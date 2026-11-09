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
CAROUSEL_02_DIR = os.path.join(IG_STUDIO, "03-Carousel-02-Smartphone-Realism-Prompts")
CAROUSEL_03_DIR = os.path.join(IG_STUDIO, "04-Carousel-03-5Day-Launch-Roadmap")

BRAIN_DIR = r"C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6"
SCRATCH_DIR = os.path.join(BRAIN_DIR, "scratch")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

for d in [REELS_DIR, CAROUSEL_02_DIR, CAROUSEL_03_DIR, SCRATCH_DIR]:
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
    return ord(ch) > 0x2000 and ch not in "—–•’“”→"

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

def add_top_bar(canvas, slide_num, accent=(139, 92, 246)):
    d = ImageDraw.Draw(canvas, "RGBA")
    d.rounded_rectangle((48, 42, 430, 94), radius=26, fill=(12, 14, 24, 225), outline=(accent[0], accent[1], accent[2], 180), width=2)
    d.ellipse((68, 59, 86, 77), fill=(56, 189, 248, 255))
    d.text((98, 55), "@personalabsacademy", font=FONT_TAG, fill=(240, 240, 255))
    d.rounded_rectangle((CW - 168, 42, CW - 48, 94), radius=26, fill=(12, 14, 24, 225), outline=(56, 189, 248, 180), width=2)
    d.text((CW - 140, 55), f"0{slide_num} / 05", font=FONT_TAG, fill=(56, 189, 248))

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

# ==============================================================================
# CAROUSEL #02 (Thu Oct 15): Plastic AI Skin vs. Raw iPhone Texture Prompts
# ==============================================================================
def build_carousel_02():
    # Slide 1
    s1 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(ASSETS["b_cafe"]).convert("RGB"), CW, 1060, align_y=0.18).convert("RGBA")
    s1.paste(hero, (0, 0))
    add_top_bar(s1, 1)
    d = ImageDraw.Draw(s1, "RGBA")
    d.rounded_rectangle((48, 785, 520, 845), radius=20, fill=(10, 14, 26, 230), outline=(56, 189, 248, 200), width=2)
    d.ellipse((70, 806, 88, 824), fill=(34, 197, 94, 255))
    d.text((102, 801), "35MM SMARTPHONE OPTICS • RAW SKIN", font=FONT_SMALL, fill=(235, 245, 255))
    add_bottom_magazine_panel(
        s1,
        badge_text="📸 PHOTOREALISM PROMPT SECRET",
        headline_lines=["WHY YOUR AI PHOTOS", "SCREAM 'FAKE' 📸"],
        subtitle_lines=["And the 3-Word 'Raw iPhone Optics' Fix", "That Makes Skin Look 100% Real (Swipe →)"],
        highlight_words={"SCREAM", "'FAKE'"},
        accent_color=(56, 189, 248)
    )
    s1.convert("RGB").save(os.path.join(CAROUSEL_02_DIR, "slide-01.jpg"), quality=96, subsampling=0)

    # Slide 2
    s2 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    bg = crop_fill(Image.open(ASSETS["studio"]).convert("RGB"), CW, CH).filter(ImageFilter.GaussianBlur(26))
    bg = ImageEnhance.Brightness(bg).enhance(0.28).convert("RGBA")
    s2.paste(bg, (0, 0))
    add_top_bar(s2, 2)
    items = [
        ("aira", "01 • NATURAL PORES", 0.15),
        ("b_cafe", "02 • CANDID CAFE LIGHT", 0.16),
        ("cafe", "03 • 24MM IPHONE LENS", 0.16),
        ("b_penthouse", "04 • FLYAWAY HAIRS", 0.16),
    ]
    positions = [(48, 118), (560, 118), (48, 506), (560, 506)]
    cell_w, cell_h = 472, 368
    d = ImageDraw.Draw(s2, "RGBA")
    for (key, label, ay), (px, py) in zip(items, positions):
        im = crop_fill(Image.open(ASSETS[key]).convert("RGB"), cell_w, cell_h, align_y=ay).convert("RGBA")
        s2.paste(im, (px, py), rounded_rect_mask((cell_w, cell_h), 24))
        d.rounded_rectangle((px, py, px + cell_w, py + cell_h), radius=24, outline=(168, 85, 247, 190), width=3)
        d.rounded_rectangle((px + 18, py + cell_h - 52, px + 310, py + cell_h - 14), radius=14, fill=(12, 15, 28, 230), outline=(56, 189, 248, 160), width=1)
        d.text((px + 32, py + cell_h - 45), label, font=FONT_SMALL, fill=(240, 248, 255))
    add_bottom_magazine_panel(
        s2,
        badge_text="❌ THE #1 BEGINNER MISTAKE",
        headline_lines=["STOP TYPING '8K", "ULTRA-HD RENDER' 🚫"],
        subtitle_lines=["Those keywords trigger plastic CGI skin.", "Real cameras have grain & micro-texture."],
        highlight_words={"'8K", "ULTRA-HD", "RENDER'"},
        accent_color=(239, 68, 68)
    )
    s2.convert("RGB").save(os.path.join(CAROUSEL_02_DIR, "slide-02.jpg"), quality=96, subsampling=0)

    # Slide 3
    s3 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    s3.paste(bg, (0, 0))
    add_top_bar(s3, 3)
    d = ImageDraw.Draw(s3, "RGBA")
    px, py, pw, ph = 48, 128, 410, 720
    im_p = crop_fill(Image.open(ASSETS["closeup"]).convert("RGB"), pw, ph, align_y=0.2).convert("RGBA")
    s3.paste(im_p, (px, py), rounded_rect_mask((pw, ph), 28))
    d.rounded_rectangle((px, py, px + pw, py + ph), radius=28, outline=(56, 189, 248, 220), width=3)
    cards = [
        (484, 128, 1032, 344, (56, 189, 248), "1. CAMERA OPTICS TOKEN 📸", "\"Shot on iPhone 15 Pro,", "24mm f/1.78 candid lens\"", "⚡ Eliminates fake studio bokeh"),
        (484, 368, 1032, 584, (168, 85, 247), "2. SKIN TEXTURE TOKEN 🧬", "\"Unretouched skin pores,", "natural subsurface scattering\"", "✅ Zero plastic AI airbrushing"),
        (484, 608, 1032, 848, (34, 197, 94), "3. IMPERFECTION TOKEN ✨", "\"Subtle flyaway baby hairs,", "natural eye catchlights\"", "🔥 Passes the Explore page test"),
    ]
    for x1, y1, x2, y2, col, title, l1, l2, foot in cards:
        d.rounded_rectangle((x1, y1, x2, y2), radius=26, fill=(14, 18, 34, 242), outline=(col[0], col[1], col[2], 235), width=3)
        d.rounded_rectangle((x1 + 20, y1 + 22, x1 + 30, y2 - 22), radius=5, fill=col)
        draw_text_with_emoji(s3, (x1 + 48, y1 + 20), title, FONT_TAG, FONT_EMOJI_SM, fill=col, shadow=False)
        draw_text_with_emoji(s3, (x1 + 48, y1 + 58), l1, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s3, (x1 + 48, y1 + 94), l2, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s3, (x1 + 48, y1 + 142), foot, FONT_SMALL, FONT_EMOJI_SM, fill=(180, 200, 230), shadow=False)
    add_bottom_magazine_panel(
        s3,
        badge_text="🧬 THE 3-PART REALISM FORMULA",
        headline_lines=["ADD 'IPHONE LENS", "PHYSICS' INSTEAD 📱"],
        subtitle_lines=["Copy these 3 prompt modifiers so every", "portrait looks like a real smartphone photo."],
        highlight_words={"'IPHONE", "LENS", "PHYSICS'"},
        accent_color=(56, 189, 248)
    )
    s3.convert("RGB").save(os.path.join(CAROUSEL_02_DIR, "slide-03.jpg"), quality=96, subsampling=0)

    # Slide 4
    s4 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    s4.paste(bg, (0, 0))
    add_top_bar(s4, 4)
    d = ImageDraw.Draw(s4, "RGBA")
    lx, ly, lw, lh = 52, 145, 455, 700
    rx, ry, rw, rh = 555, 145, 473, 700
    im_l = crop_fill(Image.open(ASSETS["b_bali"]).convert("RGB"), lw, lh, align_y=0.18).convert("RGBA")
    im_r = crop_fill(Image.open(ASSETS["b_rooftop"]).convert("RGB"), rw, rh, align_y=0.18).convert("RGBA")
    s4.paste(im_l, (lx, ly), rounded_rect_mask((lw, lh), 28))
    s4.paste(im_r, (rx, ry), rounded_rect_mask((rw, rh), 28))
    d.rounded_rectangle((lx, ly, lx + lw, ly + lh), radius=28, outline=(168, 85, 247, 235), width=3)
    d.rounded_rectangle((rx, ry, rx + rw, ry + rh), radius=28, outline=(56, 189, 248, 235), width=3)
    d.rounded_rectangle((lx + 20, ly + 20, lx + 335, ly + 66), radius=16, fill=(12, 16, 30, 235), outline=(168, 85, 247, 200), width=2)
    draw_text_with_emoji(s4, (lx + 36, ly + 31), "☀️ GOLDEN HOUR BALI", FONT_SMALL, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    d.rounded_rectangle((rx + 20, ry + 20, rx + 355, ry + 66), radius=16, fill=(12, 16, 30, 235), outline=(56, 189, 248, 200), width=2)
    draw_text_with_emoji(s4, (rx + 36, ry + 31), "🌙 EVENING ROOFTOP", FONT_SMALL, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    add_bottom_magazine_panel(
        s4,
        badge_text="🌍 SAME FACE • INFINITE LIGHTING",
        headline_lines=["LOCK THE SEED,", "SWAP THE SCENE 🔥"],
        subtitle_lines=["Keep 100% identical facial structure from", "Bali beach sunlight to evening rooftop."],
        highlight_words={"LOCK", "SEED,", "SWAP"},
        accent_color=(168, 85, 247)
    )
    s4.convert("RGB").save(os.path.join(CAROUSEL_02_DIR, "slide-04.jpg"), quality=96, subsampling=0)

    # Slide 5
    s5 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s5.paste(bg, (0, 0))
    add_top_bar(s5, 5)
    d = ImageDraw.Draw(s5, "RGBA")
    avatars = [("b_cafe", 240), ("saree", 460), ("b_bali", 680)]
    for key, ax in avatars:
        av = crop_fill(Image.open(ASSETS[key]).convert("RGB"), 160, 160, align_y=0.14).convert("RGBA")
        s5.paste(av, (ax, 120), rounded_rect_mask((160, 160), 80))
        d.ellipse((ax, 120, ax + 160, 280), outline=(56, 189, 248, 255), width=4)
    vx1, vy1, vx2, vy2 = 65, 310, CW - 65, 855
    d.rounded_rectangle((vx1, vy1, vx2, vy2), radius=32, fill=(14, 18, 34, 242), outline=(168, 85, 247, 230), width=3)
    d.rounded_rectangle((CW//2 - 235, vy1 - 22, CW//2 + 235, vy1 + 24), radius=22, fill=(168, 85, 247, 255))
    d.text((CW//2 - 205, vy1 - 12), "UNLOCK THE 250+ PROMPT BIBLE", font=FONT_TAG, fill=(255, 255, 255))
    perks = [
        "✅ 250+ Copy-Paste Realism & Skin Prompts",
        "✅ 100% Same-Face Seed-Locking Workflow",
        "✅ 23 HD Step-by-Step Video Tutorials",
        "✅ 1-Photo to 4K Viral Reel Mobile Pipeline",
        "✅ 500+ Viral Reel Hooks & Auto-DM Scripts"
    ]
    py = vy1 + 50
    for p in perks:
        draw_text_with_emoji(s5, (vx1 + 42, py), p, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(235, 245, 255), shadow=False)
        py += 64
    bx1, by1, bx2, by2 = 105, 710, CW - 105, 815
    d.rounded_rectangle((bx1, by1, bx2, by2), radius=28, fill=(56, 189, 248, 255), outline=(255, 255, 255, 230), width=3)
    draw_centered_mixed_line(s5, by1 + 28, "💬 COMMENT 'PROMPT' OR 'AI' BELOW", FONT_BTN, FONT_EMOJI_BTN, fill=(8, 12, 24), shadow=False)
    add_bottom_magazine_panel(
        s5,
        badge_text="🎁 INSTANT AUTO-DM DELIVERY",
        headline_lines=["STEAL ALL 250+", "REALISM PROMPTS 🔓"],
        subtitle_lines=["Comment 'PROMPT' or 'AI' below and I'll", "DM you the complete 5-Day Blueprint!"],
        highlight_words={"250+", "REALISM", "PROMPTS"},
        accent_color=(56, 189, 248)
    )
    s5.convert("RGB").save(os.path.join(CAROUSEL_02_DIR, "slide-05.jpg"), quality=96, subsampling=0)
    print("[OK] Built Carousel #02 (5 slides)")

# ==============================================================================
# CAROUSEL #03 (Sat Oct 17): The 5-Day AI Influencer Launch Roadmap
# ==============================================================================
def build_carousel_03():
    bg = crop_fill(Image.open(ASSETS["studio"]).convert("RGB"), CW, CH).filter(ImageFilter.GaussianBlur(26))
    bg = ImageEnhance.Brightness(bg).enhance(0.28).convert("RGBA")

    # Slide 1
    s1 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    hero = crop_fill(Image.open(ASSETS["b_bali"]).convert("RGB"), CW, 1060, align_y=0.18).convert("RGBA")
    s1.paste(hero, (0, 0))
    add_top_bar(s1, 1)
    d = ImageDraw.Draw(s1, "RGBA")
    d.rounded_rectangle((48, 785, 535, 845), radius=20, fill=(10, 14, 26, 230), outline=(168, 85, 247, 220), width=2)
    d.ellipse((70, 806, 88, 824), fill=(34, 197, 94, 255))
    d.text((102, 801), "ZERO CAMERAS • 100% MOBILE WORKFLOW", font=FONT_SMALL, fill=(235, 245, 255))
    add_bottom_magazine_panel(
        s1,
        badge_text="🚀 COMPLETE 5-DAY CREATOR ROADMAP",
        headline_lines=["GIVE ME 5 DAYS TO", "LAUNCH YOUR AI PAGE 🚀"],
        subtitle_lines=["From Blank Account to Hyper-Realistic", "Virtual Influencer & Auto-DM Funnel (Swipe →)"],
        highlight_words={"5", "DAYS", "LAUNCH"},
        accent_color=(168, 85, 247)
    )
    s1.convert("RGB").save(os.path.join(CAROUSEL_03_DIR, "slide-01.jpg"), quality=96, subsampling=0)

    # Slide 2
    s2 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    s2.paste(bg, (0, 0))
    add_top_bar(s2, 2)
    items = [
        ("b_cafe", "DAY 1 • DNA SEED LOCK", 0.16),
        ("b_bali", "DAY 2 • LUXURY SCENES", 0.16),
        ("b_gym", "DAY 2 • FITNESS NICHE", 0.16),
        ("b_rooftop", "DAY 2 • NIGHT OPTICS", 0.16),
    ]
    positions = [(48, 118), (560, 118), (48, 506), (560, 506)]
    cell_w, cell_h = 472, 368
    d = ImageDraw.Draw(s2, "RGBA")
    for (key, label, ay), (px, py) in zip(items, positions):
        im = crop_fill(Image.open(ASSETS[key]).convert("RGB"), cell_w, cell_h, align_y=ay).convert("RGBA")
        s2.paste(im, (px, py), rounded_rect_mask((cell_w, cell_h), 24))
        d.rounded_rectangle((px, py, px + cell_w, py + cell_h), radius=24, outline=(56, 189, 248, 190), width=3)
        d.rounded_rectangle((px + 18, py + cell_h - 52, px + 315, py + cell_h - 14), radius=14, fill=(12, 15, 28, 230), outline=(56, 189, 248, 160), width=1)
        d.text((px + 32, py + cell_h - 45), label, font=FONT_SMALL, fill=(240, 248, 255))
    add_bottom_magazine_panel(
        s2,
        badge_text="📅 DAYS 1 & 2 • IDENTITY & LIFESTYLE",
        headline_lines=["DAYS 1–2: LOCK HER", "CHARACTER DNA 🧬"],
        subtitle_lines=["Freeze 1 recognizable face across 50+", "travel, cafe, fitness & fashion scenes."],
        highlight_words={"CHARACTER", "DNA"},
        accent_color=(56, 189, 248)
    )
    s2.convert("RGB").save(os.path.join(CAROUSEL_03_DIR, "slide-02.jpg"), quality=96, subsampling=0)

    # Slide 3
    s3 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    s3.paste(bg, (0, 0))
    add_top_bar(s3, 3)
    d = ImageDraw.Draw(s3, "RGBA")
    lx, ly, lw, lh = 52, 145, 455, 700
    rx, ry, rw, rh = 555, 145, 473, 700
    im_l = crop_fill(Image.open(ASSETS["saree"]).convert("RGB"), lw, lh, align_y=0.18).convert("RGBA")
    im_r = crop_fill(Image.open(ASSETS["b_penthouse"]).convert("RGB"), rw, rh, align_y=0.18).convert("RGBA")
    s3.paste(im_l, (lx, ly), rounded_rect_mask((lw, lh), 28))
    s3.paste(im_r, (rx, ry), rounded_rect_mask((rw, rh), 28))
    d.rounded_rectangle((lx, ly, lx + lw, ly + lh), radius=28, outline=(168, 85, 247, 235), width=3)
    d.rounded_rectangle((rx, ry, rx + rw, ry + rh), radius=28, outline=(56, 189, 248, 235), width=3)
    d.rounded_rectangle((lx + 20, ly + 20, lx + 355, ly + 66), radius=16, fill=(12, 16, 30, 235), outline=(168, 85, 247, 200), width=2)
    draw_text_with_emoji(s3, (lx + 36, ly + 31), "🎬 DAY 3: 4K 9:16 MOTION", FONT_SMALL, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    d.rounded_rectangle((rx + 20, ry + 20, rx + 365, ry + 66), radius=16, fill=(12, 16, 30, 235), outline=(56, 189, 248, 200), width=2)
    draw_text_with_emoji(s3, (rx + 36, ry + 31), "📈 DAY 4: 3-SEC VIRAL HOOKS", FONT_SMALL, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    add_bottom_magazine_panel(
        s3,
        badge_text="📅 DAYS 3 & 4 • VIRAL REELS ENGINE",
        headline_lines=["DAYS 3–4: 9:16 REELS", "& RETENTION HOOKS 🎬"],
        subtitle_lines=["Turn static portraits into looping 4K Reels", "engineered for 110%+ watch time."],
        highlight_words={"9:16", "REELS", "RETENTION"},
        accent_color=(168, 85, 247)
    )
    s3.convert("RGB").save(os.path.join(CAROUSEL_03_DIR, "slide-03.jpg"), quality=96, subsampling=0)

    # Slide 4
    s4 = Image.new("RGBA", (CW, CH), (9, 11, 20, 255))
    s4.paste(bg, (0, 0))
    add_top_bar(s4, 4)
    d = ImageDraw.Draw(s4, "RGBA")
    px, py, pw, ph = 48, 128, 360, 720
    im_p = crop_fill(Image.open(ASSETS["dubai"]).convert("RGB"), pw, ph, align_y=0.16).convert("RGBA")
    s4.paste(im_p, (px, py), rounded_rect_mask((pw, ph), 28))
    d.rounded_rectangle((px, py, px + pw, py + ph), radius=28, outline=(34, 197, 94, 220), width=3)
    cards = [
        (434, 128, 1032, 344, (56, 189, 248), "1. DIGITAL PRODUCTS & GUIDES 📦", "Sell low-ticket kits & vaults", "via ManyChat Auto-DM links", "⚡ 100% profit margin • Instant delivery"),
        (434, 368, 1032, 584, (168, 85, 247), "2. AFFILIATE & AI TOOL STACKS 🔗", "Earn recurring commissions", "recommending creator tools", "✅ Zero inventory or fulfillment"),
        (434, 608, 1032, 848, (34, 197, 94), "3. BRAND DEALS & THEME PAGES 💰", "Monetize attention across", "fashion, travel & tech niches", "🔥 Runs in 20 mins/day from phone"),
    ]
    for x1, y1, x2, y2, col, title, l1, l2, foot in cards:
        d.rounded_rectangle((x1, y1, x2, y2), radius=26, fill=(14, 18, 34, 242), outline=(col[0], col[1], col[2], 235), width=3)
        d.rounded_rectangle((x1 + 20, y1 + 22, x1 + 30, y2 - 22), radius=5, fill=col)
        draw_text_with_emoji(s4, (x1 + 48, y1 + 20), title, FONT_TAG, FONT_EMOJI_SM, fill=col, shadow=False)
        draw_text_with_emoji(s4, (x1 + 48, y1 + 58), l1, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s4, (x1 + 48, y1 + 94), l2, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
        draw_text_with_emoji(s4, (x1 + 48, y1 + 142), foot, FONT_SMALL, FONT_EMOJI_SM, fill=(180, 200, 230), shadow=False)
    add_bottom_magazine_panel(
        s4,
        badge_text="📅 DAY 5 • AUTOMATED MONETIZATION",
        headline_lines=["DAY 5: 24/7 AUTO-DM", "MONETIZATION SYSTEM 💰"],
        subtitle_lines=["Every comment triggers an instant DM", "that educates viewers & closes sales."],
        highlight_words={"24/7", "AUTO-DM", "MONETIZATION"},
        accent_color=(34, 197, 94)
    )
    s4.convert("RGB").save(os.path.join(CAROUSEL_03_DIR, "slide-04.jpg"), quality=96, subsampling=0)

    # Slide 5
    s5 = Image.new("RGBA", (CW, CH), (8, 10, 18, 255))
    s5.paste(bg, (0, 0))
    add_top_bar(s5, 5)
    d = ImageDraw.Draw(s5, "RGBA")
    avatars = [("saree", 240), ("b_bali", 460), ("dubai", 680)]
    for key, ax in avatars:
        av = crop_fill(Image.open(ASSETS[key]).convert("RGB"), 160, 160, align_y=0.14).convert("RGBA")
        s5.paste(av, (ax, 120), rounded_rect_mask((160, 160), 80))
        d.ellipse((ax, 120, ax + 160, 280), outline=(56, 189, 248, 255), width=4)
    vx1, vy1, vx2, vy2 = 65, 310, CW - 65, 855
    d.rounded_rectangle((vx1, vy1, vx2, vy2), radius=32, fill=(14, 18, 34, 242), outline=(168, 85, 247, 230), width=3)
    d.rounded_rectangle((CW//2 - 235, vy1 - 22, CW//2 + 235, vy1 + 24), radius=22, fill=(168, 85, 247, 255))
    d.text((CW//2 - 205, vy1 - 12), "START THE 5-DAY AI LAUNCH KIT", font=FONT_TAG, fill=(255, 255, 255))
    perks = [
        "✅ Day 1: Character DNA & 100% Face-Lock",
        "✅ Day 2: 250+ Raw Smartphone Skin Prompts",
        "✅ Day 3: 1-Photo to 4K Viral Reel Pipeline",
        "✅ Day 4: 500+ Viral Reel Hooks & Templates",
        "✅ Day 5: 24/7 ManyChat Auto-DM Funnel"
    ]
    py = vy1 + 50
    for p in perks:
        draw_text_with_emoji(s5, (vx1 + 42, py), p, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(235, 245, 255), shadow=False)
        py += 64
    bx1, by1, bx2, by2 = 105, 710, CW - 105, 815
    d.rounded_rectangle((bx1, by1, bx2, by2), radius=28, fill=(56, 189, 248, 255), outline=(255, 255, 255, 230), width=3)
    draw_centered_mixed_line(s5, by1 + 28, "💬 COMMENT 'LAUNCH' OR 'AI' BELOW", FONT_BTN, FONT_EMOJI_BTN, fill=(8, 12, 24), shadow=False)
    add_bottom_magazine_panel(
        s5,
        badge_text="🎁 INSTANT DM DELIVERY • PERSONALABS ACADEMY",
        headline_lines=["READY TO LAUNCH", "THIS WEEKEND? 🚀"],
        subtitle_lines=["Comment 'LAUNCH' or 'AI' below and I'll", "DM you the complete 5-Day Blueprint!"],
        highlight_words={"LAUNCH", "WEEKEND?"},
        accent_color=(56, 189, 248)
    )
    s5.convert("RGB").save(os.path.join(CAROUSEL_03_DIR, "slide-05.jpg"), quality=96, subsampling=0)
    print("[OK] Built Carousel #03 (5 slides)")

# ==============================================================================
# REELS #04, #05, #06 + COVERS #04, #05, #06
# ==============================================================================
def build_cover_9x16(img_path, badge_text, line1, line2, highlight_words, out_path):
    base = crop_fill(Image.open(img_path).convert("RGB"), RW, RH, align_y=0.20).convert("RGBA")
    grad = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(RH):
        if y < 320:
            a = int((1 - y / 320) * 180)
            gd.line([(0, y), (RW, y)], fill=(6, 8, 16, a))
        elif y > 1050:
            prog = (y - 1050) / (RH - 1050)
            a = int(min(250, (prog ** 1.1) * 260))
            gd.line([(0, y), (RW, y)], fill=(6, 8, 16, a))
    base.alpha_composite(grad)
    d = ImageDraw.Draw(base, "RGBA")
    # Center 4:5 grid safe zone is y=285..1635
    d.rounded_rectangle((64, 1180, RW - 64, 1560), radius=34, fill=(14, 18, 34, 238), outline=(56, 189, 248, 220), width=3)
    bw = int(measure_text_with_emoji(d, badge_text, FONT_TAG, FONT_EMOJI_SM)) + 52
    bx1 = (RW - bw) // 2
    d.rounded_rectangle((bx1, 1154, bx1 + bw, 1204), radius=24, fill=(168, 85, 247, 255))
    draw_text_with_emoji(base, (bx1 + 26, 1166), badge_text, FONT_TAG, FONT_EMOJI_SM, fill=(255, 255, 255), shadow=False)
    draw_centered_mixed_line(base, 1235, line1, FONT_HEAD, FONT_EMOJI_HEAD, width=RW, fill=(255, 255, 255), highlight_words=highlight_words)
    draw_centered_mixed_line(base, 1308, line2, FONT_HEAD, FONT_EMOJI_HEAD, width=RW, fill=(255, 255, 255), highlight_words=highlight_words)
    draw_centered_mixed_line(base, 1425, "💬 Comment 'AI' for the 5-Day Blueprint 🚀", FONT_SUB_BOLD, FONT_EMOJI_SM, width=RW, fill=(74, 222, 128))
    base.convert("RGB").save(out_path, quality=95, subsampling=0)

def load_cv_9x16(img_path):
    pil = crop_fill(Image.open(img_path).convert("RGB"), RW, RH, align_y=0.22)
    return cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)

def load_demo_frames(max_frames=150):
    frames = []
    if not os.path.exists(DEMO_VID):
        return frames
    cap = cv2.VideoCapture(DEMO_VID)
    while len(frames) < max_frames:
        ret, f = cap.read()
        if not ret:
            break
        h, w = f.shape[:2]
        scale = max(RW / w, RH / h)
        nw, nh = int(w * scale), int(h * scale)
        res = cv2.resize(f, (nw, nh), interpolation=cv2.INTER_LINEAR)
        x0 = (nw - RW) // 2
        y0 = (nh - RH) // 2
        frames.append(res[y0:y0+RH, x0:x0+RW])
    cap.release()
    return frames

def apply_kb(img_bgr, prog, mode="zoom_in"):
    h, w = img_bgr.shape[:2]
    if mode == "zoom_in":
        scale = 1.0 + 0.09 * prog
        cx, cy = w * 0.5, h * (0.48 - 0.03 * prog)
    elif mode == "zoom_out":
        scale = 1.09 - 0.09 * prog
        cx, cy = w * 0.5, h * (0.45 + 0.03 * prog)
    else:
        scale = 1.06
        cx, cy = w * (0.48 + 0.04 * prog), h * 0.48
    cw, ch = w / scale, h / scale
    x1 = max(0, min(w - cw, cx - cw / 2))
    y1 = max(0, min(h - ch, cy - ch / 2))
    cropped = img_bgr[int(y1):int(y1+ch), int(x1):int(x1+cw)]
    return cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)

def make_organic_endcard_bgr(bg_path, keyword="AI"):
    base_pil = crop_fill(Image.open(bg_path).convert("RGB"), RW, RH, align_y=0.2).filter(ImageFilter.GaussianBlur(18))
    base_pil = ImageEnhance.Brightness(base_pil).enhance(0.32).convert("RGBA")
    de = ImageDraw.Draw(base_pil, "RGBA")
    f_hero = get_font("arialbd.ttf", 56)
    f_em_hero = get_font("seguiemj.ttf", 52)
    de.rounded_rectangle((28, 364, 1052, 1485), radius=42, fill=(13, 17, 31, 248), outline=(139, 92, 246, 255), width=4)
    de.rounded_rectangle((175, 402, 905, 474), radius=26, fill=(168, 85, 247, 255))
    draw_centered_mixed_line(base_pil, 422, "🎁 5-DAY AI INFLUENCER BLUEPRINT", FONT_TAG, FONT_EMOJI_SM, width=RW, fill=(255, 255, 255), shadow=False)
    draw_centered_mixed_line(base_pil, 504, "AI INFLUENCER", f_hero, f_em_hero, width=RW, fill=(255, 255, 255))
    draw_centered_mixed_line(base_pil, 574, "5-DAY LAUNCH KIT 🚀", f_hero, f_em_hero, width=RW, fill=(56, 189, 248))
    perks = [
        "✅  23 HD Step-by-Step Video Lessons (Subtitled)",
        "✅  250+ Character DNA & Face-Lock Prompts",
        "✅  1-Photo to 4K Viral Reel Mobile Workflow",
        "✅  500+ Viral Reel Hooks & Auto-DM Templates"
    ]
    py = 672
    for p in perks:
        draw_text_with_emoji(base_pil, (76, py), p, FONT_SUB_BOLD, FONT_EMOJI_SM, fill=(240, 246, 255), shadow=False)
        py += 64
    de.rounded_rectangle((100, 950, 980, 1014), radius=22, fill=(18, 25, 44, 255), outline=(56, 189, 248, 230), width=2)
    draw_centered_mixed_line(base_pil, 968, "⚡ INSTANT DELIVERY TO YOUR INSTAGRAM DMs", FONT_TAG, FONT_EMOJI_SM, width=RW, fill=(56, 189, 248), shadow=False)
    de.rounded_rectangle((96, 1040, 984, 1215), radius=30, fill=(16, 42, 38, 255), outline=(34, 197, 94, 255), width=3)
    draw_centered_mixed_line(base_pil, 1064, f"💬 COMMENT \"{keyword}\" OR \"AI\"", FONT_HEAD, FONT_EMOJI_HEAD, width=RW, fill=(74, 222, 128), shadow=False)
    draw_centered_mixed_line(base_pil, 1134, "And I'll DM You the Full 5-Day Blueprint!", FONT_SUB_BOLD, FONT_EMOJI_SM, width=RW, fill=(235, 250, 245), shadow=False)
    de.rounded_rectangle((80, 1245, 1000, 1375), radius=32, fill=(124, 58, 237, 255), outline=(216, 180, 254, 255), width=3)
    draw_centered_mixed_line(base_pil, 1290, f"COMMENT '{keyword}' FOR INSTANT ACCESS >>", FONT_BTN, FONT_EMOJI_BTN, width=RW, fill=(255, 255, 255), shadow=False)
    draw_centered_mixed_line(base_pil, 1410, "Follow @personalabsacademy so our Auto-DM reaches your inbox!", FONT_TAG, FONT_EMOJI_SM, width=RW, fill=(185, 200, 230), shadow=False)
    return cv2.cvtColor(np.array(base_pil.convert("RGB")), cv2.COLOR_RGB2BGR)

def decorate_reel_frame(frame_bgr, top_hook, sub_hook_3s, caption_text, show_3s_pill=False):
    pil = Image.fromarray(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    d = ImageDraw.Draw(pil, "RGBA")
    f_hook = get_font("segoeuib.ttf", 40)
    f_sub = get_font("segoeuib.ttf", 42)
    f_pill = get_font("segoeuib.ttf", 22)

    if top_hook:
        d.rounded_rectangle((55, 95, 1025, 205), radius=28, fill=(15, 23, 42, 235), outline=(168, 85, 247, 255), width=3)
        d.text((540, 150), top_hook, font=f_hook, fill=(255, 255, 255, 255), anchor="mm")

    d.rounded_rectangle((665, 222, 1030, 286), radius=20, fill=(14, 17, 30, 245), outline=(168, 85, 247, 220), width=2)
    d.ellipse((688, 245, 706, 263), fill=(56, 189, 248, 255))
    d.text((718, 238), "@personalabsacademy", font=f_pill, fill=(240, 248, 255))

    if show_3s_pill and sub_hook_3s:
        d.rounded_rectangle((50, 222, 645, 286), radius=20, fill=(14, 17, 30, 248), outline=(56, 189, 248, 225), width=2)
        draw_text_with_emoji(pil, (74, 238), sub_hook_3s, f_pill, FONT_EMOJI_SM, fill=(56, 189, 248), shadow=False)

    if caption_text:
        words = caption_text.split()
        lines, cur = [], ""
        for w in words:
            test = (cur + " " + w).strip()
            bb = d.textbbox((0, 0), test, font=f_sub)
            if bb[2] - bb[0] > 880 and cur:
                lines.append(cur)
                cur = w
            else:
                cur = test
        if cur:
            lines.append(cur)
        line_h = 56
        total_h = len(lines) * line_h + 36
        max_w = max((d.textbbox((0, 0), ln, font=f_sub)[2] for ln in lines), default=400)
        box_w = min(980, max_w + 64)
        x0 = (RW - box_w) // 2
        y0 = 1585 - total_h // 2
        d.rounded_rectangle((x0, y0, x0+box_w, y0+total_h), radius=24, fill=(12, 16, 28, 232), outline=(56, 189, 248, 150), width=2)
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

def render_custom_organic_reel(out_filename, top_hook, sub_hook_3s, segments):
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
            if isinstance(vis_item, list) and len(vis_item) > 0:
                frame = vis_item[f_idx % len(vis_item)].copy()
            elif mode == "static":
                frame = vis_item.copy()
            else:
                frame = apply_kb(vis_item, sub_prog, mode=mode)
            if prev_last is not None and f_idx < 5:
                alpha = (f_idx + 1) / 6.0
                frame = cv2.addWeighted(frame, alpha, prev_last, 1.0 - alpha, 0)
            active_cap = cap1 if prog < 0.48 else cap2
            show_3s = (global_frame_idx < 96)
            rendered = decorate_reel_frame(frame, top_hook, sub_hook_3s, active_cap, show_3s_pill=show_3s)
            proc.stdin.write(rendered.tobytes())
            if f_idx == num_frames - 1:
                prev_last = frame.copy()
            global_frame_idx += 1
    proc.stdin.close()
    proc.wait()
    if os.path.exists(final_aac):
        os.remove(final_aac)
    print(f"[OK] Rendered {out_filename} ({os.path.getsize(out_path):,} bytes)")

def build_reels_04_05_06():
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
    demo_frames = load_demo_frames(150)

    ec_prompt = make_organic_endcard_bgr(ASSETS["b_cafe"], "PROMPT")
    ec_reel = make_organic_endcard_bgr(ASSETS["dubai"], "REEL")
    ec_launch = make_organic_endcard_bgr(ASSETS["b_bali"], "LAUNCH")

    # Covers 04, 05, 06
    build_cover_9x16(
        ASSETS["b_cafe"],
        "📸 RAW IPHONE OPTICS SECRET",
        "WHY 99% OF AI PHOTOS",
        "LOOK FAKE (3-WORD FIX)",
        {"FAKE", "(3-WORD", "FIX)"},
        os.path.join(REELS_DIR, "Cover-04.jpg")
    )
    build_cover_9x16(
        ASSETS["b_penthouse"],
        "🎬 1 PHOTO TO 4K VIRAL REEL",
        "HOW WE ANIMATE AI",
        "WITH ZERO MELTING 🔥",
        {"ANIMATE", "ZERO", "MELTING"},
        os.path.join(REELS_DIR, "Cover-05.jpg")
    )
    build_cover_9x16(
        ASSETS["b_bali"],
        "🚀 20-MIN DAILY AI ROUTINE",
        "TRADITIONAL SHOOT VS",
        "AI INFLUENCER MATH 💰",
        {"AI", "INFLUENCER", "MATH"},
        os.path.join(REELS_DIR, "Cover-06.jpg")
    )
    print("[OK] Built Cover-04.jpg, Cover-05.jpg, Cover-06.jpg")

    # Reel #04 (Wed Oct 14)
    render_custom_organic_reel(
        "Reel-04-Raw-iPhone-Realism-Secret-Organic.mp4",
        "WHY 99% OF AI PHOTOS LOOK FAKE (3-WORD FIX)",
        "📸 35MM IPHONE OPTICS • ZERO CGI GLOW 👀",
        [
            {
                "tts": "Why do ninety-nine percent of A.I. influencer photos immediately scream fake plastic?",
                "cap1": "Why do 99% of AI influencer photos...",
                "cap2": "...immediately scream 'FAKE PLASTIC'? 😳",
                "visuals": [(c_bcafe, "zoom_in"), (c_closeup, "zoom_out")]
            },
            {
                "tts": "Because beginners type outdated words like 8K render or ultra-HD, which force smooth CGI skin.",
                "cap1": "Beginners type '8K render' or 'ultra-HD'...",
                "cap2": "...which forces fake CGI plastic skin ❌",
                "visuals": [(c_saree, "zoom_in"), (c_bbali, "pan")]
            },
            {
                "tts": "Instead, use our Raw Smartphone Optics formula: lock 24-millimeter iPhone lens physics, natural skin pores, and candid golden-hour lighting.",
                "cap1": "Use our Raw Smartphone Optics formula 📱",
                "cap2": "24mm iPhone lens + natural pores + candid light 🧬",
                "visuals": [(demo_frames if demo_frames else c_cafe, "zoom_in"), (c_bpent, "zoom_out"), (c_broof, "pan")]
            },
            {
                "tts": "Comment PROMPT or A.I. below right now, and I'll DM you our complete 5-Day Blueprint and 250-plus realism prompt vault instantly!",
                "cap1": "Comment 'PROMPT' or 'AI' below right now 💬",
                "cap2": "And I'll DM you the 5-Day Blueprint instantly! 🚀",
                "visuals": [(ec_prompt, "static")]
            }
        ]
    )

    # Reel #05 (Fri Oct 16)
    render_custom_organic_reel(
        "Reel-05-Static-To-4K-Motion-Organic.mp4",
        "1 STATIC PHOTO TO 4K VIRAL REEL IN 10 MINS",
        "🎬 ZERO MELTING HANDS • 100% FACE LOCK 🔥",
        [
            {
                "tts": "Here is how we turn one static A.I. portrait into a hyper-real 9-by-16 Reel without her face or hands ever warping.",
                "cap1": "How we turn 1 static AI portrait...",
                "cap2": "...into a 4K Reel with zero warping 🎬",
                "visuals": [(c_bpent, "zoom_in"), (demo_frames if demo_frames else c_dubai, "zoom_out")]
            },
            {
                "tts": "Step one: lock your character's facial bone structure and identity seed before generating any movement.",
                "cap1": "Step 1: Lock her Character DNA & Seed 🧬",
                "cap2": "100% identical face across every frame",
                "visuals": [(c_cafe, "zoom_in"), (c_gym, "pan"), (c_dubai, "zoom_out")]
            },
            {
                "tts": "Step two: run our mobile cloud motion pipeline with subtle camera pan controls and 2-second retention cuts.",
                "cap1": "Step 2: Run the mobile cloud motion pass 📱",
                "cap2": "Subtle micro-expressions + 2-second cuts ⚡",
                "visuals": [(c_bcafe, "zoom_in"), (c_bgym, "zoom_out"), (c_broof, "pan")]
            },
            {
                "tts": "Want our complete mobile video pipeline? Comment REEL or A.I. below and I'll send the 5-Day Launch Kit straight to your DMs!",
                "cap1": "Comment 'REEL' or 'AI' below right now 💬",
                "cap2": "And I'll DM you the 5-Day Launch Kit! 🚀",
                "visuals": [(ec_reel, "static")]
            }
        ]
    )

    # Reel #06 (Sun Oct 18)
    render_custom_organic_reel(
        "Reel-06-Faceless-Creator-Math-Organic.mp4",
        "TRADITIONAL SHOOT VS 20-MIN AI CREATOR PAGE",
        "💰 ZERO STUDIO COST • 24/7 AUTO-DM FUNNEL 🚀",
        [
            {
                "tts": "A single fashion studio shoot costs fifty thousand rupees, a camera crew, and a full weekend of editing.",
                "cap1": "1 traditional fashion studio shoot costs...",
                "cap2": "...₹50,000+ and a full weekend of work 💸",
                "visuals": [(c_bbali, "zoom_in"), (c_saree, "zoom_out")]
            },
            {
                "tts": "With our 5-Day A.I. Influencer System, you can put the exact same virtual persona in a Mumbai cafe, a Bali beach club, and a Dubai rooftop in twenty minutes from your phone.",
                "cap1": "With our 5-Day AI Influencer System 🧬",
                "cap2": "Mumbai Cafe → Bali Beach → Dubai Rooftop in 20 mins 📱",
                "visuals": [(c_cafe, "zoom_in"), (c_bcafe, "pan"), (c_dubai, "zoom_out"), (c_broof, "zoom_in")]
            },
            {
                "tts": "And when you connect our ManyChat Comment-to-DM funnel, every Reel replies to viewers and closes sales while you sleep.",
                "cap1": "Connect our ManyChat Comment-to-DM funnel 🤖",
                "cap2": "Replies to viewers & closes sales 24/7 💰",
                "visuals": [(demo_frames if demo_frames else c_bpent, "zoom_in"), (c_gym, "zoom_out")]
            },
            {
                "tts": "Ready to launch your A.I. page this week? Comment LAUNCH or A.I. below and I'll DM you the complete 5-Day Blueprint instantly!",
                "cap1": "Comment 'LAUNCH' or 'AI' below right now 💬",
                "cap2": "Get the complete 5-Day Blueprint in your DMs! 🚀",
                "visuals": [(ec_launch, "static")]
            }
        ]
    )

if __name__ == "__main__":
    build_carousel_02()
    build_carousel_03()
    build_reels_04_05_06()
    print("ALL BATCH 1B ASSETS (WED OCT 14 - SUN OCT 18) GENERATED SUCCESSFULLY!")
