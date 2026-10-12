# 🚀 PersonaLabs Academy (`personalabs.store`) — Master Vision, Roadmap & Day-Wise Execution Playbook (`ROADMAP.md`)

Single source of truth combining our **Product Vision**, **Completed Engineering Milestones**, **Day-by-Day Execution Calendar**, **Meta Ads & ManyChat Playbook**, and **30-Day Viral Reels Calendar**. Last updated `2026-10-12`.

```mermaid
flowchart LR
    A["Day 1 (Oct 11): Storefront + Vercel CDN + 3 Drive Folders + Pixel + Ad Spy ✅"] --> B["Day 2 (Today, Oct 12): Campaign #1 Live (₹500/day) + Automated Email Engine + PDF Receipt ✅"]
    B --> C["Days 3–4 (Oct 13–14): 48h Ad CTR Pruning & +25% Budget Scale 🎯"]
    C --> D["Days 5–7 (Oct 15–17): Launch Tier-1 ($9 USD) Campaign"]
    D --> E["Days 8–30 (Oct 18+): 1% Lookalikes & Scale to ₹1.5L–₹3L/mo"]
```

---

## 🗓️ 1. Date-Wise & Task-Wise Master Execution Calendar (Done + Next)

Every past and upcoming action planned day-by-day. **Who** indicates whether it is an owner action (**You**) or code/browser automation (**Agent**).

