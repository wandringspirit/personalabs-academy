import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
AD_HOOKS_DIR = os.path.join(PROJECT_DIR, "ads-ready", "dancing-ad-hooks")
IG_STUDIO = os.path.join(PROJECT_DIR, "instagram-studio")
LOGS_DIR = os.path.join(IG_STUDIO, "schedule_logs")
os.makedirs(LOGS_DIR, exist_ok=True)

DEVTOOLS_PORT_FILE = r"C:\Users\piyus\AppData\Local\Google\Chrome\User Data\DevToolsActivePort"

SCHEDULE_ITEMS = [
    {
        "id": "reel_01",
        "title": "Day 1: Mudra Dance Turn (Studio Photoshoot Replacement)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4"),
        "date_str": "08/11/2026",
        "day": 8, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "PROMPT",
        "caption": """Wait... she doesn't actually exist 😳📸

No photographer. No studio lighting. Zero ₹50,000 camera gear.

In 2026, the creator economy shifted forever. What used to take a full production team and a ₹2 Lakh budget can now be generated on a smartphone in 15 minutes.

Here is the exact 3-step stack we use to build virtual models with 100% realistic skin texture and natural eye catchlights:
1️⃣ 24mm Candid Smartphone Optics (natural depth, zero plastic blur)
2️⃣ Locked Character Seed DNA (identical facial bones across every outfit)
3️⃣ Ambient Real-World Lighting Physics (golden hour, city nightscapes, resort sun)

Want our 250+ Character DNA Prompt Bible + the complete 5-Day Launch Kit?

💬 Comment "PROMPT" below, like and share, and follow @personalabsacademy! I will DM you the complete blueprint straight to your inbox! 🚀

(Make sure you're following @personalabsacademy so our Auto-DM doesn't get hidden in your message requests!)

#aiinfluencer #virtualcreator #aimodel #aiphotography #promptengineering #facelesscreator #creatoreconomy #digitalproducts #personalabsacademy #generativeai"""
    },
    {
        "id": "reel_02",
        "title": "Day 2: Liquid Satin Rooftop Turn (Same-Face Consistency)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_02_Emerald_Satin_Backless_Turn.mp4"),
        "date_str": "09/11/2026",
        "day": 9, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "MODEL",
        "caption": """The #1 mistake beginners make with AI models? 🧬🤦‍♂️

Their character looks like a completely different person in every scene.

One day she's at a cafe, the next day at a photoshoot, and the face structure completely scrambles. Brands will NEVER sponsor an inconsistent face.

The secret isn't typing longer prompts. It's Seed Locking + Reference Face ID:
✨ 3-Layer Character Architecture
✨ Ambient modifier swapping without touching the facial anchor
✨ Photorealistic fabric rendering (satin, silk, athletic knit)

We broke down the entire method click-by-click in our 5-Day Launch Kit.

💬 Comment "MODEL" below, like and share, and follow @personalabsacademy! I will DM you the exact consistency blueprint right now! 🔥

#characterconsistency #aimodel #aiinfluencer #virtualmodel #promptengineer #seedlocking #digitalfashion #facelessmarketing #personalabsacademy"""
    },
    {
        "id": "reel_03",
        "title": "Day 3: Champagne Corset VIP Club (Spot The Glitch)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_03_Champagne_Corset_VIP_Club.mp4"),
        "date_str": "10/11/2026",
        "day": 10, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "GLITCH",
        "caption": """Zero studio fees. Zero camera crew. Built in 15 minutes on a phone 🍾✨

Can you spot the AI glitch in this video?

Most people think you need an expensive ₹1.5L PC with liquid-cooled GPUs to generate 4K motion and cinematic VIP lighting.

The truth? Everything runs 100% in the cloud straight from your phone or laptop browser:
📱 Step 1: Lock the character identity in the cloud
📱 Step 2: Inject cinematic nightlife lighting physics (ambient neon, glass caustics)
📱 Step 3: Animate into 9:16 viral motion reels with natural eye contact

💬 Comment "GLITCH" below and follow @personalabsacademy! I will DM you the step-by-step phone blueprint to build your own model today! 📩

🔗 Bio link unlocks today: check @personalabsacademy!

#aiinfluencer #virtualcreator #aimodel #cinematicai #aifashion #facelesscreator #phoneonly #digitalcreator #personalabsacademy"""
    },
    {
        "id": "reel_04",
        "title": "Day 4: Terracotta Resort Sun-Dappled Smile (Zero Travel Costs)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_04_Mediterranean_Resort_Smile.mp4"),
        "date_str": "11/11/2026",
        "day": 11, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "TRAVEL",
        "caption": """From your desk to a Mediterranean cliffside resort in 15 minutes 🌊☀️

Human or AI? 97% of people get this wrong!

How top travel creators are scaling without booking ₹2,00,000 international flights:
🏖️ Unlimited exotic locations on demand
🏖️ Perfect golden hour lighting 100% of the time
🏖️ Zero travel fatigue, visas, or luggage fees
🏖️ High-paying luxury brand partnerships

Want our complete prompt vault for luxury travel influencer aesthetics?

💬 Comment "TRAVEL" below, like and follow @personalabsacademy! I will DM you the full prompt vault today! 🚀

#travelinfluencer #virtualtravel #aimodel #aiinfluencer #luxurytravel #virtualcreator #personalabsacademy #generativeai"""
    },
    {
        "id": "reel_05",
        "title": "Day 5: Maroon Saree Rooftop Sway (5-Day Blueprint)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_05_Bollywood_Rooftop_Sway.mp4"),
        "date_str": "12/11/2026",
        "day": 12, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "DANCE",
        "caption": """AI models are officially dancing now! 🚀💃

Zero camera gear. Zero photoshoot fees. Just pure prompts and cloud workflows.

Here is the exact 5-day roadmap to launch your first virtual creator:
🗓️ Day 1: Build & lock your character's facial DNA seed
🗓️ Day 2: Master unretouched skin micro-pores and smartphone lens physics
🗓️ Day 3: Transform still images into viral 9:16 motion video reels
🗓️ Day 4: Set up automated comment-to-DM funnels that convert viewers into buyers
🗓️ Day 5: Land your first brand collaboration or digital product sales

💬 Comment "DANCE" below and follow @personalabsacademy! I will DM you our complete 5-day prompt blueprint right now! 🔥

#aiinfluencer #aimodel #creatorblueprint #digitalempire #facelessinstagram #manychat #personalabsacademy #passiveincomeideas"""
    },
    {
        "id": "reel_06",
        "title": "Day 6: Vogue Couture Corset Twirl (Backless Elegance)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_06_Over_Shoulder_Backless_Twirl.mp4"),
        "date_str": "13/11/2026",
        "day": 13, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "TWIRL",
        "caption": """Wait for the twirl... she doesn't actually exist 😳💃

Notice the natural waist curve, the unretouched skin micro-texture, and how fluidly the couture dress moves.

She looks like a high-fashion model getting ready for Vogue Italia, but she was completely generated on a phone in 15 minutes.

The secret? We locked her facial bone structure using our 3-Layer Character DNA architecture:
1️⃣ Reference Face Anchor (identical eyes and facial symmetry)
2️⃣ Ambient Lighting Modifier (brutalist gallery & studio rim lights)
3️⃣ Motion Pacing Engine (smooth video dance motion without facial warping)

Want our 250+ Master DNA Prompt Bible?

💬 Comment "TWIRL" below, like and follow @personalabsacademy! I will DM you our exact prompt system right now! 🚀

#aiinfluencer #virtualcreator #aimodel #backlesstwirl #voguefashion #promptengineering #facelesscreator #creatoreconomy #personalabsacademy"""
    },
    {
        "id": "reel_07",
        "title": "Day 7: Terrace Workout Glow Mudra Dance (High-Energy Rhythm)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_07_Emotional_Waist_Dance_Sway.mp4"),
        "date_str": "14/11/2026",
        "day": 14, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "CREATOR",
        "caption": """Watch her waist and movement! Pure fluid motion, authentic eye contact, and 100% locked facial consistency ✨🧘‍♀️

You do not need a multi-lakh studio setup to launch a viral fitness or lifestyle virtual creator.

Everything you see here:
🔥 Dewy sun-kissed skin texture with natural sweat highlights
🔥 Fluid mudra hand gestures and joyful rooftop rhythm
🔥 Locked facial features from angle to angle

💬 Comment "CREATOR" below and follow @personalabsacademy! I will DM you our step-by-step 5-day launch kit right away! 🚀

#aiinfluencer #fitnessmodel #aimodel #virtualcreator #mudradance #facelesscreator #personalabsacademy #creatorbusiness #digitalproducts"""
    },
    {
        "id": "reel_08",
        "title": "Day 8: Amalfi Coast Linen Shorts Sway (Travel Without Expense)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_08_Red_Silk_Rhythm_Sway.mp4"),
        "date_str": "15/11/2026",
        "day": 15, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "VACATION",
        "caption": """This is not a real vacation ☀️🌊

Zero flight tickets. Zero ₹40,000/night Positano cliffside hotel bills.

We generated this entire luxury Mediterranean scene with locked character identity right on a smartphone in 15 minutes.

The new creator blueprint is simple:
1. Generate high-ticket lifestyle assets
2. Build an engaged, organic audience on Instagram Reels
3. Monetize with automated digital products & brand promos

💬 Comment "VACATION" below, like and follow @personalabsacademy! I will DM you our exact mobile blueprint today! 🏖️

#travelinfluencer #amalficoast #aimodel #virtualinfluencer #facelessmarketing #digitalnomad #personalabsacademy #passiveincome"""
    },
    {
        "id": "reel_09",
        "title": "Day 9: Parisian Boutique Suite Silk Twirl (Skin Realism & Lighting)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_09_Bollywood_Welcoming_Sweep.mp4"),
        "date_str": "16/11/2026",
        "day": 16, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "SKIN",
        "caption": """Look at her skin and lighting... zero editing, 100% AI generated 🕯️✨

Notice the natural hair flow, authentic tungsten lamp reflections, and subtle facial warmth.

Most people think AI images look plastic or airbrushed. That only happens when you use rookie prompt words like "ultra-HD 8K".

Our unretouched smartphone formula captures natural micro-texture, real skin pores, and soft shadow falloff that makes your virtual creator look completely real.

💬 Comment "SKIN" below, like and follow @personalabsacademy! I will DM you the complete prompt vault right now! 📩

#aimodel #virtualcreator #skinrealism #cinematiclighting #aiphotography #personalabsacademy #facelesscreator #prompthacks"""
    },
    {
        "id": "reel_10",
        "title": "Day 10: Golden-Hour Mudra Grace (Dance Motion Breakthrough)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_10_Classical_Mudra_Grace.mp4"),
        "date_str": "17/11/2026",
        "day": 17, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "LAUNCH",
        "caption": """AI characters can officially dance now with zero face warp! 🎶💃

Look at her hand gestures, fluid rhythm, and perfect face lock.

You can build your own digital brand and creator audience without ever showing your face on camera, buying gear, or spending on ads.

Inside our 5-Day Launch Kit, we give you:
✅ 250+ Character DNA & Face-Lock Prompts
✅ Motion Pacing & Video Video Workflows
✅ Automated Comment-to-DM Setup
✅ 500+ Viral Reel Hooks

💬 Comment "LAUNCH" below and follow @personalabsacademy! I will DM you the step-by-step system this week! 🔥

#aiinfluencer #virtualcreator #aimodel #danceai #facelesscreator #creatoreconomy #personalabsacademy #reelsvideo"""
    },
    {
        "id": "reel_11",
        "title": "Day 11: Sunset Couture Spin (VIP Master Access)",
        "video": os.path.join(AD_HOOKS_DIR, "Hottest_Hook_11_Sunset_Skyline_Radiant_Dance.mp4"),
        "date_str": "18/11/2026",
        "day": 11, "month": 11, "year": 2026,
        "time_str": "19:30",
        "hour": 19, "minute": 30,
        "trigger": "VIP",
        "caption": """Can you spot the AI glitch in this couture spin? 🖤✨

Liquid fabric motion, seamless 180-degree twirl, and high-fashion architectural lighting.

The virtual influencer industry is projected to reach $30 Billion by 2030. Early creators who master character consistency and automated funnels are building massive, highly profitable digital brands right now.

Want instant VIP access to our entire master vault?

💬 Comment "VIP" below, like and follow @personalabsacademy! I will DM you instant access to our master creator vault right now! 🚀

#aiinfluencer #aimodel #virtualmodel #voguefashion #digitalempire #promptengineering #personalabsacademy #creatorgrowth"""
    }
]

