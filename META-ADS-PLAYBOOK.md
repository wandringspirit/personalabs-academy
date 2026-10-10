# 🚀 PersonaLabs Academy (`personalabs.store`) — Master Launch Playbook

This playbook is ordered in the **exact chronological sequence** to take you from where you are right now to collecting automated `₹249–₹647` (and `$9–$23`) sales every day.

---

## 🗓️ Date-Wise & Task-Wise Master Execution Calendar

| Day / Date | Phase & Focus | Exact Tasks to Complete | Time Needed | Status / Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1 (Today — Oct 11)** | **Phase 1 & 2: Legal + Live Website + Payment Keys** | 1. Register Udyam (`UDYAM-UP-43-0208040`) ✅<br>2. Unlock Razorpay Dashboard ✅<br>3. Drop `personalabs-site.zip` onto Netlify & connect `personalabs.store` DNS<br>4. Submit `https://personalabs.store` on Razorpay & paste `rzp_live_...` Key into `app.js` | **15 Mins** | 🟡 *In Progress (Step 3 & 4 left)* |
| **Day 2 (Oct 12)** | **Phase 3 & Bonus Engine: AI Persona IG + ManyChat (`₹0` Ad Spend)** | 1. Create your AI Persona Instagram Creator account & put `personalabs.store` in bio<br>2. Generate 6 consistent photos + 2 Reels using `character-dna-prompt-bible.html` on `SeaArt.ai` / `Kling AI`<br>3. Connect **ManyChat (Free)** to auto-DM `https://personalabs.store` when users comment `LAUNCH` or `AI`<br>4. Post your first **2 Reels + 1 Trial Reel** | **45 Mins** | ⬜ *Ready for Tomorrow* |
| **Day 3 (Oct 13)** | **Phase 4: Competitor Ad Spy + Create 3 Video Ads** | 1. Open Meta Ad Library (`facebook.com/ads/library`) → Search `earlycaves.com` & `AI Influencer` → Note top 3 longest-running video ads<br>2. Edit **Video Ad #1** (*"Wait, She Isn't Real?!"*), **Video Ad #2** (*"Inside the Course Vault"* screen recording), and **Video Ad #3** (*"Old Way vs. AI Creator"*) in CapCut<br>3. Post 2 daily Organic Reels on your IG page | **45 Mins** | ⬜ *Scheduled* |
| **Day 4 (Oct 14)** | **Phase 5: Meta Pixel + Launch India Campaign (`₹500/day`)** | 1. Create Meta Pixel in Events Manager & paste 15-digit ID into `app.js`<br>2. Launch **Campaign #1 (India Only)** in Meta Ads Manager (`Sales` → `Purchase` → `₹500–₹800/day` → IG Reels/Stories/Feed)<br>3. Post 2 daily Organic Reels | **30 Mins** | ⬜ *First Paid Traffic Live* |
| **Days 5–6 (Oct 15–16)** | **Phase 6: 48-Hour Ad Testing & Pruning** | 1. Let India ads run for 48 hours untouched<br>2. Check **Outbound CTR** (keep videos `> 1.2%`, pause any video `< 0.8%` after `₹250` spent)<br>3. Verify Cost Per Purchase is `₹90–₹160` (2.5x+ ROAS with Order Bumps)<br>4. Post 2 daily Organic Reels | **15 Mins/day** | ⬜ *Identify #1 Winning Video* |
| **Day 7 (Oct 17)** | **Phase 6: Scale India Winner + Connect PayPal** | 1. Increase budget on winning India Ad Set by **+25%** (`₹600` → `₹800/day`)<br>2. Connect **PayPal Business** (or enable **Razorpay International Cards**) for `$ USD` payouts to your Indian bank account | **20 Mins** | ⬜ *Consistent Daily `₹ INR` Sales* |
| **Days 8–14 (Oct 18–24)** | **Phase 7: Launch Tier-1 International (`US / UK / CA / AU` in `$ USD`)** | 1. Duplicate #1 winning video ad → change ending price text from `₹249` to **`Just $9 Today (88% OFF)`**<br>2. Launch **separate Campaign #2** targeting **`US, UK, Canada, Australia`** (`₹1,200–₹2,000/day`)<br>3. Collect **`$9–$23 USD` (`₹750–₹1,940 INR`)** per sale while continuing 2 daily Organic Reels | **20 Mins/day** | ⬜ *Global `₹ INR` + `$ USD` Scale* |

---

## ✅ PHASE 1: Finish Udyam & Unlock Razorpay KYC *(Completed!)*

Right now, Razorpay is waiting for business name proof for **`PersonaLabs Academy`** so your personal name stays off the website.

- [ ] **Step 1.1 — Complete the Udyam Form (`udyamregistration.gov.in`):**
  - **Enterprise / Unit Name:** `PersonaLabs Academy`
  - **ITR (4.2) & GSTIN (4.3):** Select **`No`**
  - **WDV Investment (5A):** Enter **`25000`** | **Exclusion (5B):** Enter **`0`**
  - **Total Turnover (6A):** Enter **`0`**
  - **Major Activity:** Select **`Services`** → **NIC Code:** `85499` (*Other educational services*) or `62011` (*IT/Software*)