| Day / Date | Phase & Focus | Who | Exact Tasks (✅ Completed vs. 🔄 In Progress vs. 🎯 Next) | Status / Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1 — Part A<br>(Completed, Oct 11)** | **Storefront `v2.8.1`, Vault, Captioned Videos, 6 Ads & Live Gateways (`INR` + `USD`)** | Agent + You | 1. ✅ Register Udyam MSME (`UDYAM-UP-43-0208040` — `PersonaLabs Academy`)<br>2. ✅ Deploy `v2.8.1` (`₹249` India / `$9` Global Flash Offer) on `https://personalabs.store`<br>3. ✅ Activate **Live Razorpay (`rzp_live_TmX62nNGuBaTUc`)** for India (`INR`)<br>4. ✅ Activate **Live PayPal (`BAARfEN6...`)** for International (`USD`)<br>5. ✅ Add 14-country Phone Validation, Strict Email Typo Validation & 2-Tier Discount Ladder (`₹249 → ₹499` still `75% OFF ₹1,999`)<br>6. ✅ Remove watermarks & burn English captions across all **23 Course Videos** (`videos-captioned/`)<br>7. ✅ Render **6 Ready-to-Post 9:16 Video Ads** (`3` India `INR ₹249` + `3` Global `USD $9` in `ads-ready/`) | ✅ **100% Done & Live** |
| **Day 1 — Part B<br>(Completed, Oct 11)** | **3 Private Drive Folders + Brand Orders DB + Vercel CDN + 107-Ad Competitor Spy + 8K Avatar** | **You + Agent** | 1. ✅ Upload 3 Restricted Drive folders under **`personalabsacademy@gmail.com`** (`01-Core`: `1QaLzv...`, `02-NSFW`: `10HGXW...`, `03-Hooks`: `1IId4d...`)<br>2. ✅ Create dedicated `PersonaLabs Academy — Orders DB` Sheet (`1Sy8fy...`) & deploy live Apps Script Web App (`AKfycbzxKG...`) with `DriveApp.addViewer` auto-whitelisting<br>3. ✅ Migrate `personalabs.store` & `www.personalabs.store` from Netlify Free to **Vercel Global CDN (`216.198.79.1`)**<br>4. ✅ Create `@personalabsacademy` IG Creator profile + generate **8K Exact-Face Saree Profile Picture** ([`insta_dp_exact_face_1080x1080.jpg`](../assets/insta_dp_exact_face_1080x1080.jpg))<br>5. ✅ Automated **Meta Ad Library Competitor Spy Scan** across all 4 tabs (`107` ads scanned; extracted top 7 long-running winners) | ✅ **100% Done & Verified** |
| **Day 1 — Part C<br>(Completed, Oct 11)** | **Meta Ad Account + Meta Pixel (`1661173205598260`) + Published Campaign #1 (`India INR`)** | **Agent + You** | 1. ✅ Created **Ad Account (`PersonaLabs Academy Ads`, ID: `2218391099056783`, `Asia/Kolkata`, `INR`)** in Meta Business Suite (`1761523878300294`)<br>2. ✅ Created **Dataset / Meta Pixel (`PersonaLabs Academy Pixel`, ID: `1661173205598260`)**, linked to Ad Account `2218391099056783`, wired into [`app.js`](../app.js) & [`index.html`](../index.html), and deployed to Vercel<br>3. ✅ Cleaned `@personalabsacademy` IG bio + configured **ManyChat Auto-DM** flow<br>4. ✅ **PUBLISHED Campaign #1 (India Only)** in Meta Ads Manager (`IN - Sales - AI Influencer Launch Kit (INR)`) | ✅ **Campaign #1 Published** |
| **Day 2<br>(Today, Oct 12)** | **Campaign #1 Active (`₹500/day`) + Automated Email Recovery/Upsells + Printable PDF Receipt (`v2.9.0`)** | **You + Agent** | 1. ✅ Verified Campaign #1 is **🟢 Active** (`₹500.00/day` CBO, Opportunity Score `100`, IG Reels & Stories) — early telemetry: **`3.52%–5.56%` Link CTR**, **78 engagements**, **7 link clicks** on first `₹204.05` spend<br>2. ✅ Deployed **Google Apps Script Version 3** with 24/7 automated **25-Min Cart Recovery** (`sendAbandonedCartRecoveryEmails`) & **12-Hr Add-On Upsell** (`sendPostPurchaseAddonUpsellEmails`) triggers + CAN-SPAM anti-spam deliverability<br>3. ✅ Built instant (`<50ms`) printable **PDF Tax Invoice (`INR`) / Payment Receipt (`USD`, no GST)** at [`course-vault/receipt.html`](../course-vault/receipt.html)<br>4. ✅ Updated secret test route [`/kjboavhpoieabpraegnaln`](https://www.personalabs.store/kjboavhpoieabpraegnaln) to **₹1 INR / $1 USD** per item (`?v=21`)<br>5. 🎯 Let ads run untouched through tonight's `7:00 PM – 11:30 PM IST` peak buying window | 🟢 **Active Day 2 Delivery (`3.52%–5.56%` CTR)** |
| **Days 3–4<br>(Tue–Wed, Oct 13–14)** | **48-Hour Ad CTR Pruning & Self-Funded Budget Scaling (`+25%`)** | **You** | 1. 🎯 Keep ads with **Outbound CTR `> 1.2%`**; once profitable purchases come in (`CPA < ₹150`), scale daily budget by **+25%** every 48 hours (`₹500` → `₹625/day`) using course earnings<br>2. 🎯 Monitor automated `Automated Recovery Email Status` & `Automated Add-On Upsell Status` columns in `PersonaLabs Academy — Orders DB` | ⬜ **Identify & Scale #1 Winner** |
| **Days 5–7<br>(Thu–Sat, Oct 15–17)** | **Launch Campaign #2: Tier-1 International (`US / UK / CA / AU` in `$ USD`)** | **You + Agent** | 1. 🎯 Create **separate Campaign #2** in Meta Ads Manager targeting **`United States, United Kingdom, Canada, Australia`** (`Exclude India`, `₹1,200–₹2,000/day`)<br>2. 🎯 Upload the 3 Global `USD` video ads from [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads) (`$9` CTA)<br>3. 🎯 Collect **`$9–$23 USD` (`₹750–₹1,930 INR`)** per sale via Live PayPal | ⬜ **Global `₹ INR` + `$ USD` Scale** |
| **Days 8–30<br>(Oct 18 – Nov 9)** | **1% Lookalike Audiences & Scale to `₹1.5L–₹3L/mo`** | **You** | 1. 🎯 Follow the **30-Day Viral Reels Calendar** below + scale winning India & Tier-1 Ad Sets by +25% every 48 hours + launch 1% Lookalike Audience at 100 `Purchase` events | ⬜ **Automated `₹1.5L–₹3L/mo` Run-Rate** |

---

## ✅ 2. Everything Completed & Live So Far (`v2.9.0` — Updated Oct 12)

