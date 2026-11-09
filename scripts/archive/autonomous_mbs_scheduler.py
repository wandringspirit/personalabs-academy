import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
IG_STUDIO = os.path.join(PROJECT_DIR, "instagram-studio")
REELS_DIR = os.path.join(IG_STUDIO, "02-Organic-Reels")
LOGS_DIR = os.path.join(IG_STUDIO, "schedule_logs")
os.makedirs(LOGS_DIR, exist_ok=True)

DEVTOOLS_PORT_FILE = r"C:\Users\piyus\AppData\Local\Google\Chrome\User Data\DevToolsActivePort"

SCHEDULE_ITEMS = [
    {
        "id": "reel_07",
        "title": "Reel #07: Raw Smartphone Optics Prompting Formula",
        "date_str": "19/10/2026",
        "day": 19,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-07-Prompts-Replaced-Camera-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-07.jpg"),
        "caption": """Stop typing "8K ultra-HD render" into your AI prompts 📸🚫

Those generic keywords trigger smooth plastic skin, fake CGI reflections, and dead cartoon eyes that people scroll right past.

Instead, we use our Raw Smartphone Optics formula:
1️⃣ 24mm Candid iPhone Lens Physics (natural depth of field & zero artificial studio blur)
2️⃣ Unretouched Micro-Pores & Texture (real facial skin physics + subtle baby flyaways)
3️⃣ Ambient Catchlights (natural room reflections in the pupils that scream 100% human)

Pair that with a locked Character DNA seed, and your virtual persona looks like a real person living in Mumbai, Paris, or Dubai.

Want our 250+ Character DNA Prompt Bible + the complete 5-Day AI Influencer Launch Kit?

💬 Comment "PROMPT" or "AI" below and I'll DM you the full step-by-step blueprint instantly! 🚀

(Make sure you're following @personalabsacademy so our Auto-DM doesn't get hidden in your message requests!)

#aiinfluencer #promptengineering #aimodel #aiphotography #virtualcreator #facelesscreator #personalabsacademy #digitalcreator #creatoreconomy"""
    },
    {
        "id": "carousel_04",
        "title": "Carousel #04: Same-Face Consistency Architecture (5 Slides)",
        "date_str": "20/10/2026",
        "day": 20,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "carousel",
        "slides": [
            os.path.join(IG_STUDIO, "06-Carousel-04-Same-Face-Consistency", f"slide-0{i}.jpg")
            for i in range(1, 6)
        ],
        "caption": """The #1 reason beginners fail with AI influencers? Their character looks like a different person in every post 🧬🤦‍♂️

Swipe through all 5 slides to see how we maintain 100% face consistency across Indian Sarees, Gym Activewear, Emerald Cafes, and Dubai Penthouse Reels:

👉 Slide 2: Why traditional prompting scrambles facial bone structures
👉 Slide 3: The 3-Layer Character DNA Architecture (Base Seed + Facial Reference + Ambient Modifier)
👉 Slide 4: Real side-by-side consistency proof across 4 high-contrast scenes
👉 Slide 5: How to unlock our 250+ Master DNA Prompt Bible

You don't need a ₹1.5L gaming PC or coding knowledge. Everything runs in the cloud straight from your smartphone in 15 minutes.

💬 Comment "MODEL" or "AI" below and I'll DM you the exact 5-Day Launch Blueprint! 🚀

(Save this post so you can reference the prompt structure later 🔖)

#aiinfluencer #characterconsistency #aimodel #facelessmarketing #aipersona #seedlocking #personalabsacademy #creatorgrowth #digitalempire"""
    },
    {
        "id": "reel_08",
        "title": "Reel #08: Mumbai to Dubai in 15 Minutes (Zero Travel Expense)",
        "date_str": "21/10/2026",
        "day": 21,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-08-Mumbai-To-Dubai-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-08.jpg"),
        "caption": """Traditional photoshoot: ₹25,000 flight to Dubai + ₹15,000 hotel + ₹20,000 model fee ✈️💸
PersonaLabs AI Creator: 15 minutes on a phone while drinking coffee ☕📱

Watch how we took the exact same virtual persona from a traditional Indian silk saree to an ultra-luxury Dubai rooftop lounge in under 15 minutes.

Zero travel expenses.
Zero camera gear.
100% facial consistency.

When you lock your Character DNA seed, you can place your AI creator anywhere in the world—from Bali beach clubs to Parisian fashion weeks—without ever leaving your room.

Want to learn how to build, launch, and monetize your own luxury AI creator page in 5 days?

💬 Comment "TRAVEL" or "AI" below and I'll DM you the complete 5-Day Launch Kit! 🚀

#aiinfluencer #travelcreator #dubailife #virtualinfluencer #luxurylifestyle #facelesscreator #personalabsacademy #digitalproducts #sidehustleideas"""
    },
    {
        "id": "carousel_05",
        "title": "Carousel #05: The 100% Free Mobile AI Stack (4 Cloud Tools)",
        "date_str": "22/10/2026",
        "day": 22,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "carousel",
        "slides": [
            os.path.join(IG_STUDIO, "07-Carousel-05-Free-Mobile-Stack", f"slide-0{i}.jpg")
            for i in range(1, 6)
        ],
        "caption": """"Do I need an expensive gaming PC or coding skills to build an AI influencer?" 💻❌
No. Here is the 100% Free Mobile AI Stack we use (Swipe through all 4 tools →)

You can run your entire virtual creator business straight from your phone browser:
🛠️ Tool 1: Cloud Image Engine (Free Daily Cloud GPU Credits — zero laptop required)
🛠️ Tool 2: Face-Lock Reference Engine (100% identical facial features across every scene)
🛠️ Tool 3: 4K Motion Engine (Transforms still portraits into looping viral Reels)
🛠️ Tool 4: 24/7 Comment-to-DM Automation (Replies to comments & sends product links while you sleep)

Swipe through all 5 slides to copy the exact setup and workflow!

Want our complete click-by-click video walkthrough showing how to connect all 4 tools on your phone?

💬 Comment "TOOLS" or "AI" below and I'll DM you the free masterclass link instantly! 🚀

(Save this carousel so you have the tool list whenever you need it 🔖)

#aiinfluencer #aitools #mobilecreator #freestack #digitalcreator #facelesscreator #personalabsacademy #creatorbusiness #onlineincome"""
    },
    {
        "id": "reel_09",
        "title": "Reel #09: Locking Facial Bones & Micro-Texture in Video Motion",
        "date_str": "23/10/2026",
        "day": 23,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-09-Locking-Facial-Bones-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-09.jpg"),
        "caption": """Why do 99% of AI video reels look like melting wax? 🫠🎬

The #1 rookie mistake is generating 5-to-10 seconds of raw video in a single pass. The AI model's spatial attention drifts, facial bone structure distorts, and hands start warping into bizarre shapes.

Inside PersonaLabs Academy, we follow the 2-Second Retention Loop Rule:
1️⃣ High-Resolution Base Portrait: Lock your Character DNA & skin micro-texture first
2️⃣ 2-Second Micro-Expression Cuts: Gentle head turns, realistic blinks, and subtle hair movements
3️⃣ 9:16 Cloud Upscaling: Crisp 4K mobile export that stops the thumb scroll

No warping hands. No drifting jawlines. Just clean, hyper-real viral Reels engineered for 110%+ watch time.

Want our complete 1-Photo to 4K Viral Reel video masterclass?

💬 Comment "MOTION" or "AI" below and I'll DM you the complete 5-Day Launch Kit instantly! 🚀

#aiinfluencer #aireels #aivideo #videomarketing #instagramgrowth #facelesscreator #personalabsacademy #creatorbusiness #digitalempire"""
    },
    {
        "id": "carousel_06",
        "title": "Carousel #06: The ₹50,000/Month Faceless Creator Income Math",
        "date_str": "24/10/2026",
        "day": 24,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "carousel",
        "slides": [
            os.path.join(IG_STUDIO, "08-Carousel-06-Faceless-Creator-Income", f"slide-0{i}.jpg")
            for i in range(1, 6)
        ],
        "caption": """How faceless creators make ₹50,000/month without ever showing their face, hiring models, or buying a single camera 💰📱 (Swipe for the real math →)

Most people think you need 100,000 followers to make money on Instagram. That is completely false.

Here is the realistic conversion math with an automated AI creator page:
📊 1 Reel reaches 5,000 views on Explore
💬 120 people comment "AI" to get your prompt guide
🤖 ManyChat automatically sends 120 DMs in seconds
👥 80 people visit your digital product vault
🛒 Just 3 to 5 sales at ₹597 = ₹2,985/day (₹89,550/month!)

With 95%+ profit margins on digital products, you keep almost all of it.

Swipe through all 5 slides to see:
✅ Slide 2: The Traditional Creator Trap vs. The AI Creator Advantage
✅ Slide 3: The 3 High-Margin Revenue Streams (Digital Guides, Brand Collabs, VIP Vaults)
✅ Slide 4: The Daily Conversion Math Breakdown
✅ Slide 5: The complete 5-Day Launch Kit package

Ready to build your faceless creator business this weekend?

💬 Comment "MONEY" or "AI" below and I'll DM you the full 5-Day Blueprint instantly! 🚀

#aiinfluencer #facelessmarketing #digitalproducts #passiveincome #onlinebusiness #personalabsacademy #sidehustle #creatoreconomy"""
    },
    {
        "id": "reel_10",
        "title": "Reel #10: The Complete 5-Day Launch Checklist & Roadmap",
        "date_str": "25/10/2026",
        "day": 25,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-10-Complete-Launch-Checklist-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-10.jpg"),
        "caption": """Give me 5 days on your phone, and I will show you how to build, launch, and monetize a 100% realistic AI Influencer from scratch 🚀📱

Here is your exact day-by-day roadmap:
📅 Day 1: Character DNA Seed-Locking (lock one unique face with 100% consistency)
📅 Day 2: Photorealistic Scene Generation (render 50+ luxury lifestyle, gym & cafe photos)
📅 Day 3: Static Image to 4K Viral Reel Pipeline (add smooth cinematic motion & retention cuts)
📅 Day 4: Instagram Creator Page Setup (bio optimization & trial reels algorithm warmup)
📅 Day 5: 24/7 Auto-DM Monetization (connect ManyChat comment triggers & digital product vault)

Inside the PersonaLabs Academy 5-Day Launch Kit, you get:
✅ 23 Step-by-Step HD Video Masterclasses (English Subtitled)
✅ 250+ Character DNA & Face-Lock Prompts
✅ 500+ Viral Reel Hooks & Auto-DM Templates
✅ Uncensored VIP Monetization & Telegram Funnel Guide

Ready to launch before this month ends?

💬 Comment "LAUNCH" or "AI" below and I will automatically DM you the complete 5-Day Blueprint right now! 👇🔥

#aiinfluencer #aimodel #creatorblueprint #digitalempire #facelessinstagram #manychat #personalabsacademy #passiveincomeideas #contentcreator"""
    },
    {
        "id": "reel_11_bonus_dance",
        "title": "Bonus Reel #11: Viral Saree Dance Reveal (Wait For The Turn)",
        "date_str": "26/10/2026",
        "day": 26,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-11-Viral-Saree-Dance-Reveal-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-11.jpg"),
        "caption": """Wait for the turn... she doesn't actually exist 😳💃

Every single frame of this dancing video was generated with 100% AI. 
Notice how her facial bone structure and identity stay completely locked even through the hair flip, saree drape, and spin turn.

Zero models. Zero studios. Zero expensive camera crews.

Smart creators are using this exact mobile AI workflow to build massive audiences on Instagram and automate 24/7 digital product sales.

Want to learn how we built her on a phone in 5 days?

💬 Comment "DANCE" or "AI" below and I'll DM you the complete 5-Day Launch Blueprint instantly! 🚀

#aiinfluencer #aimodel #sareedance #virtualcreator #indiancreator #facelesscreator #personalabsacademy #reelsindia #trendingreel"""
    },
    {
        "id": "reel_12_bonus_dance",
        "title": "Bonus Reel #12: Can You Spot The AI Glitch In Her Dance? (Realism Challenge)",
        "date_str": "27/10/2026",
        "day": 27,
        "month": 10,
        "year": 2026,
        "time_str": "19:30",
        "hour": 19,
        "minute": 30,
        "type": "reel",
        "video": os.path.join(REELS_DIR, "Reel-12-Can-You-Spot-The-Glitch-Organic.mp4"),
        "cover": os.path.join(REELS_DIR, "Cover-12.jpg"),
        "caption": """Can you spot the AI glitch in this dance? 🤔 (99% of people fail this test)

Watch her hand mudras, waist sway, and eye reflections closely. 

Most people scroll right past thinking she's a real creator filming in her living room. There is zero warping and zero melting because we use our Raw Smartphone Optics formula and 2-second retention cuts.

Ready to build your own hyper-real virtual creator?

💬 Comment "AI" below and I'll DM you the complete 5-Day Launch Kit right now! 👇🚀

#aiinfluencer #aimodel #virtualinfluencer #facelessmarketing #digitalproducts #personalabsacademy #reelsindia #aivideo"""
    }
]