- [ ] **Step 1.2 — Download Your Udyam Certificate PDF:**
  - Once you submit the OTP, click **Print / Download Udyam Certificate (PDF)**.
- [ ] **Step 1.3 — Upload to Razorpay:**
  - Go back to your Razorpay tab → Keep brand name as **`PersonaLabs Academy`** → Upload the Udyam Certificate PDF.

---

## 🌐 PHASE 2: Put `personalabs.store` Live on the Internet (5 Mins)

- [ ] **Step 2.1 — Host Your Site for Free on Vercel (or Netlify):**
  1. Go to **https://vercel.com** (or **https://app.netlify.com/drop**).
  2. Upload/import your project folder: `C:\Users\piyus\.gemini\antigravity\scratch\ai-influencer-accelerator`.
- [ ] **Step 2.2 — Connect `personalabs.store` on Namecheap:**
  1. Inside Vercel → go to **Settings → Domains** → type **`personalabs.store`** and click **Add**.
  2. Open **Namecheap → Domain List → `personalabs.store` → Manage → Advanced DNS**.
  3. Add these 2 records under **Host Records**:
     - **Record 1:** Type = **`A Record`** | Host = **`@`** | Value = **`76.76.21.21`** | TTL = `Automatic`
     - **Record 2:** Type = **`CNAME Record`** | Host = **`www`** | Value = **`cname.vercel-dns.com`** | TTL = `Automatic`
  4. Wait 5–10 minutes and test **`https://personalabs.store`** in your browser!
- [ ] **Step 2.3 — Paste Your Live Payment Keys in `app.js`:**
  - Once Razorpay gives you your Live Key ID (`rzp_live_...`), paste it into `PAYMENT_GATEWAY_CONFIG.razorpay.keyId` in `app.js`.
  - For US/Global (`$ USD`) buyers, paste your PayPal.Me username or PayPal payment links into `PAYMENT_GATEWAY_CONFIG.paypal` in `app.js`.

---

## 🎓 PHASE 3: Verify Your Post-Payment Product Delivery (5 Mins)

Your buyers get **100% instant on-screen link delivery** the moment they pay — **zero emails needed**.

- [ ] **Step 3.1 — Preview Your Built-In Student Vault:**
  - Local Preview: **`http://127.0.0.1:8085/course-vault/index.html`** (Live URL will be: **`https://personalabs.store/course-vault/index.html`**)
  - Review the 4 products inside `course-vault/`:
    1. `course-vault/index.html` — **5-Day / 18-Lesson Interactive Course Portal**
    2. `course-vault/character-dna-prompt-bible.html` — **250+ Character DNA & Face-Lock Prompt Bible**
    3. `course-vault/uncensored-content-hack.html` — **Order Bump #1 (+₹249): Uncensored Content Hack VIP Guide**
    4. `course-vault/viral-hooks-and-autodm-pack.html` — **Order Bump #2 (+₹149): 500+ Viral Reel Hooks & Auto-DM Pack**
- [ ] **Step 3.2 — (Optional) Put PDFs in Your Own Google Drive Folder:**
  - Open each of the 4 pages above → click **`🖨️ Save / Print as PDF`** → upload the 4 PDFs to a folder in your Google Drive → Share as *Anyone with the link (Viewer)* → paste your Drive link into `index.html` and `course-vault/index.html`.

---

## 🕵️‍♂️ PHASE 4: Spy on Competitor Ads & Create Your 3 Video Ads (30 Mins)

### Step 4.1 — Secret Shortcut: See Your Competitor's Exact Live Ads for Free
- [ ] Go to **https://www.facebook.com/ads/library**.
- [ ] Set **Location** to **`India`** and **Ad Category** to **`All Ads`**.
- [ ] In the search bar, type **`earlycaves.com`** (and also search **`AI Influencer`** or **`AI Model`**).
- [ ] Look for the ads that have been **running the longest (2+ weeks)** — Meta only keeps spending money on ads that are making daily profit. Model your video hooks directly on those!

### Step 4.2 — Create Your 3 Vertical (9:16) Video Ads in CapCut (15–25 Seconds Each)

1. **🎬 Video Ad #1: The *"Wait, She Isn't Real?!"* Reveal (Highest Click-Through Rate)**
   - **0–3s:** Show the hyper-realistic AI model Reel clip (`@mayavirtual` / `@riya_verse.ai`) with text overlay: *"Everyone thinks she's a real travel influencer making ₹3.5L/month... look closer 👀"*
   - **3–12s:** Fast screen recording of generating her consistent face on a phone + swapping outfits.
   - **12–22s:** *"No camera. No showing your face. No laptop needed. Get the 5-Day AI Influencer Launch Kit + 250 Face-Lock Prompts for ₹249 today (88% OFF). Tap 'Learn More' for instant access!"*
