# 📋 PersonaLabs Academy — Changelog (`CHANGES.md`)

## v2.4.0 — 2026-10-11 (Latest Release)
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