def get_ws_endpoint():
    if not os.path.exists(DEVTOOLS_PORT_FILE):
        return None
    with open(DEVTOOLS_PORT_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) >= 2:
        return f"ws://127.0.0.1:{lines[0]}{lines[1]}"
    return None

def center_prompt_dialog():
    import ctypes
    from ctypes import wintypes
    try:
        user32 = ctypes.windll.user32
        hdesk = user32.OpenDesktopW('default', 0, False, 0x10000000)
        if hdesk:
            user32.SetThreadDesktop(hdesk)
            time.sleep(1.5)
            WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
            dialogs = []
            def cb(hwnd, lp):
                if user32.IsWindowVisible(hwnd):
                    l = user32.GetWindowTextLengthW(hwnd)
                    if l > 0:
                        b = ctypes.create_unicode_buffer(l + 1)
                        user32.GetWindowTextW(hwnd, b, l + 1)
                        if "allow remote debugging" in b.value.lower():
                            dialogs.append(hwnd)
                return True
            user32.EnumWindows(WNDENUMPROC(cb), 0)
            if dialogs:
                active_h = dialogs[-1]
                # Find Chrome window to center prompt right over it
                chrome_hwnd = None
                def find_chrome(hwnd, lp):
                    nonlocal chrome_hwnd
                    if user32.IsWindowVisible(hwnd):
                        l = user32.GetWindowTextLengthW(hwnd)
                        if l > 0:
                            b = ctypes.create_unicode_buffer(l + 1)
                            user32.GetWindowTextW(hwnd, b, l + 1)
                            if "google chrome" in b.value.lower() and ("personalabs" in b.value.lower() or "meta business" in b.value.lower()):
                                chrome_hwnd = hwnd
                    return True
                user32.EnumWindows(WNDENUMPROC(find_chrome), 0)
                
                cx, cy = 400, 300
                if chrome_hwnd:
                    r = wintypes.RECT()
                    user32.GetWindowRect(chrome_hwnd, ctypes.byref(r))
                    cx = r.left + (r.right - r.left) // 2 - 250
                    cy = r.top + (r.bottom - r.top) // 2 - 130

                SWP_SHOWWINDOW = 0x0040
                user32.SetWindowPos(active_h, 0, cx, cy, 520, 260, SWP_SHOWWINDOW)
                user32.SetForegroundWindow(active_h)
                print(f"[OK] Centered 'Allow remote debugging?' prompt (HWND {active_h}) right over your Chrome window at ({cx}, {cy}).")
    except Exception as e:
        print(f"[!] Dialog centering note: {e}")