2. **🎬 Video Ad #2: The *"Inside the Vault"* Screen Recording (Highest Conversion Rate)**
   - **0–4s:** Record your screen scrolling through `personalabs.store/course-vault/index.html` and the 625-Permutation Prompt Builder: *"Here is the exact AI Influencer Vault you unlock 5 seconds after checkout 👇"*
   - **4–15s:** Tap through Day 1 → Day 2 → Day 3 → Uncensored Content Hack Guide.
   - **15–22s:** Show the `₹249` checkout card and tap `Make Payment →`.
3. **🎬 Video Ad #3: *"Old Creator Struggle vs. New AI Creator"* Comparison**
   - **0–4s:** ❌ *Filming yourself: Camera shy, 3 hours editing, 200 views* vs. ✅ *100% Face-Locked AI Influencer built on your phone in 12 mins.*
   - **4–20s:** Show the 4 AI personas and tell viewers to tap **Learn More** before the `₹249` Flash Sale expires.

---

## 📈 PHASE 5: Launch Your Meta Ads Campaign (20 Mins)

- [ ] **Campaign Objective:** **`Sales`** (Website Conversions → `Purchase` event)
- [ ] **Daily Budget:** **`₹500 – ₹800 / day`**
- [ ] **Location & Age:** `India`, Age `18–36`
- [ ] **Placements:** Manual Placements → **Instagram Reels, Instagram Stories, Instagram Feed, Facebook Reels** only (uncheck Audience Network)
- [ ] **Destination URL:** `https://personalabs.store`
- [ ] **Scaling Rule:** Turn off any video ad with `< 0.8%` CTR after `₹250` spent; increase budget by 25% every 48 hours on any ad set getting purchases under `₹160`.


---

## 📱 BONUS ENGINE: The "₹0 Ad Spend" AI Persona Instagram + ManyChat Funnel

1. **Create Your AI Persona Profile (15 Mins):**
   - Switch to **Instagram Professional Account → Creator** (free, required for ManyChat).
   - Put **`https://personalabs.store`** in your Website Link field.
2. **Generate Your First Photos & Reels for $0:**
   - Open `http://127.0.0.1:8085/course-vault/character-dna-prompt-bible.html`, copy a master prompt, generate on `SeaArt.ai` / `Tensor.art`, and animate on `Kling AI` / `Hailuo MiniMax`.
3. **Post 2 Reels/Day + 1 "Trial Reel"/Day Using Your Hook Vault (`course-vault/viral-hooks-and-autodm-pack.html`):**
   - **Reel #1 (12:30 PM):** 4.5s aesthetic loop with hook: *"99% of people scrolling past this still don't realize I don't exist in real life 👀"* → Caption: *"Comment **LAUNCH** and I'll DM you the ₹249 5-Day AI Influencer Blueprint!"*
   - **Reel #2 (7:30 PM):** 3s AI model clip + 6s screen-recording of your Course Vault (`course-vault/index.html`) → Caption: *"Comment **AI** for the instant access link ⚡"*
4. **Connect ManyChat (Free Plan):**
   - Trigger keywords: `LAUNCH`, `AI`, `LINK`, `PROMPT` → Auto-DM `https://personalabs.store`.


---

## 🌎 PHASE 7: Scaling Outside India (`US / UK / Canada / Australia` in `$ USD`)

> **GOLDEN RULE — Never Put India and US/UK/CA/AU in the Same Ad Set!**
> If you put India and the US in the same Ad Set, Meta's algorithm will spend 99% of your budget in India (because Indian clicks are 10x cheaper) and show your ad to almost nobody in the US. Always run **Campaign #1 = India Only (`₹ INR`)** and **Campaign #2 = Tier-1 Countries (`US + UK + Canada + Australia` in `$ USD`)**.

- **Step 7.1 — Connect PayPal in `app.js`:** Paste your PayPal Client ID or PayPal.Me username in `PAYMENT_GATEWAY_CONFIG.paypal`.
- **Step 7.2 — Duplicate Your #1 Winning Video from India:** Change the price overlay at the end of the video from `₹249` to **`Just $9 Today (88% OFF)`**.
- **Step 7.3 — Create Campaign #2 in Meta Ads Manager:**
  - **Locations:** `United States`, `United Kingdom`, `Canada`, `Australia` (Exclude India)
  - **Daily Budget:** `₹1,200 – ₹2,000 / day`
  - **Website URL:** `https://personalabs.store` (automatically switches prices to `$9` / `$18` / `$23` USD and opens PayPal checkout for non-Indian IPs!).

> **Rule #2 — Make Sure Either PayPal OR Razorpay International Cards Is Active:**
> As soon as you connect your **PayPal Business account** (or turn on **International Cards** inside your Razorpay dashboard under *Account & Settings -> International Payments*), buyers in the US/UK/Canada/Australia can pay you in `$ USD` with 1 click, and PayPal/Razorpay automatically converts the USD and deposits `₹ INR` straight into your Indian bank account!
