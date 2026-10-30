# 📋 PersonaLabs Academy — Changelog (`CHANGES.md`)

## v2.9.3 — 2026-10-30 (Latest Release)
- **Financial Ledger Reconciled Against Meta Billing & Razorpay Settlements ([`docs/META-ADS-CHANGELOG-AND-METRICS.md`](META-ADS-CHANGELOG-AND-METRICS.md)):**
  - Real all-time figures: **`₹4,986.00`** paid to Meta Ads (8 UPI top-ups, GST-inclusive, balance now `₹0.00`) vs **`₹2,986.00`** settled from **5** customer orders, a **`-₹2,000.00`** net position. Replaces the earlier `-₹261` estimate, which stopped at 16 Oct.
  - Added the missing 17–20 Oct campaign spend (`₹1,885.90`), Order #5 (`₹597`, settled 21 Oct), and the full reel-boost billing (`₹536.00`, not `₹299.21`).
  - Added a breakeven rule (ad cash per sale must stay below `≈ ₹583`; all-time it is `₹890`) and fixed the ledger header Pixel ID to `1661173205598260`.
- **Meta Ads Creative Test Benchmark Validation ([`docs/META-ADS-CHANGELOG-AND-METRICS.md`](META-ADS-CHANGELOG-AND-METRICS.md)):**
  - Completed initial paid test (`₹253.57` media spend / `₹299.21` cash with 18% GST) validating viral reception on Look C Indian Model dancing reels.
  - Achieved **`6.45%` outbound CTR**, **`₹34.83` CPM** (10x cheaper than industry average), and **`₹0.525` cost per profile visit** across 7,281 impressions and 5,671 unique accounts.
  - Drove **483 profile visits**, **492 link clicks**, **4,625 plays** on the primary boosted Reel, and **26 real followers** to `@personalabsacademy`.
- **5 Master Ad Hooks Re-Sequenced for Opening 0:00 Eye-Contact Hook ([`ads-ready/dancing-ad-hooks/`](../ads-ready/dancing-ad-hooks/)):**
  - Re-rendered all 5 high-converting 1080×1920 video ads (`Hottest_Hook_01` through `05`) so each opens immediately at `0:00` with the model's direct eye-contact radiant smile.
  - Cleaned all UTF-8 typography to eliminate square glyph box artifacts in Windows rendering.
  - Encoded with `-movflags +faststart` for zero-latency streaming on Meta Ads Manager and Instagram.

## v2.9.2 — 2026-10-13
- **Mobile Above-the-Fold Instant Access & Price Anchor Card ([`index.html`](../index.html), [`app.js`](../app.js)):**
  - Added a dedicated mobile-first (`lg:hidden`) **Above-the-Fold Instant Access & Price Anchor Card** directly below the 3-Panel Viral AI Reels Hero image (`#sec-overview`) with live dynamic pricing (`₹1,999` → `₹249` / `$79` → `$9`), 4-bullet deliverable summary, pulsing **`⚡ Unlock Instant Access — ₹249 →`** button (`scrollToCheckout('Hero Above-Fold CTA')`), and UPI/GPay/PhonePe trust strip so mobile Instagram Reels visitors don't have to scroll 5,000px to find the offer.
  - Added a direct checkout jump CTA button (`🚀 Join Risk-Free Now — ₹249 →`) inside the **100% Money-Back Guarantee** card (`scrollToCheckout('Guarantee Section CTA')`).
- **Full-Funnel CTA Click (`CTA_CLICKED_SCROLL`) & Early Partial Lead (`PARTIAL_LEAD_CAPTURED`) Telemetry (`?v=22`):**
  - Upgraded [`scrollToCheckout()`](../app.js) to log `CTA_CLICKED_SCROLL` (with the exact CTA button source label) to the Google Sheets `Orders DB` and fire Meta Pixel `AddToCart` once per session when a visitor taps any CTA button.
  - Added [`capturePartialLeadIfValid()`](../app.js) to automatically capture and log `PARTIAL_LEAD_CAPTURED` to `Orders DB` as soon as a visitor enters a valid Email address (`onblur`) or completes a valid 10-digit mobile number (`oninput`/`onblur`), even if they drop off before submitting the full checkout form.