- [x] **Legal & Brand Privacy:** Registered Udyam MSME Certificate (`UDYAM-UP-43-0208040`) under **`PersonaLabs Academy`**; updated all storefront, legal modal, AI assistant, and receipt emails to **`personalabsacademy@gmail.com`**.
- [x] **Official Printable PDF Tax Invoice / Payment Receipt ([`course-vault/receipt.html`](../course-vault/receipt.html)):**
  - Instant (`<50ms`) A4 printable invoice/receipt preloaded via `<link rel="prefetch">`.
  - Automatically displays **`Tax Invoice`** + **`Digital GST / Processing: Included (₹0.00)`** for Indian (`INR`) orders and **`Payment Receipt`** + **`Digital Delivery & Processing: Included ($0.00)`** (zero GST) for International (`USD`) orders.
- [x] **Automated 24/7 Cart Recovery & Post-Purchase Add-On Upsell Email Engine (`Apps Script Version 3`):**
  - **25-Min Abandoned Cart Recovery (`sendAbandonedCartRecoveryEmails`):** Automatically emails `INITIATED_CHECKOUT` leads from `PersonaLabs Academy <personalabsacademy@gmail.com>` if they haven't bought after 25 minutes (automatically skips anyone who bought 5–20 mins later).
  - **12-Hr Post-Purchase Add-On Upsell (`sendPostPurchaseAddonUpsellEmails`):** Automatically emails buyers who missed Bump #1 or Bump #2 with 1-click upgrade links (`/?upgrade=bump1` and `/?upgrade=bump2`).
