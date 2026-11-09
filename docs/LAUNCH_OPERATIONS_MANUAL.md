# 📖 PersonaLabs Academy — Complete Launch & Operations Manual

> **Last Updated:** November 9, 2026 (`v2.9.5`)  
> **Operating Mode:** 🟢 **100% Organic Growth & Viral Reels Funnel** • **All 11 Master Dancing Reels Scheduled in Meta Business Suite (`9–19 Nov 2026`)** • **Manual Comment-to-DM Replies (Phase-1 Low Volume)** • **Zero Ad Spend / Zero GST Liability**

---

## 🎯 1. Executive Summary & Live Assets

| Asset / Component | Live Identifier / URL | Current Status | Notes |
| :--- | :--- | :--- | :--- |
| **Official Website** | [https://personalabs.store](https://personalabs.store) & [https://www.personalabs.store](https://www.personalabs.store) | 🟢 **100% Live** | Hosted on Vercel Global Edge CDN (`216.198.79.1`). Zero server costs. Serves [`index.html`](../index.html), [`app.js`](../app.js) (`?v=25`), [`styles.css`](../styles.css) (`?v=9`). Anchored on **₹199 / $9 Instant Prompt Vault** (`90% OFF` 10-min Flash Sale; VIP Bundle `₹597 / $23`). |
| **Secret Testing Route** | [https://www.personalabs.store/kjboavhpoieabpraegnaln](https://www.personalabs.store/kjboavhpoieabpraegnaln) | 🟡 **Currently Enabled (`true`)** | Charges **₹1 INR** (Razorpay) / **$1 USD** (PayPal) per item with 1-click currency toggle (`PAYMENT_GATEWAY_CONFIG.testSandboxPage.enabled = true` in [`app.js`](../app.js)). Toggle to `false` after final live tests. |
| **Official Printable PDF Receipt** | [`course-vault/receipt.html`](../course-vault/receipt.html) | 🟢 **100% Live** | Instant (`<50ms`) A4 printable invoice/receipt preloaded via `<link rel="prefetch">`. Shows `Tax Invoice` + `Included (₹0.00)` for India (`INR`) and `Payment Receipt` + `Included ($0.00)` (zero GST) for International (`USD`). |
| **Member Vault Portal** | [`course-vault/index.html`](../course-vault/index.html) | 🟢 **100% Live** | 5-Day / 18-Lesson curriculum, [`character-dna-prompt-bible.html`](../course-vault/character-dna-prompt-bible.html) (`250+` prompts), and cryptographic `vt1`/`vt2` VIP add-ons ([`uncensored-vip-8f92a1c4.html`](../course-vault/uncensored-vip-8f92a1c4.html), [`hooks-vip-3d7e91b2.html`](../course-vault/hooks-vip-3d7e91b2.html)). Local `29`-file course mirror lives in `videos-captioned/`. |
| **11 Master Dancing Video Reels** | [`instagram-studio/reels-active-11/`](../instagram-studio/reels-active-11/) | 🟢 **All 11 Scheduled (`9–19 Nov`)** | 11 broadcast-grade `1080×1920` `30fps` Reels (`Hottest_Hook_01` to `11`) + custom front-facing covers (`thumbnails/Cover_01` to `11`), all scheduled `Public` with `CC` enabled in Meta Business Suite (`19:30–19:43 IST`). |
| **Carousel Library (`01`–`06`)** | [`instagram-studio/carousels/`](../instagram-studio/carousels/) | 🟢 **Ready (`01` Pinned)** | `01-Pinned-Carousel-5Slides` is live & pinned on `@personalabsacademy`. Carousels `02–06` are ready to interleave organically alongside the daily Reels. |
| **Instagram Organic Funnel** | [`@personalabsacademy`](https://www.instagram.com/personalabsacademy/) | 🟢 **Active (`9–19 Nov` Queue Live)** | 100% organic traffic using **Manual Comment-to-DM replies** (low initial volume) + **Story Link Stickers**. Profile external bio link cooldown lifts **tomorrow, Tue 10 Nov 2026**. |
| **Meta Ad Account** | `PersonaLabs Academy Ads` (`2218391099056783`) | ⏸️ **Halted as of Nov 8** | Prepaid balance `₹0.00` (all-time `₹4,986` paid to Meta vs `₹2,986` settled revenue across 5 orders = `-₹2,000` net; see [`META-ADS-CHANGELOG-AND-METRICS.md`](META-ADS-CHANGELOG-AND-METRICS.md)). Remains halted during organic scale. |
| **Meta Dataset / Pixel** | `PersonaLabs Academy Pixel` (`1661173205598260`) | 🟢 **Tracking Live** | Continues firing `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, and `Purchase` on [`personalabs.store`](https://personalabs.store) for clean attribution and remarketing audience seeding. |
| **India Payment Gateway** | Razorpay Live (`rzp_live_TmX62nNGuBaTUc`) | 🟢 **Live** | Instant UPI (GPay, PhonePe, Paytm, QR) + RuPay/Visa Cards & Netbanking. |
| **Global Payment Gateway** | PayPal Live (`BAARfEN6...`) | 🟢 **Live** | PayPal Smart Buttons (`NO_SHIPPING`, `soft_descriptor: 'PERSONALABS'`) + International Debit/Credit Cards in USD (`$`). |
| **Google Sheets Orders DB** | `PersonaLabs Academy — Orders DB` (`1Sy8fy...`) | 🟢 **Connected (22 Cols)** | Dual-tab (`Logs` + `Orders`) architecture capturing `CTA_CLICKED_SCROLL`, `PARTIAL_LEAD_CAPTURED`, `INITIATED_CHECKOUT`, and `PAID_SUCCESS`. 5 paid orders settled by Razorpay (`₹2,986.00`; Order `#5` settlement verified, sheet lookup check pending). |
| **Google Drive Auto-Access** | Apps Script Web App (`DriveApp.addViewer`, **V3**) | 🟢 **Connected** | Automatically grants private Reader/Viewer access on the customer's Gmail across purchased folders (`01-Core`, `02-NSFW`, `03-Hooks`). |
| **Automated Email Engine** | Apps Script Triggers (`GmailApp`, **V3**) | 🟢 **Running 24/7** | 1. **25-Min Cart Recovery** (`sendAbandonedCartRecoveryEmails` every `15m`)<br>2. **12-Hr Add-On Upsell** (`sendPostPurchaseAddonUpsellEmails` every `2h`) with plain-text parity & MSME footer. |
| **GitHub & Vercel CI/CD** | [`wandringspirit/personalabs-academy`](https://github.com/wandringspirit/personalabs-academy) | 🟢 **Connected to Vercel** | Every `git push origin main` auto-deploys to Vercel in `~8–15s`. [`vercel.json`](../vercel.json) enforces `noindex` on `/course-vault/*` and `/kjboavhpoieabpraegnaln`; [`.vercelignore`](../.vercelignore) excludes studio/script/doc folders on CLI deploys. |
| **Local Folder Architecture** | `C:\Projects\ai-influencer-course-website` & Junction | 🟢 **Consolidated (`v2.9.5`)** | Clean root structure with unified [`scripts/`](../scripts/) (plus `scripts/archive/`), [`instagram-studio/`](../instagram-studio/), and Windows Junction `C:\Projects\personalabs-academy` (`0 MB` duplication). |

---

## 📸 2. Daily Organic Reels & Manual Comment-to-DM Operations (`9–19 Nov 2026`)

With all **11 Master Dancing Video Reels** already scheduled live inside **Meta Business Suite Content Planner** (`business.facebook.com/latest/content_calendar`), daily execution focuses on **first-hour engagement, Story Link Stickers, tomorrow's bio link unlock, and fast manual DM conversions**:

### A. Verified Schedule & Immediate Action Timeline
Full file paths, verified timestamps (`19:30–19:43 IST`), copy-paste captions, and First Comments live in [`instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`](../instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md):

1. **Tonight — Mon, 9 Nov 2026 (`19:30 IST` — Reel #01 `PROMPT` goes live):**
   - Immediately after `Hottest_Hook_01_Wine_Saree_Mudra_Dance.mp4` publishes at `7:30 PM IST`, paste **Reel #01's First Comment** to stack extra SEO keywords.
   - Tap `Paper Airplane → Add to Story` on Reel #01 and overlay a native **Link Sticker** pointing to `https://personalabs.store` (`Get The ₹199 Kit 🚀`) since bio links are still cooling down until tomorrow.
2. **Tomorrow — Tue, 10 Nov 2026 (Before `19:39 IST` Reel #02 `MODEL`):**
   - Account external bio link cooldown ends! Open Instagram mobile app → **Edit Profile → Links → Add external link** → paste `https://personalabs.store`.
3. **Daily `10–19 Nov 2026` Routine (`~10 minutes/day`):**
   - Drop each published Reel's First Comment immediately after its scheduled go-live window (`19:30–19:43 IST`), share it to Stories with a Link Sticker, and optionally interleave **Carousels `02–06`** (`../instagram-studio/carousels/`) and the 3 daily interactive Stories from [`instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md`](../instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md).

### B. Phase-1 Manual DM Replies vs. Phase-2 ManyChat Switch
* **Current Operating Mode (Owner Decision — Nov 9, 2026):** Because early comment volume is low, you are replying **manually via Instagram DMs & Saved Replies** (zero ManyChat cost, zero bot flags, warmer 1-to-1 replies).
* **Active Keywords Covered:** `PROMPT`, `MODEL`, `GLITCH`, `TRAVEL`, `DANCE`, `TWIRL`, `CREATOR`, `VACATION`, `SKIN`, `LAUNCH`, `VIP` (plus `AI` / `LINK`).
* **Exact Saved Reply Scripts:** Copy the 1-tap Instagram Saved Replies and public comment reply templates from [`docs/OUTREACH.md`](OUTREACH.md) (Section 1) or [`instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`](../instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md) (Section 2).
* **Phase-2 Scale Trigger (`>10–15 comments/day`):** As soon as Reel velocity pushes daily comments past `10–15/day`, plug the exact same 11 keywords into ManyChat Comment-to-DM using the documented flow in [`docs/OUTREACH.md`](OUTREACH.md) (Section 2).

### C. Queue Refill Safeguards & Studio Tooling
* **Studio Render & QA Scripts ([`scripts/`](../scripts/)):**
  * [`scripts/build_all_11_organic_master_reels.py`](../scripts/build_all_11_organic_master_reels.py) — Canonical FFmpeg + Edge-TTS + `-movflags +faststart` Reels builder.
  * [`scripts/deep_audit_vault.py`](../scripts/deep_audit_vault.py) & [`scripts/audit_mobile_crossdevice.py`](../scripts/audit_mobile_crossdevice.py) — Automated storefront & vault QA checks.
* **Queue Refill Planning:** Before **Thu, 19 Nov 2026** (`Reel #11`), review Reels insights (`Plays`, `Watch Time`, `Shares`, `DM clicks`) inside Meta Business Suite to generate Batch #3 from winning dance hooks.

---

## 🛠️ 3. Secret Testing Route (`/kjboavhpoieabpraegnaln`) & Official PDF Receipt

* **Test Route URL:** [`https://www.personalabs.store/kjboavhpoieabpraegnaln`](https://www.personalabs.store/kjboavhpoieabpraegnaln) (or `?test=kjboavhpoieabpraegnaln`).
* **Test Pricing:**
  * **Rupees (`INR`):** Base Kit = **₹1**, Order Bump #1 = **+₹1**, Order Bump #2 = **+₹1** (Live Razorpay).
  * **Dollars (`USD`):** Base Kit = **$1**, Order Bump #1 = **+$1**, Order Bump #2 = **+$1** (Live PayPal).
* **Official Printable PDF Receipt ([`course-vault/receipt.html`](../course-vault/receipt.html)):**
  * Opens in **`<50ms`** (prefetched in [`index.html`](../index.html) with non-blocking fonts).
  * Automatically adapts to buyer currency:
    * **🇮🇳 India (`INR`):** Displays **`Tax Invoice`** and **`Digital GST / Processing: Included (₹0.00)`**.
    * **🌎 International (`USD`):** Displays **`Payment Receipt`** and **`Digital Delivery & Processing: Included ($0.00)`** (zero mention of GST).
* **How to Enable / Disable Test Route:**
  * In [`app.js`](../app.js) (lines `1906–1911`):
    ```javascript
    testSandboxPage: {
      slug: 'kjboavhpoieabpraegnaln',
      enabled: true, // Set to false to disable and redirect all visits cleanly to '/'
      inrUnitPrice: 1,
      usdUnitPrice: 1
    }
    ```
  * *(Optional)* [`app.js`](../app.js) also checks `?action=getTestPageStatus` against the Apps Script Web App (`testPageEnabled === false`) for remote disabling.

---

## 📊 4. Automated Email Recovery, Upsells & Lead Hygiene (Apps Script Version 3)

Your **Google Apps Script (`Version 3`)** runs two automated background triggers from **`PersonaLabs Academy <personalabsacademy@gmail.com>`** against [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md):

1. **Automated 25-Minute Abandoned Cart Recovery (`sendAbandonedCartRecoveryEmails` — every `15 mins`):**
   * Scans the `Logs` tab in `PersonaLabs Academy — Orders DB` for `INITIATED_CHECKOUT` rows older than **25 minutes**.
   * **Smart Buyer Skip:** Checks all `PAID_SUCCESS` emails across `Orders` and `Logs` first — if a visitor initiated checkout and bought minutes later, Column 21 is marked `SKIPPED (Purchased Course)` so they are **never** emailed accidentally.
   * Sends a high-deliverability recovery email (`plainText` + HTML + Udyam MSME CAN-SPAM footer) linking back to `https://personalabs.store`.
2. **Automated 12-Hour Post-Purchase Add-On Upsell (`sendPostPurchaseAddonUpsellEmails` — every `2 hours`):**
   * Scans `PAID_SUCCESS` rows older than **12 hours**.
   * Checks combined ownership across all previous purchases. If the buyer already owns both Bump #1 and Bump #2, marks Column 22 as `SKIPPED (Owns All Add-Ons)`.
   * Otherwise, emails their 1-click upgrade links (`https://personalabs.store/?upgrade=bump1` and/or `https://personalabs.store/?upgrade=bump2`) where Base Kit price is automatically `₹0` (`$0`).
3. **Manual Lead Review (`Orders DB` → `Logs` Tab):**
   * Check `PARTIAL_LEAD_CAPTURED` and yellow `INITIATED_CHECKOUT` rows daily and follow up with personalized WhatsApp/Email templates (promo codes `RIYA10` / `EARLY10` / `VIP20`) using [`docs/OUTREACH.md`](OUTREACH.md).

---

## 🚨 5. Mandatory Creative Guardrails ([`GEMINI.md`](../GEMINI.md))

Before producing any new Reel or editing copy, enforce all four rules codified in [`GEMINI.md`](../GEMINI.md):
1. **100% Fluid Dance Motion Mandate:** Every video Reel hook must open on real fluid video dance motion (`0:00` eye-contact smile, hip/waist sways, mudra hand choreography, or couture twirls). Never substitute Ken Burns static photo pans/zooms for video Reels.
2. **Carousels Only for Stills:** Static graphic slides, prompt comparisons, and infographics belong strictly inside `4:5` Carousels (`instagram-studio/carousels/`).
3. **100% Generic AI Model Terminology:** All scripts, burned-in captions, and descriptions must say `"hyper-realistic AI model"`, `"virtual creator"`, or `"AI influencer"` — zero regional, ethnic, or nationality tags.
4. **Canonical Folder Separation:** Keep runtime storefront images in [`assets/`](../assets/), brand DPs & raw video clips in `instagram-studio/source-assets/`, and course videos strictly out of Git (`videos-captioned/` is `.gitignore`d and `.vercelignore`d).

---

## 🧾 6. Historical Paid Meta Ads Summary (Halted `Nov 8, 2026`)

Paid campaigns remain **paused** to eliminate daily media burn and `18%` GST cash outflows. Full billing, Razorpay settlement UTRs, and creative metrics are preserved permanently in [`docs/META-ADS-CHANGELOG-AND-METRICS.md`](META-ADS-CHANGELOG-AND-METRICS.md):
* **Sales Campaign (`11–20 Oct`):** `₹4,449.99` GST-inclusive ad cash produced `5` Razorpay-settled orders (`₹2,986.00` revenue, **`₹597.20` AOV**; `₹890.00` ad cash/sale vs `≈ ₹583` breakeven ceiling).
* **Look C Dancing Reel Boost Test (`23–30 Oct`):** `₹536.00` GST-inclusive ad cash (`₹253.57` core test report) validated **`6.45%` outbound CTR**, **`₹34.83` CPM**, **`4,625` plays**, **`483` profile visits** (`₹0.525/visit`), and **`26` followers** — directly inspiring the **11 Master Dancing Reels** now running 100% organically.
* **Future Re-Entry Rule:** Never restart paid Meta Ads unless a capped retargeting/conversion test proves GST-inclusive ad cash per purchase stays **below `≈ ₹583`** across at least `10` verified orders.
