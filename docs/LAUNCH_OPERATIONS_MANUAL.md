# 📖 PersonaLabs Academy — Complete Launch & Operations Manual

Last Updated: **October 30, 2026** (`v2.9.3`)  
Status: **🟢 4 Sales Confirmed (₹2,389 • ₹597 AOV) • Creative Test Validated (6.45% CTR • ₹34.83 CPM • 4.6K Plays) • 5 Master Ad Hooks Ready • Storefront Live on Vercel CDN**

---

## 🎯 1. Executive Summary & Live Assets

| Asset / Component | Live Identifier / URL | Current Status | Notes |
| :--- | :--- | :--- | :--- |
| **Official Website** | [https://personalabs.store](https://personalabs.store) & [https://www.personalabs.store](https://www.personalabs.store) | 🟢 **100% Live** | Hosted on Vercel Global Edge CDN (`216.198.79.1`). Zero server costs. Anchored on ₹199 Instant Prompt Vault. |
| **Secret Testing Route** | [https://www.personalabs.store/kjboavhpoieabpraegnaln](https://www.personalabs.store/kjboavhpoieabpraegnaln) | 🟢 **Active for Testing** | **₹1 INR** (Razorpay) / **$1 USD** (PayPal) per item with 1-click currency toggle. Can be disabled anytime in `app.js`. |
| **Official Printable PDF Receipt** | [`https://personalabs.store/course-vault/receipt.html`](../course-vault/receipt.html) | 🟢 **100% Live** | Instant (`<50ms`) A4 printable invoice/receipt. Shows `Tax Invoice` + `Included (₹0.00)` for India (`INR`) and `Payment Receipt` + `Included ($0.00)` (no GST) for International (`USD`). |
| **Member Vault Portal** | `https://personalabs.store/course-vault/` | 🟢 **100% Live** | 18 HD lessons, 250+ prompts, and authenticated add-on downloads. |
| **5 Master Ad Hooks** | [`ads-ready/dancing-ad-hooks/`](../ads-ready/dancing-ad-hooks/) | 🟢 **Rendered & Ready** | 5 high-converting 1080×1920 video ads (`Hottest_Hook_01` to `05`) re-sequenced to open at `0:00` with the model's radiant eye-contact smile. Zero glyph box errors, `-movflags +faststart`. |
| **Meta Ad Account** | `PersonaLabs Academy Ads` (`2218391099056783`) | 🟢 **Active** | Currency: INR (`₹`). Timezone: Asia/Kolkata. Paused on `Payment error` upon prepaid budget exhaustion; top up via UPI to resume. |
| **Meta Dataset / Pixel** | `PersonaLabs Academy Pixel` (`1661173205598260`) | 🟢 **Tracking Live** | Events: `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`. |
| **Instagram Creator Identity** | [`@personalabsacademy`](https://www.instagram.com/personalabsacademy/) | 🟢 **Active (26 Followers)** | 19 posts, 4,625 plays on boosted Reel. External bio link unlocks after 10 Nov cooldown; direct sales run via Ads Manager website buttons. |
| **Facebook Page Identity** | `PersonaLabs Academy` (`ID: 61595148306909`) | 🟢 **Connected** | Linked to Ad Account and Campaign Identity. |
| **India Payment Gateway** | Razorpay Live (`rzp_live_TmX62nNGuBaTUc`) | 🟢 **Live** | Instant UPI (GPay, PhonePe, Paytm, QR) + RuPay/Visa Cards. |
| **Global Payment Gateway** | PayPal Live (`BAARfEN6...`) | 🟢 **Live** | PayPal 1-Click + International Cards in USD ($). |
| **Google Sheets Orders DB** | `PersonaLabs Academy — Orders DB` (`1Sy8fy...`) | 🟢 **Connected (22 Cols)** | Real-time logging of leads (`INITIATED_CHECKOUT`) and paid orders (`PAID_SUCCESS`). 4 confirmed orders (`₹2,389.00`). |
| **Google Drive Auto-Access** | Webhook App (`DriveApp.addViewer`, **Version 3**) | 🟢 **Connected** | Automatically whitelists customer's Gmail for purchased Drive folders (`01-Core`, `02-NSFW`, `03-Hooks`). |
| **Automated Email Engine** | Apps Script Triggers (`GmailApp`, **Version 3**) | 🟢 **Running 24/7** | 1. **25-Min Cart Recovery** (`sendAbandonedCartRecoveryEmails` every 15m)<br>2. **12-Hr Add-On Upsell** (`sendPostPurchaseAddonUpsellEmails` every 2h) with plain-text parity & CAN-SPAM footer. |
| **GitHub Repository** | [`wandringspirit/personalabs-academy`](https://github.com/wandringspirit/personalabs-academy) | 🟢 **Connected to Vercel** | Every `git push origin main` auto-deploys to `https://personalabs.store` in ~15 seconds. |
| **Local Folder Architecture** | `ai-influencer-course-website` & `personalabs-academy` | 🟢 **Linked via Junction** | `personalabs-academy` is a Windows Junction pointing to `ai-influencer-course-website` (0 MB duplication). |

---

## ⚡ 2. Campaign #1 Setup, Live Telemetry & Budget Architecture

### A. How Your ₹500 Daily Budget Is Split Across Ads
You have **Advantage Campaign Budget (CBO)** enabled on the Campaign level:
* **Total Daily Budget:** **₹500.00 / day** (plus standard 18% GST).
* **Placements:** Instagram Reels & Instagram Stories (Threads & Facebook Feed unchecked to prevent 9:16 vertical video aspect-ratio errors).
* **Budget Distribution:** Meta's machine learning algorithm dynamically allocates spend across all 3 creatives based on Watch-Time, Outbound CTR, and Cost per Click:
  * **`Ad 01 - Curiosity Reveal (INR)`:** High scroll-stopping hook (*"Wait… she doesn't actually exist"*).
  * **`Ad 02 - Proof & Monetization`:** Revenue & consistency proof (*"Stop paying ₹15,000 for product shoots"*).
  * **`Ad 03 - No Laptop 5Day System`:** Low-friction mobile objection handler (*"Think you need an expensive gaming PC?"*).

### B. Day-2 Live Early Performance Snapshot (Oct 12, 5:10 PM IST)

| Ad Creative | Spend | Page Engagements | Link Clicks | Link CTR (Target: `>1.2%`) | Cost Per Click (CPC) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ad 01 - Curiosity Reveal (INR)** | ₹144.63 | **67** | **5** | **3.52%** 🔥 | ₹28.93 |
| **Ad 02 - Proof & Monetization** | ₹38.93 | **6** | **1** | **5.26%** 🔥 | ₹38.93 |
| **Ad 03 - No Laptop 5Day System** | ₹20.49 | **5** | **1** | **5.56%** 🔥 | **₹20.49** |
| **TOTAL / AVERAGE** | **₹204.05** | **78** | **7 Clicks** | **~4.1% Avg** | **₹29.15 Avg** |

---

### C. Ad Scheduling: Why Running 24/7 on Daily Budget Is Optimal
* **Under Daily Budget (Current Setup — ₹500/day):**  
  Meta runs ads **24 hours a day** continuously, naturally pacing spend and concentrating delivery during peak evening engagement hours (`7:00 PM – 11:30 PM IST`) and late-night impulse buying windows (`10:00 PM – 2:00 AM IST`).

---

## 🛠️ 3. Secret Testing Route (`/kjboavhpoieabpraegnaln`) & Official PDF Receipt

* **Test Route URL:** `https://www.personalabs.store/kjboavhpoieabpraegnaln`
* **Test Pricing (`v2.9.0`):**
  * **Rupees (`INR`):** Base Kit = **₹1**, Order Bump #1 = **+₹1**, Order Bump #2 = **+₹1**
  * **Dollars (`USD`):** Base Kit = **$1**, Order Bump #1 = **+$1**, Order Bump #2 = **+$1**
* **Features:**
  * Dedicated on-screen toggle to switch between **Rupees (₹1 / item via Razorpay)** and **Dollars ($1 / item via PayPal)**.
  * Real payment execution: testing verifies Razorpay / PayPal receipt, Google Sheets logging, and Google Drive auto-whitelisting.
* **Official Printable PDF Receipt (`course-vault/receipt.html`):**
  * Opens in **<50ms** (preloaded via `<link rel="prefetch" href="course-vault/receipt.html" />` with non-blocking fonts).
  * Automatically adapts to buyer currency:
    * **🇮🇳 India (`INR`):** Displays **`Tax Invoice`** and **`Digital GST / Processing: Included (₹0.00)`**.
    * **🇺🇸 International (`USD`):** Displays **`Payment Receipt`** and **`Digital Delivery & Processing: Included ($0.00)`** (zero mention of GST).
* **How to Enable / Disable Test Route:**
  * In [`app.js`](../app.js) (around line 1810):
    ```javascript
    testSandboxPage: {
      slug: 'kjboavhpoieabpraegnaln',
      enabled: false, // Change to false to disable and redirect all visits to '/'
      inrUnitPrice: 1,
      usdUnitPrice: 1
    }
    ```

---

## 📊 4. Automated Email Recovery, Upsells & 48-Hour Scaling Playbook

### Rule 1: Let the Initial ₹889 Balance Run for 48 Hours
* Keep the campaign untouched at **₹500/day** while Meta completes its initial learning window and runs through the prime evening buying hours (`7:00 PM – 11:30 PM IST`).

### Rule 2: Key Metrics to Track in Ads Manager (Always Set Date Range to `Today` or `Last 7 Days`)

| Metric | Target Benchmark | What It Means | Action to Take |
| :--- | :--- | :--- | :--- |
| **Outbound / Link CTR** | **`> 1.2%`** *(Currently `3.52%–5.56%`)* | Strong hook, viewers are clicking through to the site. | Creative is a winner. Keep running. |
| **Cost Per Link Click (CPC)** | **`< ₹15 – ₹25`** | Targeted Indian creator traffic warming up. | Healthy ad auction performance. |
| **Cost Per Initiate Checkout** | **`< ₹40 – ₹60`** | Visitors are entering name/email/phone on checkout. | Check Orders DB for yellow rows. |
| **Cost Per Purchase (CPA)** | **`< ₹120 – ₹150`** | Profitable customer acquisition against ₹249+ cart. | Scale daily budget by **+25%**. |

---

### Rule 3: 100% Automated Brand Email Recovery & Post-Purchase Add-On Upsells (Apps Script Version 3)
Instead of messaging leads from a personal WhatsApp number, your **Google Apps Script (`Version 3`)** runs two automated background triggers from **`PersonaLabs Academy <personalabsacademy@gmail.com>`**:

1. **Automated 25-Minute Abandoned Cart Recovery (`sendAbandonedCartRecoveryEmails` — runs every 15 mins):**
   * Scans `PersonaLabs Academy — Orders DB` for `INITIATED_CHECKOUT` rows older than **25 minutes**.
   * **Smart Buyer Skip:** Automatically checks all `PAID_SUCCESS` rows first — if a visitor abandoned checkout at 8:00 PM and bought at 8:15 PM, they are automatically marked `SKIPPED (Purchased Course)` in Column 21 and **never** emailed by mistake.
   * Sends a high-deliverability transactional email (`plainText` + HTML + CAN-SPAM MSME footer) inviting them to complete enrollment, and marks Column 21 as `SENT (timestamp)`.
2. **Automated 12-Hour Post-Purchase Add-On Upsell (`sendPostPurchaseAddonUpsellEmails` — runs every 2 hours):**
   * Scans `PAID_SUCCESS` rows older than **12 hours**.
   * Checks which add-ons the buyer already owns across all orders. If they already own both Bump #1 and Bump #2, marks Column 22 as `SKIPPED (Owns All Add-Ons)`.
   * Otherwise, emails them their private 1-click student upgrade links (`https://personalabs.store/?upgrade=bump1` and/or `https://personalabs.store/?upgrade=bump2`) where Base Kit price is automatically `₹0` and they only pay for the missing add-on!

---

### Rule 4: Budget Scaling Strategy
* Once your campaign achieves profitable purchases at a Cost Per Purchase under ₹150:
  * Increase the daily budget by **+25%** every 48 hours using your course earnings to self-fund growth.
  * Never double the budget overnight as this resets Meta's learning phase.

---

## 📸 5. Autonomous 3-Agent Instagram Team (`@personalabsacademy`) & Queue Low-Refill Alerts

1. **How the 3-Agent Instagram Team Works:**
   * **`ig-content-studio` (Visual Producer):** Generates `9:16` (`1080x1920`) organic Reels, custom cover thumbnails, and `4:5` (`1080x1350`) 5-slide educational carousels inside [`instagram-studio/`](../instagram-studio).
   * **`ig-copy-and-funnel` (Copy & ManyChat Strategist):** Writes high-retention captions, first-comment SEO hashtag blocks, and ManyChat comment-to-DM keyword triggers (`AI`, `LAUNCH`, `MODEL`, `REEL`, `HACK`, `LINK`, `PROMPT`) in [`instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md`](../instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md).
   * **`instagram-creator-operator` (Browser Publisher & Scheduler):** Uploads posts right now and schedules upcoming Days 2–14 inside **Meta Business Suite Content Planner** (`business.facebook.com/latest/content_calendar`) so Meta's servers publish them on exact dates/times even when your laptop is off.
2. **How We Know When a Scheduled Batch Runs Low (2 Automatic Safeguards):**
   * **Safeguard A — Recurring Antigravity Cron Schedule (`/schedule`):** A standing background cron job wakes up the agent every 7 days (`0 10 * * 0`) to check [`instagram-studio/CONTENT-CALENDAR.md`](../instagram-studio/CONTENT-CALENDAR.md) and Meta Business Suite Content Planner, and automatically prepares the next 7–14 day batch before the queue runs out.
   * **Safeguard B — Automated Email Alert (`personalabsacademy@gmail.com`):** Your Google Apps Script can also send you a `"⚠️ Instagram Queue Running Low (48h Remaining)"` reminder email 48 hours before the last scheduled post date in your batch so you never miss a refill window.

---

## 🚀 6. Immediate Next Operations: Billing Top-Up & Direct Sales Campaign Launch

### A. Resolving the `Payment error` in Meta Ads Manager
1. Visit **Ads Manager Billing**: `https://adsmanager.facebook.com/billing`
2. Under **Payment Methods / Balance**, click **Pay Now** to settle the remaining balance (`₹253.57`).
3. Add a prepaid deposit of **₹500.00 – ₹1,000.00** using UPI, NetBanking, or Debit Card.
4. Once funded, ads resume delivery immediately without resetting account data.

### B. Launching the Direct Website Sales Campaign (`OUTCOME_SALES`)
While the Instagram profile external link is on security cooldown until **10 Nov 2026**, **do not use "Profile Visits"**. Instead, launch a **Website Sales Campaign**:
* **Campaign Objective:** Sales (`OUTCOME_SALES`).
* **Conversion Location:** Website (`https://personalabs.store`).
* **Optimization Event:** `Purchase` (Meta Pixel `1661173205598260`).
* **Budget Strategy:** Advantage Campaign Budget (CBO) at **₹500.00/day**.
* **Placements:** Instagram Reels & Stories.
* **Creatives:** The 5 newly re-sequenced master hook videos in [`ads-ready/dancing-ad-hooks/`](../ads-ready/dancing-ad-hooks/):
  1. `Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4`
  2. `Hottest_Hook_02_Emerald_Satin_Backless_Turn.mp4`
  3. `Hottest_Hook_03_Champagne_Corset_VIP_Club.mp4`
  4. `Hottest_Hook_04_Mediterranean_Resort_Smile.mp4`
  5. `Hottest_Hook_05_Bollywood_Rooftop_Sway.mp4`
* **On-Screen CTA Button:** Set to **"Learn More"** or **"Shop Now"** with website destination `https://personalabs.store`.  
  *Advantage:* When users tap the CTA button on the Reel, the storefront opens directly inside Instagram's in-app browser with the Razorpay checkout. This **100% bypasses the profile bio link restriction**!

### C. Organic Reel Monetization (ManyChat Follow-Gated DM)
On all organic Instagram posts before 10 Nov:
* Use on-screen text & caption: *"Follow @personalabsacademy and comment **PROMPT** below — I'll DM you the link!"*
* ManyChat verifies follower status and sends `https://personalabs.store` directly into their DMs with zero link restrictions.