- [x] **Secret Live Payment Testing Route (`/kjboavhpoieabpraegnaln` — `₹1 INR / $1 USD`):**
  - Live at [`https://www.personalabs.store/kjboavhpoieabpraegnaln`](https://www.personalabs.store/kjboavhpoieabpraegnaln) (`?v=21`) with **₹1 INR** / **$1 USD** per item and a 1-click currency switcher.
- [x] **Storefront & Conversion UX ([`index.html`](../index.html), [`styles.css`](../styles.css), [`app.js`](../app.js)):**
  - Geo-IP currency lock (`INR ₹249` for India / `USD $9` for Global).
  - **"Nothing to lose. Everything to gain."** 100% 7-Day Money-Back Guarantee banner right below the Hero description.
  - **2-Tier Discount Ladder (`Option A1`):** When the 10-minute `₹249` (`$9`) flash timer hits `00:00`, the price transitions to `₹499` (`$19`) while keeping **`₹1,999` (`$79`)** crossed out (`SAVE 75% OFF ₹1,999 — LAUNCH OFFER`).
  - **Country-Aware Phone & Strict Email Validation:** `<select id="phone-country-select">` (`14` country rules synced to IP country) + RFC email validation with `@gamil.com` / `@gmial.com` typo warnings and disposable domain blocking.
- [x] **Live Payment Gateways (Zero Bypass / Verified TxId Required):**
  - **India (`INR`):** Live Razorpay Standard Checkout (`rzp_live_TmX62nNGuBaTUc`) with UPI (`GPay / PhonePe / Paytm`), QR, Cards, and Netbanking + order `notes`.
  - **International (`USD`):** Live PayPal Smart Buttons SDK (`BAARfEN6AEZqn7tB4CWb08mUBhJqBYzxwPkmMnxJNkQ77mGxuYUiisrNiiYhtg75Gg12nHMXKAS38v_p1E`) with `NO_SHIPPING`, `brand_name: 'PersonaLabs Academy'`, and `soft_descriptor: 'PERSONALABS'`.
- [x] **100% Brand-Owned Google Drive Folders & Orders DB Sheet (`personalabsacademy@gmail.com`):**
  - Uploaded all 3 Restricted folders (`01-Core`: `1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`, `02-NSFW`: `10HGXWcRMR898lbQnTX41G--fPLKoBOvW`, `03-Hooks`: `1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`).
  - Connected `PersonaLabs Academy — Orders DB` (`1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc` — 22 columns) + live Apps Script Web App (`AKfycbzxKG...`, Version 3) and verified end-to-end `DriveApp.addViewer` access granting.
- [x] **Migrated to Unlimited Free Hosting on Vercel Global Edge CDN (`216.198.79.1`):**
  - Connected private GitHub repository (`wandringspirit/ai-influencer-course-website`) to Vercel (`https://personalabs.store` & `https://www.personalabs.store` serving `v2.9.0` / `app.js?v=21` with zero credit limits).
- [x] **Live Meta Ad Account, Meta Pixel (`1661173205598260`) & Active Campaign #1 (`₹500/day` CBO):**
  - Created `PersonaLabs Academy Ads` (`ID: 2218391099056783`, `INR`, `Asia/Kolkata`) and `PersonaLabs Academy Pixel` (`ID: 1661173205598260`), linked them in Meta Business Suite, wired all 5 funnel conversion events, and launched Campaign #1 (`IN - Sales - AI Influencer Launch Kit (INR)`) achieving **`3.52%–5.56%` Link CTR**.
- [x] **23 Captioned Course Videos, 6 Regional Video Ads & 8K Saree Profile Pictures:**
  - Stripped `INVISION ACADEMY` watermarks and burned Style 1 English Captions across all 23 course videos (`videos-captioned/`).
  - Rendered 3 India `INR` ads ([`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads)) and 3 Global `USD $9` ads ([`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads)).
  - Generated 8K exact-face saree profile pictures ([`insta_dp_exact_face_1080x1080.jpg`](../assets/insta_dp_exact_face_1080x1080.jpg) & [`insta_saree_full_portrait_hd.jpg`](../assets/insta_saree_full_portrait_hd.jpg)).
- [x] **107-Ad Meta Ad Library Competitor Spy Scan Across All 4 Tabs:**
  - Extracted top 7 long-running India (`₹199–₹249`) & US (`$9`) winners and crafted 3 battle-tested Headlines + Primary Text Options A, B, and C below.

---

## 🎯 3. Step-by-Step Instructions for Remaining Actions

### ✅ Action A (Completed Day 1): 3 Restricted Google Drive Folders + Brand Orders DB under `personalabsacademy@gmail.com`
All 3 Restricted folders (`01-Core`, `02-NSFW`, `03-Hooks`) and the `PersonaLabs Academy — Orders DB` Google Sheet are live under `personalabsacademy@gmail.com` and connected to `https://personalabs.store` (`v2.8.1`).

---

### 🎯 Action B (Day 2): Set PayPal Business Name & `personalabsacademy@gmail.com` as Primary Email (Once 24h Udyam Review Finishes)
While PayPal shows the yellow *"Feel free to explore your account while we review your info"* banner, profile/email edits are temporarily locked. As soon as PayPal emails you that the review is complete:
1. **Free up `personalabsacademy@gmail.com`:** Log into the unused `personalabsacademy@gmail.com` PayPal account we started earlier → go to **Settings (⚙️) → Account Options → Close your account**.
2. **Add to your verified PayPal Business account:** Log into your main verified PayPal Business account → **Account Settings → Account Owner Information → Email address → Add New** → add **`personalabsacademy@gmail.com`**, verify the link in Gmail, and make it **Primary**.
3. **Confirm Receipt Display Name:** Go to **Account Settings → Business Profile → Business Information** and confirm **Business Name** is **`PersonaLabs Academy`**, **Credit Card Statement Name** is **`PERSONALABS`**, and **Customer Service Email** is **`personalabsacademy@gmail.com`**.

---

### ✅ Action C (Completed Day 1): Migrated Static Hosting from Netlify Free to Vercel Global CDN
`personalabs.store` (`A -> 216.198.79.1`) and `www.personalabs.store` (`CNAME -> 847062401d7e0c68.vercel-dns-017.com`) are live on Vercel with automatic GitHub deployments enabled.

---

### 🎯 Action D: Organic AI Persona Instagram + ManyChat Auto-DM Engine + Competitor Spy Winners
1. **Instagram Account Safety & Bio Rules (Preventing Day-1 Link Restrictions):**
   - For the first **5 full days** of any new Instagram Creator account, **never** paste a `.store` URL or discount text (`"88% OFF"`, `"₹199"`, `"DM for link"`) in the bio. Use this clean creator bio first:
     ```text
     ✨ 4K AI Visuals & Virtual Creator Studio 🤖
     🎬 Character DNA • Cinematic AI Reels
     📍 Digital Art & Creator Lab
     ```
   - After 5 days of normal warmup, add `https://personalabs.store` via the mobile app (**Edit profile → Links → Add external link**).
2. **Connect Free ManyChat Auto-DM (`manychat.com` — Once 5-Day Warmup Completes):**
   - Trigger when user comments on any Reel with: `AI`, `LAUNCH`, `MODEL`, `REEL`, `HACK`, `LINK`, `PROMPT`.
   - Use the exact Public Comment Auto-Replies and Automated DM scripts in [`docs/OUTREACH.md`](OUTREACH.md).
3. **Verified Live Meta Ad Library Competitor Winners (`facebook.com/ads/library` — Oct 2026 Scan Across All 4 Tabs):**
   - **Tab 1 (`India — earlycaves`):** No active AI Influencer ads currently running under `earlycaves`.
   - **Tab 2 (`India — "AI Influencer"` Video Ads):**
     - **`MindBrix EdTech Solution` (`₹249` — Running 26+ days since 15 Sep 2026 · `2 ads use this creative and text`):** *"You’ve probably seen AI influencers before. But what if you could actually build one yourself? 👀 AI Influencer Mastery 2.0 teaches you how to create a realistic AI character, maintain the same identity across content, generate images & videos, and build an AI creator brand from scratch... Lifetime access for ₹249."*
     - **`Digitalvalut Media` (`₹199` — Running 67+ days nonstop since 5 Aug 2026):** *"🚀 AI Influencer banana ab pehle se bhi easy hai! ✅ AI Influencer Create Karna ✅ Viral AI Reels Banana ✅ Realistic AI Images Generate Karna ✅ Bina Face Reveal Content Banana... 📥 Payment ke turant baad Instant Course Access milega. Koi waiting nahi. 🔥 Launch Offer: ₹199 Only"*
     - **`Varnexa Digital` (`₹199` — Running since 2 Oct 2026):** Headline: **`This Girl Isn’t Real… But Her AI Page Is Making Money 😳`** | Copy: *"People are creating AI Influencer pages, viral reels & faceless content using simple AI tools — and earning online without showing their face... No Camera. No Experience. No Team Needed 🚀 Limited Time Offer Only ₹199/-"*
     - **`Shreya Xtrader` (`₹199` — Running 2 active video variations since 6 Oct 2026):** Headline: **`Build Your Own AI Influencer – ₹199 (30-min masterclass · Instant access)`** | Copy: *"She doesn't exist. Her face, her photos, her reels — all made with AI. In this 30-minute masterclass I show the full system on screen: how she's created, how her page grows, and the AI chat bot that replies to fans 24/7. No face. No camera."*
     - **`FlyAds.ai` (Running ~6 months since 18 Apr 2026 · `This ad has multiple versions`):** 4-line Hinglish/English emoji bullets (`🚨 Flyads app se video ads banaao in 2 minutes 💸 Promote Your Business 👯‍♀️ 500+ Real Looking AI Influencers ✅ Increase Leads & Sales`).
   - **Tab 3 (`India — "AI Model" Instagram` Video Ads):**
     - **`Fame Sutra` (`3 ads use this creative and text`):** *"1 फोटो से बनाएं Trending Fashion Walk AI Video."* (Proves high Indian demand for 1-photo-to-video fashion walk workflows).
   - **Tab 4 (`US / Global — "AI Influencer"` Video Ads):**
     - **`AI Video Skool` (`$9` — Running ~6 months nonstop since 15 Apr 2026 across India & US · `2 ads use this creative and text` x 4 ad sets):** Headline: **`Create Your AI Influencer — Join Only for $9`** | Copy: *"AI video is turning into a real business skill. Not because it’s trendy, but because brands, creators, and businesses all need more content than ever before... The opportunity is not in making random AI clips. It’s in learning how to make AI videos that actually look good enough to use for ads, content, and client work."*
     - **`russestudiosv with Makeugcai` (Running 51+ days since 21 Aug 2026):** *"This is AI. He was created inside MakeUGC. The pores, the eyes, the veins: all AI. And this AI influencer made $7K this month."*
     - **`FanPro Management` (Running since 13 Aug 2026 · `3 ads use this creative and text`):** *"We build AI Influencers. You own them... We post their content on Instagram, TikTok, and Fanvue."*

---

### Action E (Day 4 & Day 8): Meta Ads Campaign #1 (`India INR`) & Campaign #2 (`Tier-1 USD`)

> [!CAUTION]
> **GOLDEN RULE — Never Put India and US/UK/CA/AU in the Same Ad Set!**
> Always run **Campaign #1 = India Only (`₹ INR`)** using [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads) and **Campaign #2 = Tier-1 Countries (`US + UK + Canada + Australia` in `$ USD`)** using [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads).

| Setting / Metric | 🇮🇳 Campaign #1: India Only (Launch Today / Day 1) | 🌎 Campaign #2: Tier-1 `US, UK, CA, AU` (Launch Day 5) |
| :--- | :--- | :--- |
| **Video Ad Creatives** | [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads) (`₹249` Flash Offer) | [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads) (`$9` Flash Offer) |
| **Campaign Objective** | `Sales` → Website → Event: **`Purchase`** | `Sales` → Website → Event: **`Purchase`** |
| **Locations & Age** | `India`, Age `18–36` | `United States, United Kingdom, Canada, Australia` (*Exclude India*), Age `18–40` |
| **Placements** | Manual: **IG Reels, IG Stories, IG Feed, FB Reels** only | Manual: **IG Reels, IG Stories, IG Feed, FB Reels** only |
| **Starting Daily Budget** | **`₹500 – ₹800 / day`** | **`₹1,200 – ₹2,000 / day`** |
| **Checkout Price & Gateway** | `₹249` Base / `₹647` Full Bundle (**Razorpay Live**) | `$9` Base / `$20` Full Bundle (**PayPal Live**) |
| **Target Cost Per Purchase** | `₹90 – ₹150` (`2.5x+ ROAS` with order bumps) | `$5 – $9` (`₹420 – ₹760`) |

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

#### Copy-Paste Headlines & Primary Ad Text Options (Meta Ads Manager):

* **3 Battle-Tested Headlines (Add all 3 using Meta's `+ Add Headline Option`):**
  1. `This Girl Isn’t Real… Build Your Own AI Influencer (₹249 Instant Access) 😳` *(or `$9 Instant Access` for Global)*
  2. `Build Your Own AI Influencer in 5 Days — Instant Vault Access 🚀`
  3. `23 HD Videos + 250 Face-Lock Prompts (88% OFF Launch Offer)`

* **Primary Text Option A (Hybrid Competitor Winner — Best for India & Global):**
```text
She doesn't exist. Her face, her skin texture, her 4K Reels — 100% made with free AI tools. 🤖✨

Inside the PersonaLabs 5-Day AI Influencer Launch Kit, you’ll see the full system on screen:
✅ 100% Face-Lock DNA: Keep the exact same realistic face across every photo & outfit
✅ 4K Viral AI Reels: Turn static images into ultra-real vertical videos on your phone or laptop
✅ 24/7 Auto-DM Monetization: Automated DM funnels that convert views into sales without showing your face
✅ Bonus Included: 250+ Character DNA Prompts & Lighting Bible

📥 Instant Vault + Google Drive Access immediately after payment (No waiting, no camera, no coding needed).

🔥 Launch Offer: Only ₹249 Today (or $9 Global — 88% OFF Regular Price)
👇 Tap "Learn More" to unlock instant access now:
https://personalabs.store
```

* **Primary Text Option B (Ultra-Punchy 4-Line Hook — Modeled on 50+ Day US Winner):**
```text
This is 100% AI.
The pores, the eyes, the natural skin texture, the 4K Reels — all generated without a camera or studio.
And faceless AI Influencer pages like this are pulling 100K–1M+ views on autopilot.

Learn the exact 23-video Face-Lock & Viral Reel system today for just ₹249 (or $9) — instant access at personalabs.store 👇
```

* **Primary Text Option C (Skill & Authority Hook — Modeled on 6-Month `AI Video Skool` Winner):**
```text
Creating realistic AI Influencers is turning into a real digital business skill.

The opportunity is NOT in making random AI clips that change faces every time.
It’s in locking 100% facial consistency across photos, outfits, and 9:16 Reels that look real enough for brand deals, digital products, and automated affiliate funnels.

Inside PersonaLabs Academy (₹249 / $9 Instant Access), you get all 23 step-by-step HD video lessons + 250 copy-paste prompts.
👇 Tap "Learn More" to start building tonight:
https://personalabs.store
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
