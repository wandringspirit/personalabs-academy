# 🗓️ PersonaLabs Academy — Launch Roadmap & 30-Day Content Calendar (`ROADMAP.md`)

> [!IMPORTANT]
> ### 🔐 CRITICAL OWNER REMINDER: Dedicated Gmail & 3-Folder Private Google Drive Setup
> 1. **Create 1 Dedicated Brand Gmail Account** (e.g., `personalabs.academy@gmail.com`) and host both your **Google Sheet (`PersonaLabs Academy — Orders DB`)** and your **3 Google Drive Folders** under this same Gmail account so your personal Gmail/name is never visible.
> 2. **Split Google Drive into 3 Separate Folders — Keep All 3 Set to `Restricted (Only people added can open)`**:
>    - 📁 **Folder 1 (`01-Core-Course-Videos`)**: Upload the 19 watermark-free, English-captioned Core Videos + `Bonus.docx` + `readme.docx` + `250-AI-Character-DNA-Prompt-Bible.html`. *(Auto-whitelisted via `DriveApp.addViewer` for ALL buyers).*
>    - 📁 **Folder 2 (`02-Uncensored-NSFW-Addon-Videos`)**: Upload the 4 watermark-free, English-captioned NSFW/Uncensored Videos (`14, 15, 16, 17`) + `Uncensored-Content-Hack-VIP-Guide.html`. *(Auto-whitelisted ONLY for Order Bump #1 buyers).*
>    - 📁 **Folder 3 (`03-500-Viral-Hooks-And-Prompts-Pack`)**: Upload `500-Viral-Reel-Hooks-And-AutoDM-Pack.html` + `250-AI-Character-DNA-Prompt-Bible.html`. *(Auto-whitelisted ONLY for Order Bump #2 buyers).*
> 3. **Paste the 3 Folder IDs into your Google Apps Script** (see [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md)) so every buyer's Gmail is automatically granted Viewer access the second they complete checkout!

---

## Phase 1: Pre-Launch Checklist (Day 0)
- [x] Deploy `https://personalabs.store` via GitHub + Netlify Continuous Deployment.
- [x] Connect real-time Google Sheets Order & Lead Database (`PersonaLabs Academy — Orders DB`) with automatic Google Drive `DriveApp.addViewer` email whitelisting.
- [x] Wire Dual Order Bumps (`Uncensored Content Hack` + `500+ Viral Reel Hooks & Auto-DM Pack`), unguessable VIP URLs (`uncensored-vip-8f92a1c4.html` & `hooks-vip-3d7e91b2.html`), and 4-combination 1-Click Post-Purchase Upgrades (`?upgrade=bump1` & `?upgrade=bump2`).
- [x] Remove `INVISION ACADEMY` watermarks and burn **Style 1 English Captions** across all 23 course videos while preserving 100% original audio quality.
- [x] Create approved consistent AI Influencer persona & render 3 ready-to-post 9:16 Video Ads (`ads-ready/`).
- [ ] Create dedicated `PersonaLabs Academy` Gmail account, upload the 3 Google Drive folders, and paste the Folder IDs into Google Apps Script + folder links into `index.html` & `course-vault/index.html`.
- [ ] Switch `upiConfig.enabled = true` (or Razorpay live key) in `app.js` for real instant payments.

---

## 🎬 Phase 3: The 3 High-Converting Video Ad Scripts (2 Currency Variants: India `INR` + Global `USD`)

All 3 ads are rendered in **two dedicated currency variants (`6` ready-to-post `1080x1920 @ 30fps` `.mp4` videos in total)** inside [`ads-ready/`](../ads-ready):
- 🇮🇳 **India Variant ([`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads))**: Uses **only `₹249` (`Reg. ₹1,999`)** and `₹15,000` in voiceover, captions, and CTA end-card.
- 🌍 **Global Variant ([`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads))**: Uses **only `$9` (`Reg. $49`)** and `$500` in voiceover, captions, and CTA end-card.

### 🔥 Video Ad #1: "The Curiosity Reveal" (Cold Traffic & Viral Organic Reels)
- **India File:** `ads-ready/01-India-INR-Ads/Ad-01-Curiosity-Reveal-INR-9x16.mp4`
- **Global File:** `ads-ready/02-Global-USD-Ads/Ad-01-Curiosity-Reveal-USD-9x16.mp4`
- **Top Hook Banner:** `WAIT... SHE DOESN'T ACTUALLY EXIST?!`
- **Scene-by-Scene Script:**
  - **0:00 – 0:04 (Hook):** *"Wait… she doesn't actually exist. Every single photo and Reel you're looking at is 100% AI-generated."*
  - **0:04 – 0:09 (Problem / Agitation):** *"While most people waste hours scrolling Instagram, smart creators are building faceless AI influencers with locked facial consistency."*
  - **0:09 – 0:14 (Solution / Proof):** *"No camera, no studio, and no expensive models. Just copy-paste our exact prompts and free AI tools in 15 minutes a day."*
  - **0:14 – End (Call to Action):**
    - **India (`INR`):** *"Visit PersonaLabs.store right now to grab the 23-video AI Influencer Launch Kit for just ₹249!"*
    - **Global (`USD`):** *"Visit PersonaLabs.store right now to grab the 23-video AI Influencer Launch Kit for just $9!"*

---

### 💰 Video Ad #2: "The Proof & Monetization Breakdown" (Side-Hustle & Business Angle)
- **India File:** `ads-ready/01-India-INR-Ads/Ad-02-Proof-Monetization-INR-9x16.mp4`
- **Global File:** `ads-ready/02-Global-USD-Ads/Ad-02-Proof-Monetization-USD-9x16.mp4`
- **Top Hook Banner:** `HOW AI INFLUENCERS MONETIZE 24/7`
- **Scene-by-Scene Script:**
  - **0:00 – 0:04 (Hook):**
    - **India (`INR`):** *"Stop paying ₹15,000 for product shoots or showing your own face on camera to grow on Instagram."*
    - **Global (`USD`):** *"Stop paying $500 for product shoots or showing your own face on camera to grow on Instagram."*
  - **0:04 – 0:09 (Mechanism):** *"Look at how our AI models keep the exact same face across luxury resorts, gym selfies, cafes, and viral evening Reels."*
  - **0:09 – 0:14 (Value Stack):** *"Inside PersonaLabs Academy, you get 23 step-by-step video lessons, 250+ face-lock prompts, and automated DM funnels."*
  - **0:14 – End (Call to Action):**
    - **India (`INR`):** *"Unlock instant lifetime access today for just ₹249 at PersonaLabs.store and launch your AI influencer tonight!"*
    - **Global (`USD`):** *"Unlock instant lifetime access today for just $9 at PersonaLabs.store and launch your AI influencer tonight!"*

---

### ⚡ Video Ad #3: "The 5-Day Zero-to-Viral System" (Objection Crusher & Retargeting)
- **India File:** `ads-ready/01-India-INR-Ads/Ad-03-No-Laptop-5Day-System-INR-9x16.mp4`
- **Global File:** `ads-ready/02-Global-USD-Ads/Ad-03-No-Laptop-5Day-System-USD-9x16.mp4`
- **Top Hook Banner:** `BUILD YOUR AI INFLUENCER IN 5 DAYS`
- **Scene-by-Scene Script:**
  - **0:00 – 0:04 (Hook):** *"Think you need an expensive gaming PC or coding skills to create an ultra-realistic AI influencer? Watch this."*
  - **0:04 – 0:09 (5-Day Walkthrough):** *"In just 5 days, we walk you click-by-click from generating her face to animating viral vertical Reels using free browser tools."*
  - **0:09 – 0:14 (VIP Add-Ons Highlight):** *"Plus, you can unlock our private FaceFusion pro workflow and 500 viral Reel hooks that stop the scroll in seconds."*
  - **0:14 – End (Call to Action):**
    - **India (`INR`):** *"Don't miss the ₹249 flash sale. Tap below to get instant access to all 23 English-captioned videos right now!"*
    - **Global (`USD`):** *"Don't miss the $9 flash sale. Tap below to get instant access to all 23 English-captioned videos right now!"*

---

## 📅 30-Day Viral Instagram Reels & Revenue Content Calendar

| Day | Reel Hook (On-Screen Text First 2.5s) | Visual Concept | Caption CTA Keyword | Target Funnel Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | *"She doesn't exist… yet she makes ₹3.8 Lakhs/month on Instagram 🤯"* | 3-panel split of your AI Influencer (`demo.mp4` saree reel + luxury cafe + streetwear) | Comment **"AI"** for the ₹249 Launch Kit | Drive first 1,000 Bio/DM clicks |
| **Day 2** | *"Stop paying models ₹15,000 per shoot. Do this in 45 seconds for FREE 👇"* | Fast screen-recording of Whisk + Flow generating consistent saree portrait | Comment **"MODEL"** to get the step-by-step videos | Showcase free-tool simplicity |
| **Day 3** | *"POV: You built a 24/7 AI Influencer from your bedroom at 2 AM 💻✨"* | Before/After transformation from prompt to moving 9:16 video reel | Comment **"REEL"** for the full 23-video course | Impulse sales + Order Bump #2 |
| **Day 4** | *"How top AI creators bypass AI restrictions safely (Nobody talks about this) 🤫"* | High-curiosity editorial transition teasing the FaceFusion workflow | Comment **"HACK"** for the link | High conversion on **Order Bump #1 (+₹249)** |
| **Day 5** | *"I asked AI to create India's next viral fashion icon… rate her 1–10 👀"* | 4 ultra-realistic ethnic + western transitions on trending audio | Comment **"ICON"** to build your own | Viral reach + comment velocity |
| **Day 6** | *"How much do AI Influencers actually charge for 1 Story + 1 Reel? 💰"* | Breakdown overlay showing $500–$2,000 brand deal economics + calculator | Comment **"EARN"** for the blueprint | Attract business/side-hustle buyers |
| **Day 7** | *"3 Free AI Tools that are 100% legal to monetize in 2026 ✅"* | Quick showcase of Whisk, Kie.ai, and SJinn.ai | Comment **"TOOLS"** for my exact prompts | High save-to-view ratio (Algorithm boost) |
| **Day 8** | *"Why 99% of AI accounts fail (They make this 1 face-swap mistake) ❌"* | Side-by-side blurry swap vs crisp FaceFusion output setting (Video 13) | Comment **"SWAP"** for the fix | Establish authority & technical quality |
| **Day 9** | *"Copy-paste this exact Nano Banana prompt to lock your AI model's face 🔒"* | Screen capture of prompt + 4 identical faces in different locations | Comment **"PROMPT"** for 250+ prompts | High DM automation volume |
| **Day 10** | *"From 0 to 50K followers in 30 days with Trial Reels (Full Strategy) 📈"* | Instagram insights dashboard + Trial Reels toggle walkthrough | Comment **"GROW"** for the system | Convert skeptical creators |
| **Day 11** | *"She never sleeps, never ages, and posts 3 Reels a day automatically 🤖"* | Fast-paced montage of travel, gym, ethnic, and luxury lifestyle clips | Comment **"AUTO"** for the 5-day launch kit | Push All-Access VIP Bundle (`₹647`) |
| **Day 12** | *"How to turn 1 Pinterest photo into a completely unique AI Influencer 🎨"* | Step-by-step preview of Lesson P3 (Pinterest -> Whisk -> Flow) | Comment **"CREATE"** for all 23 lessons | Direct product demonstration |
| **Day 13** | *"500+ Viral Reel Hooks that force people to stop scrolling in 1.5s 🔥"* | Rapid-fire text hooks flashing over aesthetic AI model b-roll | Comment **"HOOKS"** to grab the pack | Boost **Order Bump #2 (+₹149)** attach rate |
| **Day 14** | *"Week 2 Student Results & Q&A: Can you really do this without a gaming PC?"* | Screen recording showing cloud/browser tools running smoothly | Comment **"START"** before ₹249 flash ends | Overcome "I don't have a strong PC" objection |
| **Day 15–20** | **Scale Winners (2 Reels/Day):** Remix the top 3 highest-comment Reels from Days 1–14 with new trending audio + run WhatsApp follow-up on all `INITIATED_CHECKOUT` leads in Google Sheets. | | Comment **"AI"** | Scale daily volume to 15–30 sales/day |
| **Day 21–25** | **Post-Purchase Upgrade Push:** Message all Basic Pack buyers (`b1=0` or `b2=0`) on WhatsApp/Email with their 1-click upgrade links (`?upgrade=bump1` & `?upgrade=bump2`). | | Direct WhatsApp / Email | Collect pure-profit add-on upgrades (`+₹249` / `+₹149`) |
| **Day 26–30** | **Meta Ads Retargeting & Lookalike Scale:** Launch ₹500/day Instagram Reel Ad using the #1 organic Reel (>5% comment rate) driving directly to `https://personalabs.store`. | | Direct `"Learn More"` CTA | Scale to ₹1.5L–₹3L/month automated run-rate |

