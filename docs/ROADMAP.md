# 🚀 PersonaLabs Academy (`personalabs.store`) — Master Vision, Roadmap & Day-Wise Execution Playbook (`ROADMAP.md`)

Single source of truth combining our **Product Vision**, **Completed Engineering Milestones**, **Day-by-Day Execution Calendar**, **Meta Ads & ManyChat Playbook**, and **30-Day Viral Reels Calendar**. Last updated `2026-10-11`.

```mermaid
flowchart LR
    A["Day 1 (Oct 11): Udyam + v2.8.0 Live + Razorpay & PayPal Live ✅"] --> B["Day 1–2 (Oct 11–12): 3 Drive Folders + PayPal Email Swap + IG Page"]
    B --> C["Day 3 (Oct 13): ManyChat Auto-DM + Competitor Spy + Vercel DNS"]
    C --> D["Day 4–7 (Oct 14–17): Launch ₹500/day India Meta Ads + WhatsApp Recovery"]
    D --> E["Day 8–30 (Oct 18+): Scale India + Launch US/UK/CA/AU ($9 USD) Campaign"]
```

---

## 🗓️ 1. Date-Wise & Task-Wise Master Execution Calendar (Done + Next)

Every past and upcoming action planned day-by-day. **Who** indicates whether it is an owner action (**You** — your accounts/dashboards) or code/automation (**Agent**).

