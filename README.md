# 🚀 PersonaLabs Academy (`personalabs.store`)

> **Official Storefront, Interactive Student Vault, Automated Delivery Engine & 100% Organic Viral Reels Studio (`v2.9.5`)**  
> **Live Website:** [https://personalabs.store](https://personalabs.store) · **Student Vault:** [https://personalabs.store/course-vault/](https://personalabs.store/course-vault/) · **Instagram:** [@personalabsacademy](https://www.instagram.com/personalabsacademy/)

---

## 📁 Clean Project Layout

| Path | Role |
| :--- | :--- |
| **`index.html`**, **`app.js`**, **`styles.css`**, **`favicon.svg`**, **`vercel.json`**, **`.vercelignore`** | Live static storefront (`personalabs.store`) hosted on Vercel Global Edge CDN. `.vercelignore` keeps internal docs, scripts, and studio files off the public web root. |
| [**`assets/`**](assets/) | Runtime storefront images **only** (`insta_profile_closeup_hd.jpg`, `images/hero_showcase.jpg`, `ai_workflow_studio.jpg`, `uncensored_hack_cover.png`, `persona_*.jpg`). |
| [**`course-vault/`**](course-vault/) | Student member portal, printable A4 Tax Invoice/Receipt, Prompt Bible, and VIP add-on pages. |
| [**`instagram-studio/`**](instagram-studio/) | **Unified social studio:** `reels-active-11/` (11 scheduled Master Reels + `thumbnails/`), `carousels/` (`01`–`06`), `source-assets/` (`character-assets/`, `raw-gemini-videos/`, `brand-dps/`, `bgm_master.mp3`), calendars, and `archive/`. |
| [**`scripts/`**](scripts/) | **Unified automation & audit scripts:** `build_all_11_organic_master_reels.py`, `deep_audit_vault.py`, `audit_mobile_crossdevice.py`, plus `archive/` for legacy builders. |
| [**`docs/`**](docs/) | Strategy, architecture, deployment guide, delivery setup, Google Sheets Apps Script docs, and launch playbooks. |

---

## 🎯 Quick Links & Documentation Index

| Document | Description |
| :--- | :--- |
| [**`GEMINI.md`**](GEMINI.md) | **Mandatory Repository Creative Standard:** Strict 100% fluid dance motion Reels hook standard, 100% generic AI model terminology, and organic ManyChat conversion protocol. |
| [**`docs/LAUNCH_OPERATIONS_MANUAL.md`**](docs/LAUNCH_OPERATIONS_MANUAL.md) | **Master Operational Handbook (`v2.9.5`):** 100% organic growth & Reels publishing protocol, 11 Master Dancing Video Reels, automated email recovery/upsells, and ManyChat comment-to-DM triggers. |
| [**`docs/CHANGES.md`**](docs/CHANGES.md) | **Full Release Changelog (`v2.2.0` → `v2.9.5`):** Release notes for the 100% organic pivot, 11 dancing reels portfolio, and repository cleanup. |
| [**`docs/ROADMAP.md`**](docs/ROADMAP.md) | Date-Wise & Task-Wise Master Execution Calendar, completed sales milestones, creative testing logs, and post-Nov 10 scaling roadmap. |
| [**`docs/ARCHITECTURE.md`**](docs/ARCHITECTURE.md) | System & funnel architecture, Geo-IP pricing state machine, FNV-1a (`vt1`/`vt2`) add-on access signatures, and unified directory map. |
| [**`docs/CREATOR-DELIVERY-README.md`**](docs/CREATOR-DELIVERY-README.md) | Internal digital product packaging & Google Drive / web delivery setup reference. |
| [**`docs/META-ADS-CHANGELOG-AND-METRICS.md`**](docs/META-ADS-CHANGELOG-AND-METRICS.md) | **Financial & Historical Ad Ledger (reconciled 30 Oct):** ₹4,986 ad spend vs ₹2,986 revenue from 5 orders (−₹2,000 net, ₹597 AOV, ₹890 ad cash per sale), Meta billing & Razorpay settlement logs, and 24–28 Oct Look C creative test results (**6.45% CTR**, **₹34.83 CPM**, **4,625 plays**, **26 followers**). |
| [**`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`**](docs/GOOGLE-SHEETS-DATABASE-SETUP.md) | Google Sheets 22-column Order & Lead DB (`1Sy8fy...`) + Apps Script (`Version 3`) `DriveApp.addViewer` auto-whitelisting and `GmailApp` 25-min cart recovery / 12-hr upsell triggers. |
| [**`instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`**](instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md) | Master 11-Day Organic Reels Schedule (Nov 9 – Nov 19, 2026), exact cover thumbnails, captions, first-comment SEO keywords, and story link stickers. |
| [**`instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md`**](instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md) | Carousel captions, First-Comment SEO Hashtags, Daily 3-Story Sequences, and ManyChat base DM copy. |

---

## ⚡ Live Production Stack Summary (`v2.9.5`)

- **Hosting & CDN:** Vercel Global Edge CDN (`216.198.79.1`) with instant GitHub `main` auto-deploy (`<15s`).
- **Local Directory Architecture:**
  - Physical Directory: `C:\Projects\ai-influencer-course-website` (contains all Git repository code & assets).
  - Directory Junction: `C:\Projects\personalabs-academy` (Windows alias pointing to the physical directory; 0 MB duplicate storage).
- **Payments:**
  - **🇮🇳 India (`INR`):** Live Razorpay Standard Checkout (`rzp_live_TmX62nNGuBaTUc` — UPI, QR, Cards, Netbanking).
  - **🌎 International (`USD`):** Live PayPal Smart Buttons SDK (`BAARfEN6...` — PayPal + Debit/Credit Cards, `NO_SHIPPING`).
- **Automated Fulfillment & Email Recovery (`personalabsacademy@gmail.com`):**
  - Instant on-screen Student Portal ([`course-vault/index.html`](course-vault/index.html)) + `<50ms` printable A4 PDF Tax Invoice / Payment Receipt ([`course-vault/receipt.html`](course-vault/receipt.html)).
  - Automatic `DriveApp.addViewer` whitelisting across 3 private Google Drive deliverable folders (`01-Core-Course-Videos`, `02-Uncensored-NSFW-Addon-Videos`, `03-500-Viral-Hooks-And-Prompts-Pack`).
  - 24/7 Google Apps Script triggers for **25-Min Abandoned Cart Recovery** and **12-Hr Post-Purchase Add-On Upsells**.
- **100% Organic Acquisition & Reels Engine:**
  - **11 Master Dancing Video Reels ([`instagram-studio/reels-active-11/`](instagram-studio/reels-active-11/)):** 11 broadcast-grade 1080×1920 video reels (`Hottest_Hook_01` to `11`) + custom front-facing covers (`thumbnails/Cover_01` to `11`) scheduled daily `9 Nov – 19 Nov 2026 @ 7:30 PM IST`.
  - **Instagram (`@personalabsacademy`):** Operating on 100% organic growth via ManyChat Comment-to-DM triggers and Story Link Stickers (zero paid ad spend). External bio link unlock scheduled for 10 Nov 2026.