## v2.9.1 — 2026-10-13
- **Live & 6-Day Scheduled Instagram Queue (`@personalabsacademy`) ([`instagram-studio/CONTENT-CALENDAR.md`](../instagram-studio/CONTENT-CALENDAR.md)):**
  - Published and pinned **Carousel #01** (`5 Slides, 4:5` — [`https://www.instagram.com/p/DeZdiZ2EuBf/`](https://www.instagram.com/p/DeZdiZ2EuBf/)) to the top of `@personalabsacademy` alongside live **Reel #01** ([`DeWdJplElw6`](https://www.instagram.com/personalabsacademy/reel/DeWdJplElw6/)) and **Reel #02** ([`DeZd2Z6o-Be`](https://www.instagram.com/p/DeZd2Z6o-Be/)).
  - Rendered and scheduled **6 consecutive daily posts/Reels (`Tue Oct 13 – Sun Oct 18, 2026 at 7:30 PM IST / 19:30`)** in Meta Business Suite Content Planner:
    1. **Tue, Oct 13 (`19:30 IST`):** `Reel #03 (Mobile Creator Pipeline)` — Scheduled ID: `1796375885019195`
    2. **Wed, Oct 14 (`19:30 IST`):** `Reel #04 (Raw iPhone Realism Secret)` — Scheduled ID: `1517688583525114`
    3. **Thu, Oct 15 (`19:30 IST`):** `Carousel #02 (Smartphone Realism Prompts — 5 Slides)` — Scheduled ID: `2220488025553695`
    4. **Fri, Oct 16 (`19:30 IST`):** `Reel #05 (1 Static Photo to 4K Viral Reel)` — Scheduled ID: `1099506249107288`
    5. **Sat, Oct 17 (`19:30 IST`):** `Carousel #03 (5-Day AI Influencer Roadmap — 5 Slides)` — Scheduled ID: `908070545570409`
    6. **Sun, Oct 18 (`19:30 IST`):** `Reel #06 (₹50,000 Studio Shoot vs. 20-Min AI Creator Page)` — Scheduled ID: `1622233036055930`
  - Added reusable studio asset builder ([`instagram-studio/scripts/build_batch_1b_5days.py`](../instagram-studio/scripts/build_batch_1b_5days.py)) and local file bridge ([`instagram-studio/scripts/ig_bridge.js`](../instagram-studio/scripts/ig_bridge.js)).
- **Weekly Sunday 10:00 AM IST Instagram Batch Refill Automation (`/schedule`):**
  - Activated recurring cron automation **`Weekly Instagram Batch Refill (@personalabsacademy)`** (`CRON_TZ=Asia/Kolkata 0 10 * * 0`) to automatically generate the next 7-day Reel/Carousel batch every Sunday morning before Sunday night's scheduled Reel goes live.
- **Meta Ads Campaign #1 (`100/100` Opportunity Score) & Root `README.md`:**
  - Applied Meta Advantage+ Creative `Video touch-ups` on **`IN - Sales - AI Influencer Launch Kit (INR)`**, reaching a **`100/100` Opportunity Score** (`₹302.29` spent, `273` impressions, `236` reach).
  - Added root [`README.md`](../README.md) indexing all architecture, operations, and Instagram Studio files.

## v2.9.0 — 2026-10-12
- **Official Printable PDF Tax Invoice / Payment Receipt ([`course-vault/receipt.html`](../course-vault/receipt.html), [`app.js`](../app.js), [`index.html`](../index.html)):**
  - Replaced the plain-text `.txt` download with a printable A4 invoice/receipt ([`course-vault/receipt.html`](../course-vault/receipt.html)) displaying Udyam MSME Registration (`UDYAM-UP-43-0208040`), itemized deliverables, Razorpay/PayPal Transaction ID, Order ID, and direct lifetime portal & Google Drive links.
  - Added currency-aware tax/processing logic: displays **`Tax Invoice`** + **`Digital GST / Processing: Included (₹0.00)`** for Indian (`INR`) orders, and **`Payment Receipt`** + **`Digital Delivery & Processing: Included ($0.00)`** (zero mention of GST) for International (`USD`) orders.
  - Optimized for **`<50ms` instant tab opening** by removing the blocking automatic `window.print()` spooler call on tab load, making Google Fonts non-render-blocking (`media="print" onload="this.media='all'"`), and prefetching `course-vault/receipt.html` in [`index.html`](../index.html).
