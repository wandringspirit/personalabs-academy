# 🏗️ PersonaLabs Academy — System & Funnel Architecture (`personalabs.store`)

Last Updated: **November 9, 2026 (`v2.9.5`)**

## 1. High-Level Architecture Overview

```text
Visitor (11 Organic Dancing Reels / Story Link Sticker / Manual DM / Bio Link)
   │
   ▼
https://personalabs.store/ (Vercel Global Edge CDN — 216.198.79.1, v2.9.5 / app.js?v=25)
   ├── Meta Pixel Conversion Tracking (`1661173205598260` — PersonaLabs Academy Pixel + Advanced Matching)
   │     └── Auto-fires: PageView, ViewContent, AddToCart, InitiateCheckout & Purchase (INR/USD)
   │
   ├── Geo-IP Detection & Currency Lock + Live Test Route (`/kjboavhpoieabpraegnaln`, enabled: true)
   │     ├── 🇮🇳 India IPs ──► Locked to INR (₹199 Flash [90% OFF] / ₹499 Launch [75% OFF ₹1,999]; Bumps +₹249 / +₹149)
   │     ├── 🌎 Global IPs ──► Locked to USD ($9 Flash [90% OFF] / $19 Launch [75% OFF $79]; Bumps +$9 / +$5)
   │     └── 🧪 Test Route ──► `/kjboavhpoieabpraegnaln` (₹1 INR / $1 USD per item + 1-click toggle)
   │
   ├── 10-Minute Persistent Flash Sale & 2-Tier Discount Ladder (sessionStorage)
   │     ├── Tier 1 (00:01–10:00): 90% OFF Flash Sale (₹199 / $9 vs. ₹1,999 / $79)
   │     └── Tier 2 (Post-Timer):  75% OFF Launch Offer (₹499 / $19 vs. ₹1,999 / $79 — saves ₹1,500 / $60)
   │
   ├── Country-Aware Checkout Input Validation & Early Lead Telemetry (app.js?v=25)
   │     ├── Strict Email Validation + Typo Detection (@gamil.com, @gmial.com, disposable blocklist)
   │     ├── 14-Country Phone Length & Prefix Validation (+91 IN 10-digit 6-9, +1 US/CA 10-digit, etc.)
   │     └── Logs `CTA_CLICKED_SCROLL` + `PARTIAL_LEAD_CAPTURED` on valid input blur before form submit
   │
   ├── Live Regional Payment Gateways (Zero Bypass / Verified TxId Required)
   │     ├── 🇮🇳 India (INR): Live Razorpay Standard Checkout (`rzp_live_TmX62nNGuBaTUc` — UPI/QR/Cards/NetBanking)
   │     └── 🌎 Global (USD): Live PayPal Smart Buttons SDK (`BAARfEN6...` — PayPal + International Cards, NO_SHIPPING)
   │
   ├── Real-Time Google Sheets Database (`1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc` — 22 Cols, `Logs` + `Orders` Tabs)
   │     ├── Event 1: CTA_CLICKED_SCROLL / PARTIAL_LEAD_CAPTURED / INITIATED_CHECKOUT (`Logs` Tab)
   │     ├── Event 2: PAID_SUCCESS (Green Row — logged to both `Logs` & clean `Orders` Tab + triggers DriveApp.addViewer)
   │     ├── Trigger 1: 25-Min Abandoned Cart Email Recovery (`sendAbandonedCartRecoveryEmails` via GmailApp)
   │     └── Trigger 2: 12-Hr Post-Purchase Add-On Upsell Email (`sendPostPurchaseAddonUpsellEmails` via GmailApp)
   │
   └── Post-Purchase Delivery, Printable PDF Receipt & Cryptographic Add-On Verification
         ├── 1. Interactive Member Vault: https://personalabs.store/course-vault/?email=...&tx=...&vt1=...&vt2=...
         ├── 2. Official Printable PDF Receipt: https://personalabs.store/course-vault/receipt.html (INR Tax Invoice / USD Receipt)
         └── 3. Private Google Drive 3-Folder Architecture (personalabsacademy@gmail.com + DriveApp.addViewer)
               ├── Folder 01: 01-Core-Course-Videos (`1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm` — 19 MP4s + Guide + Docs)
               ├── Folder 02: 02-Uncensored-NSFW-Addon-Videos (`10HGXWcRMR898lbQnTX41G--fPLKoBOvW` — 4 NSFW MP4s + Guide)
               └── Folder 03: 03-500-Viral-Hooks-And-Prompts-Pack (`1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN` — Prompt & Hooks HTMLs)
```

---

## 2. File & Directory Structure