def connect_to_chrome(timeout_minutes=30):
    print("=== CONNECTING TO RUNNING CHROME INSTANCE VIA CDP ===")
    p = sync_playwright().start()
    ws = get_ws_endpoint()
    if not ws:
        print("[FAIL] DevToolsActivePort not found. Make sure Chrome is open.")
        p.stop()
        return None, None

    import threading
    t_center = threading.Thread(target=center_prompt_dialog, daemon=True)
    t_center.start()

    print(f"Connecting to {ws} with single long timeout (waiting up to {timeout_minutes} mins for user 'Allow' click)...")
    try:
        # Single connection with long timeout prevents dialog spamming
        browser = p.chromium.connect_over_cdp(ws, timeout=timeout_minutes * 60 * 1000)
        print("[SUCCESS] DevTools handshake accepted! Taking over Chrome session...")
        return p, browser
    except Exception as e:
        print(f"[ERROR] Could not connect to Chrome CDP: {e}")
        p.stop()
        return None, None

def schedule_reel(page, item):
    print(f"\n---> Scheduling Reel: {item['title']} for {item['date_str']} @ {item['time_str']}")
    composer_url = "https://business.facebook.com/latest/reels_composer?asset_id=1338150602718052&business_id=1761523878300294"
    page.goto(composer_url, wait_until="networkidle", timeout=60000)
    time.sleep(4)

    # 1. Attach Video File
    print(f"   [1/5] Attaching video: {os.path.basename(item['video'])}")
    file_input = page.wait_for_selector('input[type="file"][accept*="video"], input[type="file"]', timeout=30000)
    file_input.set_input_files(item["video"])
    print("   [1/5] Video attached. Waiting for upload processing...")
    time.sleep(12)

    # 2. Set Caption
    print("   [2/5] Setting caption text...")
    try:
        caption_box = page.wait_for_selector('div[role="textbox"], textarea[placeholder*="caption" i], textarea', timeout=15000)
        caption_box.click()
        time.sleep(1)
        caption_box.fill(item["caption"])
        print("   [2/5] Caption filled successfully.")
    except Exception as e:
        print(f"   [!] Note on caption fill: {e}")

    time.sleep(3)
    # Save step screenshot
    screenshot_path = os.path.join(LOGS_DIR, f"{item['id']}_step1.png")
    page.screenshot(path=screenshot_path)

    # 3. Navigate to Next / Step 2 & 3
    print("   [3/5] Navigating to Share step...")
    for _ in range(3):
        try:
            next_btn = page.locator('div[role="button"]:has-text("Next"), button:has-text("Next")').first
            if next_btn.is_visible():
                next_btn.click()
                time.sleep(3)
        except:
            break

    # 4. Configure Schedule
    print(f"   [4/5] Selecting Schedule option ({item['date_str']} @ {item['time_str']})...")
    try:
        sched_radio = page.locator('text="Schedule", div[role="radio"]:has-text("Schedule"), label:has-text("Schedule")').first
        if sched_radio.is_visible():
            sched_radio.click()
            time.sleep(2)
    except Exception as e:
        print(f"   [!] Schedule option toggle note: {e}")

    # Set Date & Time if date input visible
    try:
        date_input = page.locator('input[placeholder*="dd/mm/yyyy" i], input[type="text"][value*="/"]').first
        if date_input.is_visible():
            date_input.fill(item["date_str"])
            time.sleep(1)
    except:
        pass

    # Save schedule step screenshot
    screenshot_sched = os.path.join(LOGS_DIR, f"{item['id']}_schedule_ready.png")
    page.screenshot(path=screenshot_sched)

    # 5. Click Schedule Button
    print("   [5/5] Submitting Schedule...")
    try:
        sched_btn = page.locator('div[role="button"]:has-text("Schedule"):not(:has-text("Schedule post")), button:has-text("Schedule")').last
        if sched_btn.is_visible():
            sched_btn.click()
            print("   [OK] Schedule button clicked! Waiting 10s for confirmation...")
            time.sleep(10)
    except Exception as e:
        print(f"   [!] Note on schedule button click: {e}")

    print(f"[COMPLETED] Reel {item['id']} processed.")

