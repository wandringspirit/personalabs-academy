# 🚀 PersonaLabs Academy (`personalabs.store`)

> **Official Storefront, Interactive Student Vault, Automated Delivery Engine & 100% Organic Viral Reels Studio (`v2.9.5`)**  
> **Live Website:** [https://personalabs.store](https://personalabs.store) · **Student Vault:** [https://personalabs.store/course-vault/](https://personalabs.store/course-vault/) · **Instagram:** [@personalabsacademy](https://www.instagram.com/personalabsacademy/)

---

## 📁 Clean Project Layout

| Path | Role |
| :--- | :--- |
| **`index.html`**, **`app.js`**, **`styles.css`**, **`favicon.svg`**, **`vercel.json`**, **`.vercelignore`** | Live static storefront (`personalabs.store`, `app.js?v=25`, `styles.css?v=9`) hosted on Vercel Global Edge CDN. `.vercelignore` keeps internal docs, scripts, and studio files excluded on CLI deploys, and `vercel.json` protects `/course-vault/*` and `/kjboavhpoieabpraegnaln` with `noindex`. |
| [**`assets/`**](assets/) | Runtime storefront images **only** (`insta_profile_closeup_hd.jpg`, `images/hero_showcase.jpg`, `images/ai_workflow_studio.jpg`, `images/uncensored_hack_cover.png`, `images/persona_bali.jpg`, `images/persona_maya.jpg`, `images/persona_aira.jpg`, `images/persona_alex.jpg`). |
| [**`course-vault/`**](course-vault/) | Student member portal (`index.html`), printable `<50ms` A4 Tax Invoice/Receipt (`receipt.html`), Prompt Bible (`character-dna-prompt-bible.html`), cryptographic VIP add-on pages (`uncensored-vip-8f92a1c4.html`, `hooks-vip-3d7e91b2.html`), plus legacy redirect shims. |
| [**`instagram-studio/`**](instagram-studio/) | **Unified social studio:** `reels-active-11/` (11 scheduled Master Dancing Reels + `thumbnails/`), `carousels/` (`01`–`06`), `source-assets/` (`character-assets/`, `raw-gemini-videos/`, `brand-dps/`, `bgm_master.mp3`), calendars, and `archive/`. |
| [**`scripts/`**](scripts/) | **Unified automation & audit scripts:** `build_all_11_organic_master_reels.py`, `deep_audit_vault.py`, `audit_mobile_crossdevice.py`, plus `archive/` for legacy builders. |
| [**`docs/`**](docs/) | Strategy, architecture, deployment guide, delivery setup, Google Sheets Apps Script docs, financial ledger, outreach templates, and launch playbooks. |

---

## 🎯 Quick Links & Documentation Index

| Document | Description |
| :--- | :--- |
| [**`GEMINI.md`**](GEMINI.md) | **Mandatory Repository Creative Standard:** Strict 100% fluid dance motion Reels hook mandate, 100% generic AI model terminology, organic Comment-to-DM protocol, and canonical paths. |
| [**`docs/LAUNCH_OPERATIONS_MANUAL.md`**](docs/LAUNCH_OPERATIONS_MANUAL.md) | **Master Operational Handbook (`v2.9.5`):** 100% organic growth & Reels publishing protocol, 11 scheduled Dancing Video Reels (`9–19 Nov`), manual DM & Story Link Sticker workflow, automated email recovery/upsells, and live `/kjboavhpoieabpraegnaln` testing route. |
| [**`docs/CHANGES.md`**](docs/CHANGES.md) | **Full Release Changelog (`v2.2.0` → `v2.9.5`):** Complete engineering, creative, financial, and repository consolidation history. |
| [**`docs/ROADMAP.md`**](docs/ROADMAP.md) | Date-Wise & Task-Wise Master Execution Calendar (updated through `9 Nov 2026`), completed milestones, and Nov 10+ bio-link unlock & organic scaling roadmap. |
| [**`docs/ARCHITECTURE.md`**](docs/ARCHITECTURE.md) | System & funnel architecture, Geo-IP `INR`/`USD` pricing state machine (`₹199` / `$9` Flash), FNV-1a (`vt1`/`vt2`) access signatures, and directory map. |
| [**`docs/CREATOR-DELIVERY-README.md`**](docs/CREATOR-DELIVERY-README.md) | Digital product packaging, private `DriveApp.addViewer` delivery setup, VIP HTML vault architecture, and customer delivery templates (`v2.9.5`). |
| [**`docs/META-ADS-CHANGELOG-AND-METRICS.md`**](docs/META-ADS-CHANGELOG-AND-METRICS.md) | **Financial & Historical Ad Ledger (reconciled 30 Oct + Nov 8 Organic Pivot note):** ₹4,986 ad cash paid to Meta vs ₹2,986 settled from 5 orders (−₹2,000 net, ₹597.20 AOV, ₹890 ad cash/sale), Meta billing & Razorpay settlement logs, and Oct 24–28 Look C creative test results (**6.45% CTR**, **₹34.83 CPM**, **4,625 plays**, **26 followers**). |
| [**`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`**](docs/GOOGLE-SHEETS-DATABASE-SETUP.md) | Google Sheets 22-column Order & Lead DB (`1Sy8fy...`, `Logs` + `Orders` tabs) + Apps Script (`Version 3`) `DriveApp.addViewer` auto-whitelisting and `GmailApp` 25-min cart recovery / 12-hr upsell triggers. |
| [**`docs/COMPETITORS.md`**](docs/COMPETITORS.md) | Market & 107-ad Meta Ad Library competitor analysis with pricing, AOV, and conversion moat comparison. |
| [**`docs/DESIGN.md`**](docs/DESIGN.md) | Storefront visual identity, color tokens, typography, mobile price anchor UX, and micro-interaction specification. |
| [**`docs/OUTREACH.md`**](docs/OUTREACH.md) | Manual Instagram Comment-to-DM Saved Replies (for all 11 Reel keywords), Phase-2 ManyChat automation spec, and WhatsApp/Email recovery scripts (`RIYA10` / `VIP20`). |
| [**`docs/RESEARCH.md`**](docs/RESEARCH.md) | Target buyer psychology, `INR`/`USD` pricing economics, and 23-video free/cloud AI tool stack validation. |
| [**`docs/SEO.md`**](docs/SEO.md) | On-page SEO tags (`index.html`), target keyword clusters, Vercel Edge CDN performance, and `noindex` Vault configuration. |
| [**`instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`**](instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md) | **Active Master 11-Day Schedule (`9–19 Nov 2026`):** Verified MBS scheduled timestamps, cover thumbnails, captions, first-comment SEO keywords, Story link stickers, and manual DM replies. |
| [**`instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md`**](instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md) | Reusable Carousels (`01`–`06`), Daily 3-Story Conversion Sequences, and ManyChat Phase-2 Automation Templates. |

---

## ⚡ Live Production Stack Summary (`v2.9.5`)

- **Hosting & CDN:** Vercel Global Edge CDN (`216.198.79.1`) with instant GitHub `main` auto-deploy (`~8–15s`).
- **Local Directory Architecture:**
  - Physical Directory: `C:\Projects\ai-influencer-course-website` (Git repo + Git-ignored local `videos-captioned/` course mirror of 29 files).
  - Directory Junction: `C:\Projects\personalabs-academy` (Windows alias pointing to the physical directory; `0 MB` duplicate storage).
- **Pricing & Checkout (`app.js?v=25`):**
  - **🇮🇳 India (`INR`):** **₹199** (`90% OFF` 10-min Flash Sale vs `₹1,999`) → **₹499** (`75% OFF` Launch Offer) + Bump #1 `+₹249` + Bump #2 `+₹149` (VIP Bundle `₹597`) via **Live Razorpay** (`rzp_live_TmX62nNGuBaTUc`).
  - **🌎 International (`USD`):** **$9** (`90% OFF` 10-min Flash Sale vs `$79`) → **$19** (`75% OFF` Launch Offer) + Bump #1 `+$9` + Bump #2 `+$5` (VIP Bundle `$23`) via **Live PayPal Smart Buttons SDK** (`BAARfEN6...`, `NO_SHIPPING`).
- **Automated Fulfillment & Email Recovery (`personalabsacademy@gmail.com`):**
  - Instant on-screen Student Portal ([`course-vault/index.html`](course-vault/index.html)) + `<50ms` printable A4 PDF Tax Invoice / Payment Receipt ([`course-vault/receipt.html`](course-vault/receipt.html)).
  - Automatic `DriveApp.addViewer` whitelisting across 3 private Google Drive deliverable folders (`01-Core-Course-Videos`, `02-Uncensored-NSFW-Addon-Videos`, `03-500-Viral-Hooks-And-Prompts-Pack`).
  - 24/7 Google Apps Script triggers for **25-Min Abandoned Cart Recovery** and **12-Hr Post-Purchase Add-On Upsells**.
- **100% Organic Acquisition & Reels Engine (`@personalabsacademy`):**
  - **11 Master Dancing Video Reels ([`instagram-studio/reels-active-11/`](instagram-studio/reels-active-11/)):** All **11 Reels** (`Hottest_Hook_01` to `11`) + custom front-facing covers (`thumbnails/Cover_01` to `11`) **Scheduled Live in Meta Business Suite** (`9 Nov – 19 Nov 2026 @ 19:30–19:43 IST`).
  - **DM & Link Strategy:** Manual Comment-to-DM replies during initial low-volume phase (`PROMPT`, `MODEL`, `GLITCH`, `TRAVEL`, `DANCE`, `TWIRL`, `CREATOR`, `VACATION`, `SKIN`, `LAUNCH`, `VIP`) + daily Instagram Story Link Stickers. Profile external bio link cooldown lifts **Tue, 10 Nov 2026**.