| File / Folder | Purpose |
| :--- | :--- |
| [`index.html`](../index.html) | High-converting single-page storefront with Mobile Above-the-Fold Price Anchor Card (`lg:hidden`), 10-min flash timer, `"Nothing to lose. Everything to gain."` 100% Guarantee banner, interactive Revenue Chart & Earnings Calculator, AI Persona Lab sandbox, Dual Visual Order Bumps (`Uncensored Content Hack` & `500+ Viral Reel Hooks`), promo codes (`RIYA10`, `EARLY10`, `VIP20`), 14-country phone selector, live Razorpay (`INR`) & PayPal (`USD`) checkout, Meta Pixel (`1661173205598260`), Post-Purchase Upgrade Mode (`?upgrade=bump1` / `?upgrade=bump2`), and `receipt.html` prefetching. |
| [`styles.css`](../styles.css) | Custom design system tokens (`styles.css?v=9`), light/dark mode contrast enforcement (`color-scheme: light`), smooth pointer hover zoom (`hero-hover-zoom`), and mobile-first responsive utilities. |
| [`app.js`](../app.js) | Pricing state machine (`₹199` / `$9` Flash → `₹499` / `$19` Launch), Geo-IP currency detection, `/kjboavhpoieabpraegnaln` (`₹1 / $1`, `enabled: true`) live test mode, country-aware phone & email validator, live Razorpay & PayPal SDK orchestration, Meta Pixel + Advanced Matching dispatcher, FNV-1a (`vt1`/`vt2`) signature verification, promo code handler (`RIYA10`, `EARLY10`, `VIP20`), and Google Sheets webhook dispatcher (`?v=25`). |
| [`vercel.json`](../vercel.json) & [`.vercelignore`](../.vercelignore) | Zero-build static hosting configuration with rewrites for `/kjboavhpoieabpraegnaln`, instant cache revalidation on `index.html`/`app.js`/`styles.css`, `X-Robots-Tag: noindex, nofollow, noarchive` on `/course-vault/*` and `/kjboavhpoieabpraegnaln`, plus `.vercelignore` keeping docs/scripts/studio files off CLI bundles. |
| [`favicon.svg`](../favicon.svg) | Official `PersonaLabs Academy` (`PL` + Gold AI Spark) vector brand mark. |
| [`assets/`](../assets) | Runtime website storefront assets **only** (`8` files: `insta_profile_closeup_hd.jpg`, `images/hero_showcase.jpg`, `images/ai_workflow_studio.jpg`, `images/uncensored_hack_cover.png`, `images/persona_bali.jpg`, `images/persona_maya.jpg`, `images/persona_aira.jpg`, `images/persona_alex.jpg`). |
| [`course-vault/`](../course-vault) | **7 HTML files:** Interactive 5-Day / 18-Lesson Student Member Portal (`index.html`), `<50ms` A4 printable PDF Receipt (`receipt.html`), Core Bonus (`character-dna-prompt-bible.html`), cryptic FNV-1a VIP add-ons (`uncensored-vip-8f92a1c4.html`, `hooks-vip-3d7e91b2.html`), plus 2 backward-compatible redirect shims (`uncensored-content-hack.html`, `viral-hooks-and-autodm-pack.html`). |
| [`GEMINI.md`](../GEMINI.md) | Codified repository rules: 100% genuine fluid video dance motion Reels hook mandate, 100% generic AI model terminology, Comment-to-DM keywords, and canonical layout. |
| [`README.md`](../README.md) | Root repository overview, live production URLs, documentation index, and stack summary (`v2.9.5`). |
| [`instagram-studio/`](../instagram-studio) | Unified organic Instagram production studio: `reels-active-11/` (11 Master Dancing Video Reels + `thumbnails/`), `carousels/` (`01`–`06`), `source-assets/` (`character-assets/`, `raw-gemini-videos/`, `brand-dps/`, `bgm_master.mp3`), [`ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`](../instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md), [`CONTENT-CALENDAR-AND-CAPTIONS.md`](../instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md), and `archive/`. |
| [`scripts/`](../scripts) | Unified automation & QA tools (`build_all_11_organic_master_reels.py`, `audit_mobile_crossdevice.py`, `deep_audit_vault.py`) plus `archive/` (`22` legacy builders, `ig_bridge.js`, `remind_leads.ps1`, schedulers). |
| [`videos-captioned/`](../videos-captioned) | Local Git-ignored & `.vercelignore`d mirror of the `29` Google Drive deliverables (`01-Core-Course-Videos/`, `02-Uncensored-NSFW-Addon-Videos/`, `03-500-Viral-Hooks-And-Prompts-Pack/`). |
| [`docs/`](.) | All project operations, deployment, financial ledger, delivery, Apps Script, outreach, design, competitor, research, and roadmap documentation (`13` files). |

---

## 3. 4-Combination Add-On Access & Post-Purchase Upgrade State Machine

| Buyer State | Verified Signature Flags (`vt1`, `vt2`) | Unlocked in Vault & Google Drive (`DriveApp.addViewer`) | Locked Inside Vault (With 1-Click Upgrade) |
| :--- | :--- | :--- | :--- |
| **Combo 1: Basic Pack Only** | `vt1=none, vt2=none` | 19 Core Drive Videos + 18-Lesson Portal + 250+ Prompt Bible | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249 / +$9`) & 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149 / +$5`) |
| **Combo 2: Basic + Uncensored Hack** | `vt1=valid, vt2=none` | Core + 🔓 4 Uncensored NSFW Videos & VIP Guide | 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149 / +$5` — Bump #1 never charged again) |
| **Combo 3: Basic + 500+ Viral Hooks** | `vt1=none, vt2=valid` | Core + 🔓 500+ Viral Reel Hooks & Auto-DM Pack | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249 / +$9` — Bump #2 never charged again) |
| **Combo 4: Full VIP Bundle** | `vt1=valid, vt2=valid` | 🔓 Everything Unlocked (`₹597` India / `$23` Global Flash) | None — Full VIP Access Badge displayed |