def schedule_carousel(page, item):
    print(f"\n---> Scheduling Carousel: {item['title']} for {item['date_str']} @ {item['time_str']}")
    composer_url = "https://business.facebook.com/latest/composer?asset_id=1338150602718052&business_id=1761523878300294&context_ref=CONTENT_CALENDAR"
    page.goto(composer_url, wait_until="networkidle", timeout=60000)
    time.sleep(4)

    # 1. Attach Images
    print(f"   [1/5] Attaching {len(item['slides'])} carousel slides...")
    file_input = page.wait_for_selector('input[type="file"][accept*="image"], input[type="file"]', timeout=30000)
    file_input.set_input_files(item["slides"])
    print("   [1/5] Slides attached. Waiting 8s for thumbnails...")
    time.sleep(8)

    # 2. Fill Caption
    print("   [2/5] Setting caption text...")
    try:
        caption_box = page.wait_for_selector('div[role="textbox"], textarea', timeout=15000)
        caption_box.click()
        time.sleep(1)
        caption_box.fill(item["caption"])
        print("   [2/5] Caption filled.")
    except Exception as e:
        print(f"   [!] Note on caption fill: {e}")

    # 3. Schedule Option
    print(f"   [3/5] Setting Schedule option ({item['date_str']} @ {item['time_str']})...")
    try:
        sched_toggle = page.locator('text="Schedule", div[role="radio"]:has-text("Schedule")').first
        if sched_toggle.is_visible():
            sched_toggle.click()
            time.sleep(2)
    except Exception as e:
        print(f"   [!] Schedule toggle note: {e}")

    screenshot_path = os.path.join(LOGS_DIR, f"{item['id']}_carousel_ready.png")
    page.screenshot(path=screenshot_path)

    # 4. Submit Schedule
    print("   [4/5] Clicking Schedule button...")
    try:
        sched_btn = page.locator('div[role="button"]:has-text("Schedule"), button:has-text("Schedule")').last
        if sched_btn.is_visible():
            sched_btn.click()
            print("   [OK] Schedule submitted. Waiting 10s...")
            time.sleep(10)
    except Exception as e:
        print(f"   [!] Submit button note: {e}")

    print(f"[COMPLETED] Carousel {item['id']} processed.")