| Day / Date | Phase & Focus | Who | Exact Tasks (✅ Completed vs. 🎯 To Do Next) | Status / Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1 — Part A<br>(Today, Oct 11)** | **Storefront, Vault, Captioned Videos, 6 Ads & Live Gateways (`INR` + `USD`)** | Agent + You | 1. ✅ Register Udyam MSME (`UDYAM-UP-43-0208040` — `PersonaLabs Academy`)<br>2. ✅ Deploy `v2.8.0` on `https://personalabs.store` (`app.js?v=14`)<br>3. ✅ Connect 20-column Google Sheets Orders & Leads DB + `DriveApp.addViewer` code<br>4. ✅ Activate **Live Razorpay (`rzp_live_TmX62nNGuBaTUc`)** for India (`INR`)<br>5. ✅ Activate **Live PayPal (`BAARfEN6...`)** for International (`USD`)<br>6. ✅ Add 14-country Phone Validation, Strict Email Typo Validation & 2-Tier Discount Ladder (`₹249 → ₹499` still `75% OFF ₹1,999`)<br>7. ✅ Remove watermarks & burn English captions across all **23 Course Videos** (`videos-captioned/`)<br>8. ✅ Render **6 Ready-to-Post 9:16 Video Ads** (`3` India `INR ₹249` + `3` Global `USD $9` in `ads-ready/`) | ✅ **100% Done & Live** |
| **Day 1 — Part B<br>(Tonight, Oct 11)** | **Finish `@personalabsacademy` IG Profile + 3 Restricted Google Drive Folders + Brand Orders DB** | **You + Agent** | 1. ✅ Create official Instagram account **`@personalabsacademy`** (`PersonaLabs Academy`) & use the clean 48h Warmup "Comment-to-DM" Bio<br>2. ✅ Upload the 3 Restricted folders under **`personalabsacademy@gmail.com`** (`01-Core`: `1QaLzv...`, `02-NSFW`: `10HGXW...`, `03-Hooks`: `1IId4d...`)<br>3. ✅ Create dedicated `PersonaLabs Academy — Orders DB` Sheet (`1Sy8fy...`) & deploy live Apps Script Web App (`AKfycbzxKG...`) under `personalabsacademy@gmail.com` with `DriveApp.addViewer` auto-whitelisting (`v2.8.1`) | ✅ **100% Done & Verified** |
| **Day 2<br>(Mon, Oct 12)** | **PayPal Post-Review Email Swap + ManyChat Auto-DM (`₹0` Ad Spend) + First 2 Reels** | **You** | 1. 🎯 **Once PayPal's yellow review banner clears (~24h):**<br>&nbsp;&nbsp;• Close the unused `personalabsacademy@gmail.com` PayPal account (*Settings → Close account*) to free the email<br>&nbsp;&nbsp;• On your verified PayPal Business account, add `personalabsacademy@gmail.com` as **Primary Email**<br>&nbsp;&nbsp;• In *Business Information*, confirm **Business Name** = `PersonaLabs Academy` & **Customer Service Email** = `personalabsacademy@gmail.com`<br>2. 🎯 Connect **ManyChat (Free)** to `@personalabsacademy` to auto-DM `https://personalabs.store` on keywords `AI`, `LAUNCH`, `MODEL`, `REEL`<br>3. 🎯 Post **Day 1 Reel** + **1 Trial Reel** from the 30-Day Calendar below | ⬜ **Up Next (35 Mins)** |
| **Day 3<br>(Tue, Oct 13 — After 48h IG Warmup)** | **Add `https://personalabs.store` to IG Bio/Links + Competitor Spy + Vercel Free DNS Switch** | **You** | 1. 🎯 **48h Instagram Warmup Complete — Add Website Link & Update Bio on `@personalabsacademy`:**<br>&nbsp;&nbsp;• On the Instagram mobile app → **Edit profile → Links → Add external link** → enter **`https://personalabs.store`**<br>&nbsp;&nbsp;• Update Bio last line to include `personalabs.store`<br>2. 🎯 Open [Meta Ad Library](https://www.facebook.com/ads/library) (`India`, `All Ads`) → search `earlycaves.com` & `AI Influencer` → note top 3 longest-running ads (2+ weeks)<br>3. 🎯 **Switch static host from Netlify Free (300-credit cap) to Vercel Free (100 deploys/day)** before our next code edit: Import private repo `wandringspirit/ai-influencer-course-website` on `vercel.com` & point Namecheap DNS (`A @` → `76.76.21.21`, `CNAME www` → `cname.vercel-dns.com`)<br>4. 🎯 Post **Day 2 Reel** + **1 Trial Reel** | ⬜ **Scheduled (30 Mins)** |
| **Day 4<br>(Wed, Oct 14)** | **Meta Pixel Setup + Launch Campaign #1 (India `₹500–₹800/day`)** | **You + Agent** | 1. 🎯 Create **Meta Pixel** in Meta Events Manager → send 15-digit Pixel ID to Agent to wire into `META_PIXEL_CONFIG.pixelId` in [`app.js`](../app.js)<br>2. 🎯 Launch **Campaign #1 (India Only)** in Meta Ads Manager (`Sales → Purchase`, `₹500–₹800/day`, IG Reels/Stories/Feed) uploading the 3 India `INR` videos from [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads)<br>3. 🎯 Post **Day 3 Reel** + **1 Trial Reel** | ⬜ **First Paid Traffic Live** |
| **Days 5–6<br>(Thu–Fri, Oct 15–16)** | **48-Hour Ad Testing, CTR Pruning & 15-Min WhatsApp Cart Recovery** | **You** | 1. 🎯 Let India ads run 48 hours untouched; keep videos with **Outbound CTR `> 1.2%`**, pause any video `< 0.8%` after `₹250` spent<br>2. 🎯 Check `PersonaLabs Academy — Orders DB` Google Sheet daily for yellow `INITIATED_CHECKOUT` rows without a green `PAID_SUCCESS` row and send the WhatsApp recovery message ([`OUTREACH.md`](OUTREACH.md) §2) with code `RIYA10`<br>3. 🎯 Post **Day 4 & Day 5 Reels** | ⬜ **Identify #1 Winning Ad** |
| **Day 7<br>(Sat, Oct 17)** | **Scale India Winning Ad Set + 48h Post-Purchase Add-On Upsells** | **You** | 1. 🎯 Increase daily budget on winning India Ad Set by **+25%** (`₹600` → `₹800/day`) when Cost Per Purchase is `< ₹160`<br>2. 🎯 Message Basic Pack buyers (`b1=0` or `b2=0`) 48h after purchase with their 1-click upgrade links (`https://personalabs.store/?upgrade=bump1` & `/?upgrade=bump2`, [`OUTREACH.md`](OUTREACH.md) §3)<br>3. 🎯 Post **Day 6 Reel** | ⬜ **Daily `₹ INR` Profit + Upsells** |
| **Days 8–14<br>(Oct 18–24)** | **Launch Campaign #2: Tier-1 International (`US / UK / CA / AU` in `$ USD`)** | **You** | 1. 🎯 Create **separate Campaign #2** in Meta Ads Manager targeting **`United States, United Kingdom, Canada, Australia`** (`Exclude India`, `₹1,200–₹2,000/day`)<br>2. 🎯 Upload the 3 Global `USD` video ads from [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads) (`$9` CTA)<br>3. 🎯 Collect **`$9–$20 USD` (`₹750–₹1,680 INR`)** per sale via Live PayPal while posting **Day 7–13 Reels** | ⬜ **Global `₹ INR` + `$ USD` Scale** |
| **Days 15–30<br>(Oct 25 – Nov 9)** | **Remix Top Viral Reels, Lookalike Audiences & Scale to `₹1.5L–₹3L/mo`** | **You** | 1. 🎯 Follow **Day 14–30** of the Content Calendar below (2 Reels/day remixing top comment-velocity hooks)<br>2. 🎯 Scale winning India & Tier-1 Ad Sets by +25% every 48 hours and create a 1% Lookalike Audience once 100 `Purchase` events fire | ⬜ **Automated `₹1.5L–₹3L/mo` Run-Rate** |

---

## ✅ 2. Everything Completed & Live So Far (`v2.8.0`)

- [x] **Legal & Brand Privacy:** Registered Udyam MSME Certificate (`UDYAM-UP-43-0208040`) under **`PersonaLabs Academy`**; updated all storefront, legal modal, AI assistant, and downloadable `.txt` receipt emails to **`personalabsacademy@gmail.com`**.
- [x] **Storefront & Conversion UX ([`index.html`](../index.html), [`styles.css`](../styles.css), [`app.js`](../app.js)):**
  - Geo-IP currency lock (`INR` for India / `USD` for Global).
  - **"Nothing to lose. Everything to gain."** 100% 7-Day Money-Back Guarantee banner right below the Hero description.
  - **2-Tier Discount Ladder (`Option A1`):** When the 10-minute `₹249` (`$9`) flash timer hits `00:00`, the price transitions to `₹499` (`$19`) while keeping **`₹1,999` (`$79`)** crossed out (`SAVE 75% OFF ₹1,999 — LAUNCH OFFER`).
  - **Country-Aware Phone & Strict Email Validation:** `<select id="phone-country-select">` (`14` country rules synced to IP country) + RFC email validation with `@gamil.com` / `@gmial.com` typo warnings and disposable domain blocking.
- [x] **Live Payment Gateways (Zero Bypass / Verified TxId Required):**
  - **India (`INR`):** Live Razorpay Standard Checkout (`rzp_live_TmX62nNGuBaTUc`) with UPI (`GPay / PhonePe / Paytm`), QR, Cards, and Netbanking + order `notes`.
  - **International (`USD`):** Live PayPal Smart Buttons SDK (`BAARfEN6AEZqn7tB4CWb08mUBhJqBYzxwPkmMnxJNkQ77mGxuYUiisrNiiYhtg75Gg12nHMXKAS38v_p1E`) with `NO_SHIPPING`, `brand_name: 'PersonaLabs Academy'`, and `soft_descriptor: 'PERSONALABS'`.
- [x] **Real-Time Google Sheets DB & Private Drive Automation ([`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md)):**
  - Logs `INITIATED_CHECKOUT` (yellow lead row) and `PAID_SUCCESS` (green verified row) across 20 columns and triggers `DriveApp.addViewer(buyerEmail)` for purchased folders.
- [x] **Member Vault & Cryptographic VIP Add-On Protection ([`course-vault/`](../course-vault)):**
  - Interactive 5-Day / 18-Lesson Portal (`course-vault/index.html`), 250+ Prompt Bible (`character-dna-prompt-bible.html`), and unguessable VIP guides (`uncensored-vip-8f92a1c4.html` & `hooks-vip-3d7e91b2.html`) protected by FNV-1a (`vt1`/`vt2`) signatures + server-side Google Sheet verification + 4-combination 1-click upgrades (`?upgrade=bump1` & `?upgrade=bump2`).
- [x] **23 Captioned Course Videos & 6 Regional Video Ads:**
  - Stripped `INVISION ACADEMY` watermarks and burned Style 1 English Captions across all 23 course videos (`videos-captioned/`).
  - Rendered 3 India `INR ₹249` ads ([`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads)) and 3 Global `USD $9` ads ([`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads)).
- [x] **Prepared Unlimited Free Hosting Config ([`vercel.json`](../vercel.json)):**
  - Configured zero-build static headers + `X-Robots-Tag: noindex, nofollow` on `/course-vault/*` for 3-click migration from Netlify Free (300-credit cap) to Vercel Free (`100 deploys/day`, private GitHub repo preserved).

---

## 🎯 3. Step-by-Step Instructions for Your Next Actions

### Action A (Day 1 Tonight): Upload 3 Restricted Google Drive Folders under `personalabsacademy@gmail.com`
> [!IMPORTANT]
> **Privacy Rule:** Never share Google Drive folders from your personal Gmail account because Google Drive's *Details → Owner* panel shows the owner's email/name to viewers. Always use **`personalabsacademy@gmail.com`**.

1. Log into Google Drive using **`personalabsacademy@gmail.com`** and upload these 3 folders from `C:\Projects\ai-influencer-course-website\videos-captioned\`:
   - **Folder 1 (`01-Core-Course-Videos`)**: 19 Core Videos + `Bonus.docx` + `readme.docx` + `250-AI-Character-DNA-Prompt-Bible.html`.
   - **Folder 2 (`02-Uncensored-NSFW-Addon-Videos`)**: 4 Exclusive NSFW FaceSwap Videos (`14, 15, 16, 17`) + `Uncensored-Content-Hack-VIP-Guide.html`.
   - **Folder 3 (`03-500-Viral-Hooks-And-Prompts-Pack`)**: `500-Viral-Reel-Hooks-And-AutoDM-Pack.html` + `250-AI-Character-DNA-Prompt-Bible.html`.
2. Keep all 3 folders set to **`Restricted (Only people added can open)`**.
3. Copy the Folder ID from each folder's URL (`https://drive.google.com/drive/folders/FOLDER_ID_HERE`) and paste them into `CORE_FOLDER_ID`, `NSFW_FOLDER_ID`, and `HOOKS_FOLDER_ID` in your Google Sheet's **Extensions → Apps Script** ([`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md)), then click **Deploy → Manage deployments → Edit (✏️) → Version: New version → Deploy**.

---

### Action B (Day 2): Set PayPal Business Name & `personalabsacademy@gmail.com` as Primary Email (Once 24h Udyam Review Finishes)
While PayPal shows the yellow *"Feel free to explore your account while we review your info"* banner, profile/email edits are temporarily locked. As soon as PayPal emails you that the review is complete:
1. **Free up `personalabsacademy@gmail.com`:** Log into the unused `personalabsacademy@gmail.com` PayPal account we started earlier → go to **Settings (⚙️) → Account Options → Close your account**.
2. **Add to your verified PayPal Business account:** Log into your main verified PayPal Business account → **Account Settings → Account Owner Information → Email address → Add New** → add **`personalabsacademy@gmail.com`**, verify the link in Gmail, and make it **Primary**.
3. **Confirm Receipt Display Name:** Go to **Account Settings → Business Profile → Business Information** and confirm **Business Name** is **`PersonaLabs Academy`**, **Credit Card Statement Name** is **`PERSONALABS`**, and **Customer Service Email** is **`personalabsacademy@gmail.com`**.

---

### Action C (Day 3 / Before Next Website Code Edit): Switch Static Hosting from Netlify Free to Vercel Free
`v2.8.0` is already live on `https://personalabs.store` and kept online by Netlify's 30 operational credits. Before we push any new website code edits:
1. Go to **[vercel.com](https://vercel.com)** → Sign in with **GitHub (`wandringspirit`)** → **Add New → Project** → Import private repository `wandringspirit/ai-influencer-course-website` → Click **Deploy** ([`vercel.json`](../vercel.json) configures everything automatically).
2. In Vercel **Settings → Domains**, add **`personalabs.store`**.
3. In **Namecheap → Domain List → `personalabs.store` → Manage → Advanced DNS**, update:
   - **`A Record` (`@`):** `76.76.21.21` (replaces Netlify's `75.2.60.5`)
   - **`CNAME Record` (`www`):** `cname.vercel-dns.com`

---

### Action D (Day 2–3): The "₹0 Ad Spend" AI Persona Instagram + ManyChat Auto-DM Engine
1. **Create Your AI Persona IG Profile (15 Mins):**
   - Switch to **Instagram Professional Account → Creator** (free, required for ManyChat).
   - Bio:
     ```text
     ✨ Digital Girl Living in 4K • 100% AI-Created 🤖
     📍 Mumbai • Bali • Monaco
     👇 Build your own AI Influencer in 5 Days (88% OFF today):
     🔗 personalabs.store
     ```
2. **Connect Free ManyChat Auto-DM (`manychat.com`):**
   - Trigger when user comments on any Reel with: `AI`, `LAUNCH`, `MODEL`, `REEL`, `HACK`, `LINK`, `PROMPT`.
   - Use the exact Public Comment Auto-Replies and Automated DM scripts in [`docs/OUTREACH.md`](OUTREACH.md).
3. **Spy on Competitor Ads Before Launching Paid Traffic (`facebook.com/ads/library`):**
   - Set Location = `India`, Category = `All Ads`, search `earlycaves.com` and `AI Influencer`, and note the hooks running `2+ weeks`.

---

### Action E (Day 4 & Day 8): Meta Ads Campaign #1 (`India INR`) & Campaign #2 (`Tier-1 USD`)

> [!CAUTION]
> **GOLDEN RULE — Never Put India and US/UK/CA/AU in the Same Ad Set!**
> Always run **Campaign #1 = India Only (`₹ INR`)** using [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads) and **Campaign #2 = Tier-1 Countries (`US + UK + Canada + Australia` in `$ USD`)** using [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads).

| Setting / Metric | 🇮🇳 Campaign #1: India Only (Launch Day 4) | 🌎 Campaign #2: Tier-1 `US, UK, CA, AU` (Launch Day 8) |
| :--- | :--- | :--- |
| **Video Ad Creatives** | [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads) (`₹249` CTA) | [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads) (`$9` CTA) |
| **Campaign Objective** | `Sales` → Website → Event: **`Purchase`** | `Sales` → Website → Event: **`Purchase`** |
| **Locations & Age** | `India`, Age `18–36` | `United States, United Kingdom, Canada, Australia` (*Exclude India*), Age `18–40` |
| **Placements** | Manual: **IG Reels, IG Stories, IG Feed, FB Reels** only | Manual: **IG Reels, IG Stories, IG Feed, FB Reels** only |
| **Starting Daily Budget** | **`₹500 – ₹800 / day`** | **`₹1,200 – ₹2,000 / day`** |
| **Checkout Price & Gateway** | `₹249` Base / `₹647` Full Bundle (**Razorpay Live**) | `$9` Base / `$20` Full Bundle (**PayPal Live**) |
| **Target Cost Per Purchase** | `₹90 – ₹160` (`2.5x+ ROAS` with order bumps) | `$5 – $9` (`₹420 – ₹760`) |

#### Ready-to-Post Video Ad Scripts (Already Rendered in `ads-ready/`):
1. **🔥 Video Ad #1 (`Ad-01-Curiosity-Reveal-*-9x16.mp4`):**
   - **0:00–0:04:** *"Wait… she doesn't actually exist. Every single photo and Reel you're looking at is 100% AI-generated."*
   - **0:04–0:09:** *"While most people waste hours scrolling Instagram, smart creators are building faceless AI influencers with locked facial consistency."*
   - **0:09–0:14:** *"No camera, no studio, and no expensive models. Just copy-paste our exact prompts and free AI tools in 15 minutes a day."*
   - **0:14–End:** *"Visit PersonaLabs.store right now to grab the 23-video AI Influencer Launch Kit for just ₹249 [or $9]!"*
2. **💰 Video Ad #2 (`Ad-02-Proof-Monetization-*-9x16.mp4`):**
   - **0:00–0:04:** *"Stop paying ₹15,000 [or $500] for product shoots or showing your own face on camera to grow on Instagram."*
   - **0:04–0:09:** *"Look at how our AI models keep the exact same face across luxury resorts, gym selfies, cafes, and viral evening Reels."*
   - **0:09–0:14:** *"Inside PersonaLabs Academy, you get 23 step-by-step video lessons, 250+ face-lock prompts, and automated DM funnels."*
   - **0:14–End:** *"Unlock instant lifetime access today for just ₹249 [or $9] at PersonaLabs.store and launch your AI influencer tonight!"*
3. **⚡ Video Ad #3 (`Ad-03-No-Laptop-5Day-System-*-9x16.mp4`):**
   - **0:00–0:04:** *"Think you need an expensive gaming PC or coding skills to create an ultra-realistic AI influencer? Watch this."*
   - **0:04–0:09:** *"In just 5 days, we walk you click-by-click from generating her face to animating viral vertical Reels using free browser tools."*
   - **0:09–0:14:** *"Plus, you can unlock our private FaceFusion pro workflow and 500 viral Reel hooks that stop the scroll in seconds."*
   - **0:14–End:** *"Don't miss the ₹249 [or $9] flash sale. Tap below to get instant access to all 23 English-captioned videos right now!"*

#### Copy-Paste Primary Ad Text (Meta Ads Manager):
```text
Still filming Reels with your own camera in 2026? 🤖✨

Top virtual creator pages are pulling 100K–1M+ views and automated daily income using 100% AI-generated influencers — built entirely from a smartphone or browser with free AI tools.

Inside the 5-Day AI Influencer Launch Kit (88% OFF Flash Sale: ₹249 / $9), you get:
✅ 23 Step-by-Step HD Video Lessons (With English Captions)
✅ The 100% Face-Lock Workflow (Same exact face across every photo & outfit)
✅ 250+ Copy-Paste Character DNA & Luxury Scene Prompts
✅ Viral 9:16 AI Reels & Automated ManyChat DM Blueprint
✅ Instant On-Screen Vault Access + 100% 7-Day Money-Back Guarantee

⚠️ 88% OFF Flash Offer expires when the timer hits 00:00.
👇 Tap "Learn More" to unlock your Vault instantly at personalabs.store!
```

---

## 📅 4. 30-Day Viral Instagram Reels & Revenue Content Calendar

| Day | Reel Hook (On-Screen Text First 2.5s) | Visual Concept | Caption CTA Keyword | Target Funnel Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1 (Oct 12)** | *"She doesn't exist… yet she makes ₹3.8 Lakhs/month on Instagram 🤯"* | 3-panel split of your AI Influencer (`demo.mp4` saree reel + luxury cafe + streetwear) | Comment **"AI"** for the ₹249 Launch Kit | Drive first 1,000 Bio/DM clicks |
| **Day 2 (Oct 13)** | *"Stop paying models ₹15,000 per shoot. Do this in 45 seconds for FREE 👇"* | Fast screen-recording of Whisk + Flow generating consistent saree portrait | Comment **"MODEL"** to get the step-by-step videos | Showcase free-tool simplicity |
| **Day 3 (Oct 14)** | *"POV: You built a 24/7 AI Influencer from your bedroom at 2 AM 💻✨"* | Before/After transformation from prompt to moving 9:16 video reel | Comment **"REEL"** for the full 23-video course | Impulse sales + Order Bump #2 |
| **Day 4 (Oct 15)** | *"How top AI creators bypass AI restrictions safely (Nobody talks about this) 🤫"* | High-curiosity editorial transition teasing the FaceFusion workflow | Comment **"HACK"** for the link | High conversion on **Order Bump #1 (+₹249 / +$6)** |
| **Day 5 (Oct 16)** | *"I asked AI to create India's next viral fashion icon… rate her 1–10 👀"* | 4 ultra-realistic ethnic + western transitions on trending audio | Comment **"ICON"** to build your own | Viral reach + comment velocity |
| **Day 6 (Oct 17)** | *"How much do AI Influencers actually charge for 1 Story + 1 Reel? 💰"* | Breakdown overlay showing $500–$2,000 brand deal economics + calculator | Comment **"EARN"** for the blueprint | Attract business/side-hustle buyers |
| **Day 7 (Oct 18)** | *"3 Free AI Tools that are 100% legal to monetize in 2026 ✅"* | Quick showcase of Whisk, Kie.ai, and SJinn.ai | Comment **"TOOLS"** for my exact prompts | High save-to-view ratio (Algorithm boost) |
| **Day 8 (Oct 19)** | *"Why 99% of AI accounts fail (They make this 1 face-swap mistake) ❌"* | Side-by-side blurry swap vs crisp FaceFusion output setting (Video 13) | Comment **"SWAP"** for the fix | Establish authority & technical quality |
| **Day 9 (Oct 20)** | *"Copy-paste this exact Nano Banana prompt to lock your AI model's face 🔒"* | Screen capture of prompt + 4 identical faces in different locations | Comment **"PROMPT"** for 250+ prompts | High DM automation volume |
| **Day 10 (Oct 21)** | *"From 0 to 50K followers in 30 days with Trial Reels (Full Strategy) 📈"* | Instagram insights dashboard + Trial Reels toggle walkthrough | Comment **"GROW"** for the system | Convert skeptical creators |
| **Day 11 (Oct 22)** | *"She never sleeps, never ages, and posts 3 Reels a day automatically 🤖"* | Fast-paced montage of travel, gym, ethnic, and luxury lifestyle clips | Comment **"AUTO"** for the 5-day launch kit | Push All-Access VIP Bundle (`₹647` / `$20`) |
| **Day 12 (Oct 23)** | *"How to turn 1 Pinterest photo into a completely unique AI Influencer 🎨"* | Step-by-step preview of Lesson P3 (Pinterest -> Whisk -> Flow) | Comment **"CREATE"** for all 23 lessons | Direct product demonstration |
| **Day 13 (Oct 24)** | *"500+ Viral Reel Hooks that force people to stop scrolling in 1.5s 🔥"* | Rapid-fire text hooks flashing over aesthetic AI model b-roll | Comment **"HOOKS"** to grab the pack | Boost **Order Bump #2 (+₹149 / +$5)** attach rate |
| **Day 14 (Oct 25)** | *"Week 2 Student Results & Q&A: Can you really do this without a gaming PC?"* | Screen recording showing cloud/browser tools running smoothly | Comment **"START"** before ₹249 flash ends | Overcome "I don't have a strong PC" objection |
| **Days 15–20 (Oct 26–31)** | **Scale Winners (2 Reels/Day):** Remix the top 3 highest-comment Reels from Days 1–14 with new trending audio + run daily 15-min WhatsApp follow-up on all yellow `INITIATED_CHECKOUT` leads in Google Sheets. | | Comment **"AI"** | Scale daily volume to 15–30 sales/day |
| **Days 21–25 (Nov 1–5)** | **Post-Purchase Upgrade Push:** Message all Basic Pack buyers (`b1=0` or `b2=0`) on WhatsApp/Email with their 1-click upgrade links (`?upgrade=bump1` & `?upgrade=bump2`). | | Direct WhatsApp / Email | Collect pure-profit add-on upgrades (`+₹249` / `+₹149`) |
| **Days 26–30 (Nov 6–10)** | **Meta Ads Retargeting & 1% Lookalike Scale:** Launch retargeting + 1% Lookalike Ad Set using the #1 organic/paid Reel (`>1.5%` CTR) driving directly to `https://personalabs.store`. | | Direct `"Learn More"` CTA | Scale to `₹1.5L–₹3L/month` automated run-rate |