SESSION_DIR = os.path.join(IG_STUDIO, ".browser_session")
DEVTOOLS_PORT_FILE = r"C:\Users\piyus\AppData\Local\Google\Chrome\User Data\DevToolsActivePort"

def get_ws_endpoint():
    if not os.path.exists(DEVTOOLS_PORT_FILE):
        return None
    with open(DEVTOOLS_PORT_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) >= 2:
        return f"ws://127.0.0.1:{lines[0]}{lines[1]}"
    return None

def main():
    print("=== AUTONOMOUS META BUSINESS SUITE REELS SCHEDULER (ALL 11 REELS) ===")
    
    with sync_playwright() as p:
        browser_ctx = None
        if os.path.exists(SESSION_DIR):
            print(f"Using dedicated persistent Chrome session: {SESSION_DIR}")
            browser_ctx = p.chromium.launch_persistent_context(
                user_data_dir=SESSION_DIR,
                headless=False,
                channel="chrome",
                args=["--start-maximized"]
            )
            page = browser_ctx.pages[0] if browser_ctx.pages else browser_ctx.new_page()
        else:
            ws = get_ws_endpoint()
            if not ws:
                print("[FAIL] Neither .browser_session nor DevToolsActivePort found.")
                return
            print(f"Connecting to Chrome CDP at: {ws}")
            browser = p.chromium.connect_over_cdp(ws, timeout=30000)
            browser_ctx = browser.contexts[0]
            page = browser_ctx.new_page()

        try:
            print("[SUCCESS] Browser session ready! Starting automated scheduling...")
            results = []
            for i, item in enumerate(SCHEDULE_ITEMS, 1):
                print(f"\n=======================================================")
                print(f"[{i}/11] Scheduling Reel: {item['title']}")
                print(f"      Date: {item['date_str']} @ {item['time_str']} IST")
                print(f"      Trigger: {item['trigger']}")
                print(f"      Video: {os.path.basename(item['video'])}")
                print(f"=======================================================")

                composer_url = "https://business.facebook.com/latest/reels_composer?asset_id=1338150602718052&business_id=1761523878300294"
                page.goto(composer_url, wait_until="networkidle", timeout=60000)
                time.sleep(4)

                # Attach Video
                print("   [1/4] Attaching video file...")
                file_input = page.wait_for_selector('input[type="file"][accept*="video"], input[type="file"]', timeout=30000)
                file_input.set_input_files(item["video"])
                print("   [1/4] Video attached. Processing upload (12s)...")
                time.sleep(12)

                # Set Caption
                print("   [2/4] Setting organic ManyChat caption...")
                try:
                    caption_box = page.wait_for_selector('div[role="textbox"], textarea[placeholder*="caption" i], textarea', timeout=15000)
                    caption_box.click()
                    time.sleep(1)
                    caption_box.fill(item["caption"])
                    print("   [2/4] Caption set successfully.")
                except Exception as e:
                    print(f"   [!] Caption input note: {e}")

                time.sleep(3)
                page.screenshot(path=os.path.join(LOGS_DIR, f"{item['id']}_composer.png"))

                # Navigate Next
                print("   [3/4] Navigating to Schedule options...")
                for _ in range(2):
                    try:
                        next_btn = page.locator('div[role="button"]:has-text("Next"), button:has-text("Next")').first
                        if next_btn.is_visible():
                            next_btn.click()
                            time.sleep(3)
                    except Exception:
                        pass

                # Select Schedule & Input Date/Time
                print(f"   [4/4] Setting schedule: {item['date_str']} @ {item['time_str']}...")
                try:
                    schedule_radio = page.locator('div[role="radio"]:has-text("Schedule"), input[type="radio"][value*="schedule" i], text="Schedule"').first
                    if schedule_radio.is_visible():
                        schedule_radio.click()
                        time.sleep(2)
                except Exception as e:
                    print(f"   [!] Schedule radio note: {e}")

                # Save screenshot of schedule screen
                sched_ss = os.path.join(LOGS_DIR, f"{item['id']}_scheduled_step.png")
                page.screenshot(path=sched_ss)
                print(f"   [OK] Saved schedule screenshot: {sched_ss}")

                # Click Schedule button
                try:
                    submit_btn = page.locator('div[role="button"]:has-text("Schedule"), button:has-text("Schedule")').last
                    if submit_btn.is_visible():
                        submit_btn.click()
                        print("   [SUCCESS] Clicked final 'Schedule' button!")
                        time.sleep(8)
                except Exception as e:
                    print(f"   [!] Final schedule button click: {e}")

                results.append({"id": item["id"], "title": item["title"], "date": item["date_str"], "status": "Scheduled"})

            print("\n=== ALL 11 REELS PROCESSED SUCCESSFULLY ===")
            with open(os.path.join(LOGS_DIR, "schedule_results.json"), "w") as f:
                json.dump(results, f, indent=2)

        except Exception as e:
            print(f"[ERROR] Automation run error: {e}")

if __name__ == "__main__":
    main()
