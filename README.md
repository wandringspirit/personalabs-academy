# 🚀 PersonaLabs Academy (`personalabs.store`)

> **Official Storefront, Interactive Student Vault, Automated Delivery Engine, Meta Ads Engine & 3-Agent Autonomous Instagram Studio (`v2.9.3`)**  
> **Live Website:** [https://personalabs.store](https://personalabs.store) · **Student Vault:** [https://personalabs.store/course-vault/](https://personalabs.store/course-vault/) · **Instagram:** [@personalabsacademy](https://www.instagram.com/personalabsacademy/)

---

## 🎯 Quick Links & Documentation Index

| Document | Description |
| :--- | :--- |
| [**`docs/META-ADS-CHANGELOG-AND-METRICS.md`**](docs/META-ADS-CHANGELOG-AND-METRICS.md) | **Live Financial & Ad Telemetry Ledger:** ₹2,389 confirmed revenue (4 orders, 100% order bump take rate, ₹597.25 AOV), customer registry, unit economics, and 24–28 Oct Look C creative test results (**6.45% CTR**, **₹34.83 CPM**, **4,625 plays**, **26 followers**). |
| [**`docs/LAUNCH_OPERATIONS_MANUAL.md`**](docs/LAUNCH_OPERATIONS_MANUAL.md) | **Master Operational Handbook (`v2.9.3`):** Live Meta Ads Campaign architecture, 5 master re-sequenced dancing video hooks, automated email recovery/upsells, `/kjboavhpoieabpraegnaln` (`₹1 / $1`) test route, and ManyChat comment-to-DM strategy. |
| [**`docs/ROADMAP.md`**](docs/ROADMAP.md) | Date-Wise & Task-Wise Master Execution Calendar, completed sales milestones, creative testing logs, and post-Nov 10 scaling roadmap. |
| [**`docs/ARCHITECTURE.md`**](docs/ARCHITECTURE.md) | System & funnel architecture, Geo-IP pricing state machine, FNV-1a (`vt1`/`vt2`) add-on access signatures, and directory map. |
| [**`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`**](docs/GOOGLE-SHEETS-DATABASE-SETUP.md) | Google Sheets 22-column Order & Lead DB (`1Sy8fy...`) + Apps Script (`Version 3`) `DriveApp.addViewer` auto-whitelisting and `GmailApp` 25-min cart recovery / 12-hr upsell triggers. |
| [**`docs/CHANGES.md`**](docs/CHANGES.md) | Full release changelog (`v2.2.0` → `v2.9.3`). |
| [**`instagram-studio/CONTENT-CALENDAR.md`**](instagram-studio/CONTENT-CALENDAR.md) | Live & Scheduled Meta Business Suite queue + Sunday `10:00 AM IST` recurring refill schedule. |
| [**`instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md`**](instagram-studio/CONTENT-CALENDAR-AND-CAPTIONS.md) | Complete Captions, First-Comment SEO Hashtags, Daily 3-Story Sequences, and ManyChat Keyword Triggers (`AI`, `LAUNCH`, `MODEL`, `REEL`, `HACK`, `LINK`, `PROMPT`). |

---

## ⚡ Live Production Stack Summary (`v2.9.3`)

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
- **Paid Acquisition & Creative Engine:**
  - **Meta Ad Account:** `PersonaLabs Academy Ads` (`2218391099056783`), Pixel `1661173205598260`.
  - **Re-Sequenced Master Hook Ads ([`ads-ready/dancing-ad-hooks/`](ads-ready/dancing-ad-hooks/)):** 5 master 1080×1920 video ads (`Hottest_Hook_01` to `05`) engineered to open at `0:00` with the model's direct eye-contact radiant smile, proven by the 24–28 Oct test to deliver **6.45% CTR** and **₹34.83 CPM**.
  - **Instagram (`@personalabsacademy`):** 19 posts, 26 real followers, active boosted Reels with over 4,600 plays. Bio external link unlock scheduled after 10 Nov; direct sales currently run via Meta Ads Manager website CTA buttons.
