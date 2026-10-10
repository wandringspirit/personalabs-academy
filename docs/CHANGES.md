# 📋 PersonaLabs Academy — Changelog (`CHANGES.md`)

## v2.5.0 — 2026-10-11 (Latest Release)
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
