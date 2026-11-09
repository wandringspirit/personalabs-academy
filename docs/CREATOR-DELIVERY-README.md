# 📦 PersonaLabs Academy — Digital Product Packaging & Customer Delivery Guide

Last Updated: **November 9, 2026 (`v2.9.5`)**

Everything inside [`course-vault/`](../course-vault/) and your 3 Restricted Google Drive folders (`videos-captioned/` local mirror) forms your **complete digital product delivery architecture** for `https://personalabs.store`. When a customer pays via **Razorpay (`INR`)** or **PayPal (`USD`)**, delivery happens instantaneously on-screen + via automated Google Drive viewer whitelisting.

---

## 🗂️ 1. Complete Product & Deliverable Inventory

### A. Hosted Student Portal Files ([`course-vault/`](../course-vault/))
| File Name | Product Role | Live Pricing (`INR` / `USD`) | Access Gate & What's Inside |
| :--- | :--- | :--- | :--- |
| [**`course-vault/index.html`**](../course-vault/index.html) | **Core Flagship Course Portal** (*AI Influencer Accelerator — 5-Day Launch Kit*) | **₹199 / `$9`** *(10-Min Flash)*<br>**₹499 / `$19`** *(Post-Timer)* | Interactive **5-Day / 18-Lesson** Student Member Dashboard (`localStorage` progress tracking, copy-paste prompt cards, tool workflow guides, and links to Google Drive folders + 1-click add-on upgrades). |
| [**`course-vault/character-dna-prompt-bible.html`**](../course-vault/character-dna-prompt-bible.html) | **Included Core Bonus Vault** (*250+ AI Character DNA & Face-Lock Prompt Bible*) | **Included Free** with Core | Interactive Character DNA Combiner + copy-paste master prompts for fashion, resort travel, streetwear, fitness, and universal negative prompts & seed locks. |
| [**`course-vault/uncensored-vip-8f92a1c4.html`**](../course-vault/uncensored-vip-8f92a1c4.html) | **Order Bump #1 (VIP Secret URL)** (*Uncensored Content Hack*) | **`+₹249` / `+$9`** *(Flash)*<br>`+₹399` / `+$14` *(Post-Timer)* | Protected by FNV-1a cryptographic signature (`vt1`) + Apps Script lookup. Covers Filter-Bypass Vocabulary Matrix, Safe High-Curiosity IG Hooks, Uncensored SDXL/Flux workflow, Shield Bridge Funnel, and EXIF/C2PA scrubbing + links to the 4 NSFW videos. |
| [**`course-vault/hooks-vip-3d7e91b2.html`**](../course-vault/hooks-vip-3d7e91b2.html) | **Order Bump #2 (VIP Secret URL)** (*500+ Viral Reel Hooks & Auto-DM Pack*) | **`+₹149` / `+$5`** *(Flash)*<br>`+₹249` / `+$9` *(Post-Timer)* | Protected by FNV-1a cryptographic signature (`vt2`) + Apps Script lookup. Searchable/filterable vault of 500+ 3-second text hooks, Daily Reel Combo Generator, Viral Caption Frameworks, and Done-For-You Comment-to-DM Scripts. |
| [**`course-vault/receipt.html`**](../course-vault/receipt.html) | **Instant Printable Tax Invoice / Receipt** | **Included** (`<50ms` load) | Preloaded via `<link rel="prefetch">`. Displays Udyam MSME (`UDYAM-UP-43-0208040`), itemized add-ons, verified Txn ID, **`Tax Invoice`** (`INR`) or **`Payment Receipt`** (`USD` — zero GST), and direct vault/Drive links. |
| `uncensored-content-hack.html` & `viral-hooks-and-autodm-pack.html` | **Backward-Compatible Redirect Shims** | — | Forward legacy URLs to `uncensored-vip-8f92a1c4.html` and `hooks-vip-3d7e91b2.html` while preserving `?email=...&tx=...&vt1=...&vt2=...` query parameters. |

> **Security & SEO Note:** [`vercel.json`](../vercel.json) attaches `X-Robots-Tag: noindex, nofollow, noarchive` and `Cache-Control: private, no-cache, no-store, must-revalidate` to all `/course-vault/(.*)` routes, and plain-text filenames are hidden from `index.html` source.

---