- **Secret Live Payment Test Route (`/kjboavhpoieabpraegnaln` — `₹1 INR / $1 USD` per item) ([`app.js`](../app.js), [`index.html`](../index.html), [`vercel.json`](../vercel.json)):**
  - Configured [`https://www.personalabs.store/kjboavhpoieabpraegnaln`](https://www.personalabs.store/kjboavhpoieabpraegnaln) (`PAYMENT_GATEWAY_CONFIG.testSandboxPage`) to charge **₹1 INR** (Razorpay) or **$1 USD** (PayPal) per item (`Base Kit`, `Bump #1`, `Bump #2`) with an on-screen 1-click currency switcher (`?v=21`).
- **Automated 25-Min Cart Recovery & 12-Hour Post-Purchase Add-On Upsell Email Engine ([`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md)):**
  - Deployed **Version 3** of the Google Apps Script Web App (`AKfycbzxKG...`) with two time-driven `GmailApp` triggers under `personalabsacademy@gmail.com`:
    1. `sendAbandonedCartRecoveryEmails` (every 15 mins): Sends recovery emails to `INITIATED_CHECKOUT` leads after 25 minutes while automatically skipping anyone who subsequently completed a `PAID_SUCCESS` order.
    2. `sendPostPurchaseAddonUpsellEmails` (every 2 hours): Sends 1-click upgrade links (`/?upgrade=bump1` and `/?upgrade=bump2`) 12 hours after purchase to students who did not buy both add-ons.
  - Added full plain-text parity (`plainText`), `replyTo: 'personalabsacademy@gmail.com'`, and a CAN-SPAM compliant MSME footer to ensure Primary Inbox deliverability.
- **Storefront UI Polish & Campaign #1 Live Activation (`₹500/day` CBO) ([`index.html`](../index.html), [`docs/LAUNCH_OPERATIONS_MANUAL.md`](LAUNCH_OPERATIONS_MANUAL.md)):**
  - Updated Order Bump #1 (*Uncensored Content Hack*) thumbnail to [`assets/images/uncensored_hack_cover.png`](../assets/images/uncensored_hack_cover.png) and moved the `🌴 Bali Travel` persona pill to the first position in `#sec-ai-lab`.
  - Published **Campaign #1 (`IN - Sales - AI Influencer Launch Kit (INR)`)** live in Meta Ads Manager at **₹500.00/day** (Instagram Reels & Stories), achieving **`3.52% – 5.56%` Link CTR** and **78 engagements** on initial delivery.
- **GitHub Repository Renamed to `wandringspirit/personalabs-academy` & 3-Agent Autonomous Instagram Studio ([`docs/DEPLOY.md`](DEPLOY.md), [`instagram-studio/`](../instagram-studio)):**
  - Renamed the official GitHub repository from `wandringspirit/ai-influencer-course-website` to **[`wandringspirit/personalabs-academy`](https://github.com/wandringspirit/personalabs-academy)** and updated all documentation references.
  - Created the **3-Agent Autonomous Instagram Team** (`ig-content-studio`, `ig-copy-and-funnel`, `instagram-creator-operator`) and generated Batch #1 (`01-Pinned-Carousel-5Slides/`, `02-Organic-Reels/`, and [`CONTENT-CALENDAR-AND-CAPTIONS.md`](../instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md)) for `@personalabsacademy`.

## v2.8.2 — 2026-10-11
- **Live Meta Pixel (`1661173205598260`) & Ad Account (`2218391099056783`) Connected ([`app.js`](../app.js), [`index.html`](../index.html), [`docs/ROADMAP.md`](ROADMAP.md)):**
  - Created **`PersonaLabs Academy Ads`** (`ID: 2218391099056783`, `Currency: INR`, `Time Zone: Asia/Kolkata`) and **`PersonaLabs Academy Pixel`** (`ID: 1661173205598260`) in Meta Business Suite (`business_id=1761523878300294`) and linked them under *Connected Assets*.
  - Wired `metaPixelId: '1661173205598260'` in [`app.js`](../app.js) (`?v=16`) and added the `<noscript>` beacon in [`index.html`](../index.html) to automatically track `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, and `Purchase` (with dynamic `INR`/`USD` values).
  - Created Draft Sales Campaign **`IN - Sales - AI Influencer Launch Kit (INR)`** (`Campaign ID: 120251814625900152`) in Meta Ads Manager.
- **Vercel Global Edge CDN Auto-Deploy & Privacy-Protected Git Author ([`docs/DEPLOY.md`](DEPLOY.md)):**
  - Completed DNS migration of `personalabs.store` (`A @` → `216.198.79.1`) and `www.personalabs.store` (`CNAME www` → `847062401d7e0c68.vercel-dns-017.com`) to Vercel Global Edge CDN.
  - Configured local Git author to GitHub's privacy-preserving `wandringspirit <209062033+wandringspirit@users.noreply.github.com>` address so every `git push origin main` triggers an instant automatic Vercel Hobby deployment without exposing any personal email.
- **8K Exact-Face Saree Profile Portraits & ManyChat Auto-DM Flow ([`assets/`](../assets), [`docs/OUTREACH.md`](OUTREACH.md)):**
  - Generated 8K DSLR-restored portraits from `demo.mp4` ([`assets/insta_dp_exact_face_1080x1080.jpg`](../assets/insta_dp_exact_face_1080x1080.jpg) & [`assets/insta_saree_full_portrait_hd.jpg`](../assets/insta_saree_full_portrait_hd.jpg)) with zero facial drift and uploaded to `@personalabsacademy`.
  - Configured ManyChat Comment-to-DM automation (`AI, LAUNCH, MODEL, REEL, HACK, LINK, PROMPT, VIP`) with 2-step Opening DM (`🚀 Send me the link` → `🚀 Unlock Launch Kit` → `https://personalabs.store`).
- **107-Ad Meta Ad Library Competitor Spy Scan ([`docs/ROADMAP.md`](ROADMAP.md), [`docs/COMPETITORS.md`](COMPETITORS.md)):**
  - Scanned 107 active video ads across 4 Meta Ad Library tabs (`India "AI Influencer"`, `India "AI Model" Instagram`, `US "AI Influencer"`, `earlycaves`) and extracted the top 7 long-running winners (`MindBrix EdTech`, `Digitalvalut Media`, `Varnexa Digital`, `Shreya Xtrader`, `FlyAds.ai`, `AI Video Skool`, `russestudiosv`) + 3 Battle-Tested Headlines and Primary Text Options (`A`, `B`, `C`).

## v2.8.1 — 2026-10-11
- **Dedicated `personalabsacademy@gmail.com` 3-Folder Google Drive + New Orders DB Sheet Connected ([`app.js`](../app.js), [`index.html`](../index.html), [`course-vault/index.html`](../course-vault/index.html), [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md)):**
  - Connected the new Google Sheets Order & Lead Database (`1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc`) and live Apps Script Web App (`AKfycbzxKGXLOy1g2TebrWch0aGHdvTp7iYffCULRApdjlEerdum6p2Sj4mAWa5awzM_JrOm`) owned 100% by **`personalabsacademy@gmail.com`**.
  - Wired all 3 Restricted Google Drive deliverable folders (`01-Core-Course-Videos`: `1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`, `02-Uncensored-NSFW-Addon-Videos`: `10HGXWcRMR898lbQnTX41G--fPLKoBOvW`, `03-500-Viral-Hooks-And-Prompts-Pack`: `1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`) across `DriveApp.addViewer` and the on-screen/receipt delivery links (`?v=15`).

## v2.8.0 — 2026-10-11
- **Live PayPal Smart Buttons Checkout Activated for International (`USD`) ([`app.js`](../app.js), [`index.html`](../index.html)):**
  - Configured the live PayPal Business Client ID (`BAARfEN6AEZqn7tB4CWb08mUBhJqBYzxwPkmMnxJNkQ77mGxuYUiisrNiiYhtg75Gg12nHMXKAS38v_p1E`) in `PAYMENT_GATEWAY_CONFIG.paypal.clientId` ([`app.js`](../app.js)).
  - Verified live PayPal JS SDK loading (`https://www.paypal.com/sdk/js?client-id=...&currency=USD`, `HTTP 200 OK`) and automatic mounting of the official Gold **PayPal** button + Dark **Debit or Credit Card** button for all international (`USD`) visitors.
  - Configured `application_context` (`brand_name: 'PersonaLabs Academy'`, `shipping_preference: 'NO_SHIPPING'`, `user_action: 'PAY_NOW'`) and `soft_descriptor: 'PERSONALABS'` so international buyers get a digital-goods checkout with no shipping address prompts.
  - Enforced strict live transaction ID verification across both **Razorpay (`INR`)** and **PayPal (`USD`)** (`?v=14`).
  - Kept the PayPal `Secret key 1` strictly out of client-side code and GitHub commits.
- **Static Hosting Configuration & Roadmap Action Table ([`vercel.json`](../vercel.json), [`docs/ROADMAP.md`](ROADMAP.md), [`docs/DEPLOY.md`](DEPLOY.md), [`docs/ARCHITECTURE.md`](ARCHITECTURE.md)):**
  - Added [`vercel.json`](../vercel.json) with zero-build static headers and `X-Robots-Tag: noindex, nofollow` protection on `/course-vault/*` so `personalabs.store` can switch from Netlify Free (300-credit cap) to Vercel Free (100 deploys/day from the private GitHub repo) in 3 clicks whenever needed.
  - Restructured [`docs/ROADMAP.md`](ROADMAP.md) with a unified **`🗓️ Date-Wise & Task-Wise Master Execution Calendar`** tracking all completed milestones and upcoming daily actions.

## v2.7.2 — 2026-10-11
- **Country-Aware Phone Number & Strict Email Validation ([`app.js`](../app.js), [`index.html`](../index.html)):**
  - Added `<select id="phone-country-select">` (`+91 IN`, `+1 US/CA`, `+44 GB`, `+61 AU`, `+971 AE`, `+65 SG`, `+49 DE`, `+33 FR`, `+31 NL`, `+966 SA`, `+60 MY`, `+27 ZA`, `+55 BR`, `OTHER`) automatically synced to the visitor's IP country.
  - Added `PHONE_COUNTRY_RULES` in [`app.js`](../app.js) enforcing each country's exact subscriber digit length (`10` digits for `IN`/`US`/`CA`/`GB`, `9` digits for `AE`/`AU`/`FR`/`NL`/`SA`/`ZA`, `8` digits for `SG`, `10–11` for `DE`/`BR`), automatically stripping leading `0`s or pasted dial prefixes, validating starting digits (e.g. `6–9` for India `+91`), and rejecting repeated/dummy digits (`/(.)\1{5,}/`).
  - Added strict RFC email validation (`validateEmailField`) with real-time domain typo detection (`gamil.com`, `gmial.com`, `gmail.co`, `yaho.com`, `outlok.com`, etc.) and disposable/fake domain blocking.

## v2.7.1 — 2026-10-11
- **Official Support Email Updated to `personalabsacademy@gmail.com` ([`index.html`](../index.html), [`app.js`](../app.js)):**
  - Replaced all occurrences of `sayana.official.help@gmail.com` across the website support footer, Legal & Refund Policy modal, AI Assistant, and downloadable `.txt` receipts with **`personalabsacademy@gmail.com`** (`?v=12`).
- **Live Razorpay Checkout Activated for India (`INR`) ([`app.js`](../app.js), [`index.html`](../index.html)):**
  - Configured `PAYMENT_GATEWAY_CONFIG.razorpay.keyId = 'rzp_live_TmX62nNGuBaTUc'` in [`app.js`](../app.js).
  - Added `ensureRazorpaySdkLoaded()` and `openLiveRazorpayCheckout()` so clicking **Make Payment** in `INR` always launches the live Razorpay Standard Checkout modal (`UPI / GPay / PhonePe / Paytm / Cards / Netbanking`) with rich order `notes` (`order_id`, `customer_email`, `customer_phone`, `items`, `bump1_nsfw`, `bump2_hooks`).
  - Blocked simulated `PLA-...` preview IDs in `INR` and required live Google Sheet `lookupOrder` verification in `openSignInModal()`.
  - Kept the Razorpay `Live Key Secret` strictly out of client-side code and GitHub commits to protect account security.

## v2.6.1 — 2026-10-11
- **2-Tier Discount Ladder When 10-Min Flash Offer Ends ([`app.js`](../app.js)):**
  - Updated `renderPricing()`, `renderOfferTimerDisplay()`, and `handleOfferExpiredTransition()` so that after the 10-minute `₹249` (`$9`) fast-action bonus ends, `#anchor-strike-price` continues crossing out the original retail price **`₹1,999` (`$79`)** next to **`₹499` (`$19`)**, `#checkout-save-badge` displays **`SAVE 75% OFF ₹1,999 (LAUNCH OFFER)`** in emerald green, and the urgency banners highlight that the buyer still saves **`₹1,500` (`$60`)** off retail (`🔥 75% OFF ACTIVE` / `SAVE 75%`).
- **"Nothing to lose. Everything to gain." Guarantee Banner Typography & Spacing Fix ([`index.html`](../index.html)):**
  - Fixed side-edge fading on `"Everything to gain."` and `"100% Money-Back Guarantee"` by replacing Tailwind `via-*` gradient classes with explicit 100%-opaque CSS `linear-gradient(90deg, ...)` hex stops.
  - Balanced the Left Guarantee Card (`100% Money-Back Guarantee` + Gold Seal SVG + 3 concise guarantee paragraphs) and Right 3 FAQ Cards so the gold badge and text align evenly with zero empty white space below the badge.
- **Reverted Website Avatar & Order Bump #1 Thumbnail to Original Photo:**
  - Restored [`assets/images/creator_avatar.jpg`](../assets/images/creator_avatar.jpg) and [`assets/images/uncensored_hack_cover.jpg`](../assets/images/uncensored_hack_cover.jpg) to the original website maroon saree back-portrait photo (`?v=12` in [`index.html`](../index.html)).

## v2.6.0 — 2026-10-11
- **"Nothing to lose. Everything to gain." — 100% Money-Back Guarantee Section & Graphic:**
  - Recreated the **"Nothing to lose. Everything to gain."** 2-column Guarantee + 3 Key Answers layout matched to the PersonaLabs Academy dark/amber/fuchsia theme right below the Hero & Description in [`index.html`](../index.html) (`lines 270–360`) so it is immediately visible at the top of the page.
  - Generated the standalone high-resolution `1600x900` banner graphic at [`assets/images/nothing_to_lose_guarantee.png`](../assets/images/nothing_to_lose_guarantee.png).
- **Dual-Currency Video Ad Variants (India `INR ₹249` vs. Global `USD $9`):**
  - Split all 3 promotional 9:16 Video Ads into two region-specific folders (`6` rendered `.mp4` ads in total) with dedicated voiceovers, captions, and CTA end-cards:
    - [`ads-ready/01-India-INR-Ads/`](../ads-ready/01-India-INR-Ads): Shows **only `₹249` (`Reg. ₹1,999`)** and `₹15,000` in voiceover/captions (zero `$` symbols).
    - [`ads-ready/02-Global-USD-Ads/`](../ads-ready/02-Global-USD-Ads): Shows **only `$9` (`Reg. $49`)** and `$500` in voiceover/captions (zero `₹` symbols).

## v2.5.1 — 2026-10-11
- **Website Avatar & Order Bump #1 Thumbnail Updated to Approved AI Character:**
  - Replaced [`assets/images/creator_avatar.jpg`](../assets/images/creator_avatar.jpg) (`Created by PersonaLabs Academy` header avatar & checkout modal avatar) and [`assets/images/uncensored_hack_cover.jpg`](../assets/images/uncensored_hack_cover.jpg) (Order Bump #1 `Uncensored Content Hack` thumbnail) with the spotless, mole-free square portrait of the approved blonde emerald-top cafe AI Influencer persona.
  - Bumped cache-busting query strings to `?v=11` in [`index.html`](../index.html).

## v2.5.0 — 2026-10-11
- **Automatic Google Drive Email Whitelisting (`DriveApp.addViewer` — Option 2):**
  - Updated [`app.js`](../app.js) (`logOrderToGoogleSheet` & `completePaymentSuccess`) to transmit explicit Google Drive permission flags (`grantCoreDrive`, `grantNsfwDrive`, `grantHooksDrive`) after merging initial and post-purchase add-on upgrades.
  - Updated the Google Apps Script backend in [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md) so all 3 Google Drive deliverable folders (`01-Core-Course-Videos`, `02-Uncensored-NSFW-Addon-Videos`, `03-500-Viral-Hooks-And-Prompts-Pack`) remain **Restricted (Private)** and automatically grant Viewer permission to each verified buyer's Gmail address (`DriveApp.getFolderById(...).addViewer(buyerEmail)`), logging the granted folders in Column 20 (`Google Drive Access Granted`).
  - Updated checkout email field label in [`index.html`](../index.html) to `Email (Gmail for instant Google Drive access) *`.
- **Unguessable VIP Guide URLs & Cryptographic Access Signatures (`vt1` / `vt2`):**
  - Renamed `course-vault/uncensored-content-hack.html` $\rightarrow$ [`course-vault/uncensored-vip-8f92a1c4.html`](../course-vault/uncensored-vip-8f92a1c4.html) and `course-vault/viral-hooks-and-autodm-pack.html` $\rightarrow$ [`course-vault/hooks-vip-3d7e91b2.html`](../course-vault/hooks-vip-3d7e91b2.html).
  - Removed all plain-text VIP guide filenames from HTML source code so *View Source* cannot leak them; URLs are now assembled dynamically in JS only after verifying deterministic signatures (`vt1`/`vt2`) or live Google Sheet `lookupOrder` responses.
- **Documentation Migration to `/docs` & Phase 3 Video Ads:**
  - Moved all 10 project documentation files (`ARCHITECTURE.md`, `CHANGES.md`, `COMPETITORS.md`, `DEPLOY.md`, `DESIGN.md`, `GOOGLE-SHEETS-DATABASE-SETUP.md`, `OUTREACH.md`, `RESEARCH.md`, `ROADMAP.md`, `SEO.md`) into [`/docs`](.).
  - Added complete word-for-word scripts for the **3 Promotional 9:16 Video Ads** to [`docs/ROADMAP.md`](ROADMAP.md) and generated the approved consistent AI Influencer persona (`ads-ready/character-assets/`) + 3 rendered `.mp4` Video Ads (`ads-ready/`).

## v2.4.0 — 2026-10-11
- **Hero & Order Bump Visual Refresh:**
  - Replaced `assets/images/hero_showcase.jpg` with the updated 3-panel high-contrast `CREATE VIRAL AI REELS / EARN LAKHS EVERY MONTH` showcase (`2.5M | 1.2M | 3.6M`).
  - Replaced `assets/images/uncensored_hack_cover.jpg` with the original maroon saree back-portrait thumbnail.
  - Added smooth pointer hover zoom (`scale(1.035)` on hero banner, `scale(1.10)` on order bump thumbnails).
- **Single-Line Top Urgency Bar:**
  - Locked `⚡ URGENT`, `88% OFF FLASH SALE`, countdown timer `⏱ 10:00`, and `👁 viewing now` pill onto a single horizontal row (`flex-nowrap whitespace-nowrap`) so `viewing now` never wraps below the timer.
- **Light & Dark Mode Contrast Hardening:**
  - Enforced `color-scheme: light` on light mode and darkened secondary slate text (`#475569` / `#0f172a`) so browser auto-darkening extensions cannot wash out `Created by` or Order Bump descriptions.
- **Automated Course Video Processing Pipeline (23 Videos):**
  - Removed legacy `INVISION ACADEMY` and `invisionacademy.com` floating watermarks across all course videos.
  - Translated Hindi voiceovers into clean International English subtitles burned in **Style 1 (Netflix/YouTube Pro Dark Pill Box)** while preserving 100% original audio (`-c:a copy`).
  - Organized deliverables into 3 Google Drive folders (`01-Core-Course-Videos`, `02-Uncensored-NSFW-Addon-Videos`, `03-500-Viral-Hooks-And-Prompts-Pack`).

## v2.3.0 — 2026-10-10
- **4-Combination Add-On Lock & 1-Click Post-Purchase Upgrade Flow:**
  - Styled Order Bump #2 (`500+ Viral Reel Hooks & Auto-DM Pack`) as a visual card matching Order Bump #1 (`Uncensored Content Hack`).
  - Added `?upgrade=bump1` and `?upgrade=bump2` checkout mode in `app.js` so Basic Pack students can unlock individual add-ons later from inside `course-vault/index.html` without re-paying for the Base Course.

## v2.2.0 — 2026-10-10
- **Live Google Sheets Order & Lead Database:**
  - Connected `app.js` to live Google Apps Script Web App (`PersonaLabs Academy — Orders DB`), logging both `INITIATED_CHECKOUT` (abandoned cart leads) and `PAID_SUCCESS` (verified buyers).
- **Brand Identity & Continuous Deployment:**
  - Added `favicon.svg` (`PL` monogram) and linked GitHub (`wandringspirit/ai-influencer-course-website`) to Netlify (`personalabs.store`).
