# 🏗️ PersonaLabs Academy — System & Funnel Architecture (`personalabs.store`)

## 1. High-Level Architecture Overview

```
Visitor (Instagram Reel / Bio Link / ManyChat DM / Meta Video Ad)
   │
   ▼
https://personalabs.store/ (Vercel Global Edge CDN — 216.198.79.1, v2.8.2)
   ├── Meta Pixel Conversion Tracking (`1661173205598260` — PersonaLabs Academy Pixel)
   │     └── Auto-fires: PageView, ViewContent, AddToCart, InitiateCheckout & Purchase (INR/USD)
   │
   ├── Geo-IP Detection & Currency Lock
   │     ├── 🇮🇳 India IPs ──► Locked to INR (₹249 Flash / ₹499 Launch Offer — 75% OFF ₹1,999)
   │     └── 🌎 Global IPs ──► Locked to USD ($9 Flash / $19 Launch Offer — 75% OFF $79)
   │
   ├── 10-Minute Persistent Flash Sale & 2-Tier Discount Ladder (localStorage)
   │     ├── Tier 1 (00:01–10:00): 88% OFF Flash Offer (₹249 / $9 vs. ₹1,999 / $79)
   │     └── Tier 2 (Post-Timer):  75% OFF Launch Offer (₹499 / $19 vs. ₹1,999 / $79 — saves ₹1,500 / $60)
   │
   ├── Country-Aware Checkout Input Validation (app.js)
   │     ├── Strict Email Validation + Typo Detection (@gamil.com, @gmial.com, disposable blocklist)
   │     └── 14-Country Phone Length & Prefix Validation (+91 IN 10-digit 6-9, +1 US/CA 10-digit, +971 AE 9-digit, etc.)
   │
   ├── Live Regional Payment Gateways (Zero Bypass / Verified TxId Required)
   │     ├── 🇮🇳 India (INR): Live Razorpay Standard Checkout (`rzp_live_TmX62nNGuBaTUc` — UPI/QR/Cards/NetBanking)
   │     └── 🌎 Global (USD): Live PayPal Smart Buttons SDK (`BAARfEN6...` — PayPal + International Cards, NO_SHIPPING)
   │
   ├── Real-Time Google Sheets Order & Lead Database (`1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc`)
   │     ├── Event 1: INITIATED_CHECKOUT (Yellow Row — captures WhatsApp/Email before payment)
   │     └── Event 2: PAID_SUCCESS (Green Row — logs verified TxId + triggers DriveApp.addViewer)
   │
   └── Post-Purchase Delivery & Cryptographic Add-On Verification
         ├── 1. Interactive Member Vault: https://personalabs.store/course-vault/?email=...&tx=...&vt1=...&vt2=...
         └── 2. Private Google Drive 3-Folder Architecture (personalabsacademy@gmail.com + DriveApp.addViewer)
               ├── Folder 01: 01-Core-Course-Videos (`1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`)
               ├── Folder 02: 02-Uncensored-NSFW-Addon-Videos (`10HGXWcRMR898lbQnTX41G--fPLKoBOvW`)
               └── Folder 03: 03-500-Viral-Hooks-And-Prompts-Pack (`1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`)
```

---

## 2. File & Directory Structure

| File / Folder | Purpose |
| :--- | :--- |
| [`index.html`](../index.html) | High-converting single-page storefront with 10-min flash timer, "Nothing to lose. Everything to gain." 100% Guarantee section, inline live viewer counter, dual order bumps, country-aware phone selector, live Razorpay (`INR`) & PayPal (`USD`) checkout, Meta Pixel (`1661173205598260`), and Post-Purchase Upgrade Mode (`?upgrade=bump1` / `?upgrade=bump2`). |
| [`styles.css`](../styles.css) | Custom design system tokens, light/dark mode contrast enforcement, smooth pointer hover zoom (`hero-hover-zoom`), and mobile-first responsive utilities. |
| [`app.js`](../app.js) | Pricing state machine (`Option A1` 2-tier discount ladder), Geo-IP currency detection, country-aware phone & email validator, live Razorpay & PayPal SDK orchestration, Meta Pixel event dispatcher (`1661173205598260`), FNV-1a (`vt1`/`vt2`) signature verification, and Google Sheets webhook dispatcher. |
| [`vercel.json`](../vercel.json) | Zero-build static hosting configuration with instant cache revalidation on `index.html`/`app.js`/`styles.css` and `X-Robots-Tag: noindex, nofollow` on `/course-vault/*`. |
| [`favicon.svg`](../favicon.svg) | Official `PersonaLabs Academy` (`PL` + Gold AI Spark) vector brand mark. |
| [`assets/insta_dp_exact_face_1080x1080.jpg`](../assets/insta_dp_exact_face_1080x1080.jpg) | 8K DSLR-restored 1:1 square Instagram & Facebook Page profile picture matching `demo.mp4` with zero facial drift. |
| [`course-vault/index.html`](../course-vault/index.html) | Interactive Student Member Portal with 5-Day curriculum, progress tracking, cryptographic + server-side add-on access control (`vt1` & `vt2`), and 1-click post-purchase upgrade cards. |
| [`course-vault/uncensored-vip-8f92a1c4.html`](../course-vault/uncensored-vip-8f92a1c4.html) | Order Bump #1 Unguessable VIP Guide: Uncensored Content Hack, FaceFusion workflow, and safe multi-platform funneling. |
| [`course-vault/hooks-vip-3d7e91b2.html`](../course-vault/hooks-vip-3d7e91b2.html) | Order Bump #2 Unguessable VIP Guide: 500+ Viral Reel Hooks & ManyChat Comment-to-DM Automation Scripts. |
| [`course-vault/character-dna-prompt-bible.html`](../course-vault/character-dna-prompt-bible.html) | Core Bonus: 250+ AI Character DNA & Face-Lock Master Prompts. |
| [`docs/ROADMAP.md`](ROADMAP.md) | Single unified source of truth: Date-Wise & Task-Wise Master Execution Calendar, Meta Ads Campaign #1 & #2 step-by-step guide, Competitor Spy breakdown, and 30-Day Viral Reels Calendar. |
| [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md) | Live Google Apps Script webhook documentation, `DriveApp.addViewer` auto-whitelisting, and 20-column schema reference. |

---

## 3. 4-Combination Add-On Access & Post-Purchase Upgrade State Machine

| Buyer State | Verified Signature Flags (`vt1`, `vt2`) | Unlocked in Vault & Google Drive (`DriveApp.addViewer`) | Locked Inside Vault (With 1-Click Upgrade) |
| :--- | :--- | :--- | :--- |
| **Combo 1: Basic Pack Only** | `vt1=none, vt2=none` | 19 Core Videos + 5-Day Curriculum + 250+ Prompt Bible | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249 / +$6`) & 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149 / +$5`) |
| **Combo 2: Basic + Uncensored Hack** | `vt1=valid, vt2=none` | Core + 🔓 Uncensored NSFW Add-On Videos & Guide | 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149 / +$5` — Bump #1 never charged again) |
| **Combo 3: Basic + 500+ Viral Hooks** | `vt1=none, vt2=valid` | Core + 🔓 500+ Viral Reel Hooks & Auto-DM Pack | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249 / +$6` — Bump #2 never charged again) |
| **Combo 4: Full VIP Bundle** | `vt1=valid, vt2=valid` | 🔓 Everything Unlocked (Core + Bump #1 + Bump #2) | None — Full VIP Access Badge displayed |