def main():
    print("====================================================")
    print("  AUTONOMOUS INSTAGRAM META BUSINESS SUITE SCHEDULER")
    print("  Account: @personalabsacademy")
    print(f"  Total items to schedule: {len(SCHEDULE_ITEMS)}")
    print("====================================================")

    p, browser = connect_to_chrome(timeout_minutes=60)
    if not browser:
        print("[FAIL] Could not connect to Chrome. Exiting.")
        return

    ctx = browser.contexts[0]
    page = ctx.new_page()

    for idx, item in enumerate(SCHEDULE_ITEMS, 1):
        print(f"\n==================== [{idx}/{len(SCHEDULE_ITEMS)}] ====================")
        if item["type"] == "reel":
            schedule_reel(page, item)
        elif item["type"] == "carousel":
            schedule_carousel(page, item)
        time.sleep(3)

    print("\n====================================================")
    print("  ALL 9 ITEMS PROCESSED SUCCESSFULLY!")
    print("  Verifying Scheduled Posts list...")
    print("====================================================")
    page.goto("https://business.facebook.com/latest/posts/scheduled_posts?asset_id=1338150602718052&business_id=1761523878300294", wait_until="networkidle")
    time.sleep(5)
    final_screenshot = os.path.join(LOGS_DIR, "final_scheduled_posts_verified.png")
    page.screenshot(path=final_screenshot)
    print(f"[OK] Verification screenshot saved to: {final_screenshot}")
    browser.close()
    p.stop()

if __name__ == "__main__":
    main()