### B. Private Google Drive Folders (Local Mirror in Git-Ignored `videos-captioned/` — 29 Files)
All 3 folders live under **`personalabsacademy@gmail.com`** and remain **Restricted (Private)** — never set to "Anyone with the link"!
1. **Folder 01 (`01-Core-Course-Videos` — ID `1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`):**
   - **19 Watermark-Free HD `.mp4` Course Videos** (`1.Intro` through `22.The Endgame`, `P2`–`P4` converters, `demo.mp4` — Style 1 English captions burned in) + `Bonus.docx` + `readme.docx` + `250-AI-Character-DNA-Prompt-Bible.html` (`22` files total).
2. **Folder 02 (`02-Uncensored-NSFW-Addon-Videos` — ID `10HGXWcRMR898lbQnTX41G--fPLKoBOvW`):** *(Bump #1 only)*
   - **4 Exclusive Uncensored NSFW Videos** (`14`–`17` FaceFusion series) + `Uncensored-Content-Hack-VIP-Guide.html` (`5` files total).
3. **Folder 03 (`03-500-Viral-Hooks-And-Prompts-Pack` — ID `1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`):** *(Bump #2 only)*
   - `250-AI-Character-DNA-Prompt-Bible.html` + `500-Viral-Reel-Hooks-And-AutoDM-Pack.html` (`2` files total).

---

## 🚀 2. Automated Live Delivery Pipeline (Zero Manual Work)

1. **Instant On-Screen Unlock (`app.js?v=25`):**
   - Immediately upon Razorpay (`pay_...`) or PayPal (`order.capture()`) confirmation, `simulatePaymentComplete()` computes deterministic `vt1`/`vt2` signatures, stores unlocked state in `localStorage`, and reveals personalized links inside the checkout modal + **View & Download Official Tax Invoice / Receipt (PDF)** (`course-vault/receipt.html`).
2. **Returning Sign-In Lookup (`Already made a payment?`):**
   - Buyers can retrieve lost links anytime by entering their email; `openSignInModal()` queries the Google Apps Script `?action=lookupOrder` endpoint against the clean `Orders` tab (`PAID_SUCCESS` rows) and restores their exact add-on permissions (`vt1`/`vt2`).
3. **Automatic Private Google Drive Whitelisting (`Apps Script Version 3`):**
   - `doPost` receives `grantCoreDrive`, `grantNsfwDrive`, and `grantHooksDrive` flags and executes `DriveApp.getFolderById(...).addViewer(buyerEmail)` strictly for purchased folders, logging results (`01-Core, 02-NSFW, 03-Hooks`) in Column 20 (`Google Drive Access Granted`).
4. **Automated 12-Hour Post-Purchase Add-On Upsells:**
   - Every 2 hours, `sendPostPurchaseAddonUpsellEmails` scans paid students (`>12h` post-purchase) who skipped Bump #1 or Bump #2 and sends 1-click upgrade links (`https://personalabs.store/?upgrade=bump1` / `/?upgrade=bump2`) where Base Kit price is automatically `₹0` / `$0`.

---

## 📩 3. Manual Backup Delivery Email / Support Template

If a customer requests manual access resend from **`personalabsacademy@gmail.com`**:

```text
Subject: 🎉 Access Unlocked: Your PersonaLabs AI Influencer Launch Kit

Hey [Name]! 👋

Your enrollment with PersonaLabs Academy is confirmed and your Google Drive email access has been enabled for your Gmail!

👉 ENTER YOUR INTERACTIVE COURSE VAULT:
https://personalabs.store/course-vault/

👉 DIRECT GOOGLE DRIVE CORE VIDEOS (19 HD Lessons):
https://drive.google.com/drive/folders/1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm?usp=sharing

Inside your Vault:
✅ 5-Day / 18-Lesson Guided Portal + Progress Tracker
✅ 250+ Character DNA & Face-Lock Prompt Bible
✅ [If Bump #1 Purchased] Uncensored Content Hack + 4 Exclusive NSFW Videos
✅ [If Bump #2 Purchased] 500+ Viral Reel Hooks & Auto-DM Pack

Tip: Bookmark your portal link or tap "Already made a payment on this page?" anytime on https://personalabs.store to recover your access links with your email.

Reply here anytime if you need assistance!
Team PersonaLabs Academy
personalabsacademy@gmail.com | https://personalabs.store
```
