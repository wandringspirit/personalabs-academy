# 🏗️ PersonaLabs Academy — System & Funnel Architecture (`personalabs.store`)

## 1. High-Level Architecture Overview

```
Visitor (Instagram Reel / Bio Link / ManyChat DM / Ad)
   │
   ▼
https://personalabs.store/ (Netlify Global Edge CDN)
   ├── Geo-IP Detection & Currency Lock
   │     ├── 🇮🇳 India IPs ──► Locked to INR (₹249 Flash / ₹499 Post-Timer)
   │     └── 🌎 Global IPs ──► Locked to USD ($9 Flash / $19 Post-Timer)
   │
   ├── 10-Minute Persistent Flash Sale Engine (localStorage)
   │     └── Automatically steps price from ₹249 → ₹499 ($9 → $19) at 00:00
   │
   ├── Dual Order Bump & 4-Combination Upgrade Engine
   │     ├── Base Course Only (b1=0, b2=0)
   │     ├── Base + Bump #1: Uncensored Content Hack (+₹249 / +$9 -> b1=1, b2=0)
   │     ├── Base + Bump #2: 500+ Viral Reel Hooks & Auto-DM Pack (+₹149 / +$5 -> b1=0, b2=1)
   │     └── All-Access VIP Bundle (Base + Bump #1 + Bump #2 -> b1=1, b2=1)
   │
   ├── Real-Time Google Sheets Order & Lead Database (Apps Script Webhook)
   │     ├── Event 1: INITIATED_CHECKOUT (Yellow Row — captures abandoned cart leads)
   │     └── Event 2: PAID_SUCCESS (Green Row — records verified Transaction ID & Bumps)
   │
   └── Post-Purchase Delivery (Dual-Channel)
         ├── 1. Interactive Member Vault: https://personalabs.store/course-vault/?b1=X&b2=Y
         └── 2. Google Drive 3-Folder Architecture (Dedicated Brand Gmail Account)
               ├── Folder 01: 01-Core-Course-Videos (19 Core English-Captioned HD Videos)
               ├── Folder 02: 02-Uncensored-NSFW-Addon-Videos (4 Exclusive NSFW Add-On Videos — Bump #1)
               └── Folder 03: 03-500-Viral-Hooks-And-Prompts-Pack (500+ Hooks + 250+ Prompts — Bump #2)
```

---

## 2. File & Directory Structure

| File / Folder | Purpose |
| :--- | :--- |
| `index.html` | High-converting single-page storefront with 10-min flash timer, inline live viewer counter, dual order bumps, UPI QR / Razorpay / PayPal / Stripe checkout, and Post-Purchase Upgrade Mode (`?upgrade=bump1` / `?upgrade=bump2`). |
| `styles.css` | Custom design system tokens, light/dark mode contrast enforcement, smooth pointer hover zoom (`hero-hover-zoom`), and mobile-first responsive utilities. |
| `app.js` | Pricing state machine, Geo-IP currency detection, promo code engine, 4-combination add-on upgrade checkout logic, and Google Sheets webhook dispatcher. |
| `favicon.svg` | Official `PersonaLabs Academy` (`PL` + Gold AI Spark) vector brand mark. |
| `course-vault/index.html` | Interactive Student Member Portal with 5-Day curriculum, progress tracking, add-on access control (`b1` & `b2` locks), and 1-click post-purchase upgrade cards. |
| `course-vault/uncensored-content-hack.html` | Order Bump #1 VIP Guide: Uncensored Content Hack, safe multi-platform funneling, and realism prompt modifiers. |
| `course-vault/viral-hooks-and-autodm-pack.html` | Order Bump #2 VIP Guide: 500+ Viral Reel Hooks & ManyChat Comment-to-DM Automation Scripts. |
| `course-vault/character-dna-prompt-bible.html` | Core Bonus: 250+ AI Character DNA & Face-Lock Master Prompts. |
| `GOOGLE-SHEETS-DATABASE-SETUP.md` | Live Google Apps Script webhook documentation & 19-column schema reference. |

---

## 3. 4-Combination Add-On Access & Post-Purchase Upgrade State Machine

| Buyer State | URL / `localStorage` Flags | Unlocked in Vault & Google Drive | Locked Inside Vault (With 1-Click Upgrade) |
| :--- | :--- | :--- | :--- |
| **Combo 1: Basic Pack Only** | `b1=0, b2=0` | 19 Core Videos + 5-Day Curriculum + 250+ Prompt Bible | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249`) & 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149`) |
| **Combo 2: Basic + Uncensored Hack** | `b1=1, b2=0` | Core + 🔓 Uncensored NSFW Add-On Videos & Guide | 🔒 Bump #2 (`/?upgrade=bump2`, `+₹149` — Bump #1 never charged again) |
| **Combo 3: Basic + 500+ Viral Hooks** | `b1=0, b2=1` | Core + 🔓 500+ Viral Reel Hooks & Auto-DM Pack | 🔒 Bump #1 (`/?upgrade=bump1`, `+₹249` — Bump #2 never charged again) |
| **Combo 4: Full VIP Bundle** | `b1=1, b2=1` | 🔓 Everything Unlocked (Core + Bump #1 + Bump #2) | None — Full VIP Access Badge displayed |
