# 🎨 Design System & UI/UX Specification (`DESIGN.md`)

Last Updated: **November 9, 2026 (`v2.9.5`)**

## 1. Visual Identity & Aesthetic Direction
- **Brand Name:** PersonaLabs Academy (`personalabs.store`)
- **Design Archetype:** High-Converting Editorial Creator Storefront (Split-Layout Checkout + Interactive SaaS Sandbox & Proof Cards)
- **Primary Palette:**
  - **Brand Orchid / Fuchsia:** `#e65ce4` → `#d946ef` (Primary CTA buttons, active bump borders, right-side signature pastel polka-dot strip)
  - **Urgency Crimson:** `#991b1b` / `#dc2626` with `#fde047` / `bg-yellow-300` timer badge (`90% OFF FLASH SALE`)
  - **Trust Emerald:** `#10b981` / `#059669` (Verified badges, live viewer indicator, savings pills)
  - **Guarantee Dark Card Accent:** `#07090e` card backdrop paired with opaque Amber-Orange linear gradient (`#fbbf24` → `#f97316` → `#ea580c`) and crisp white inner FAQ/Seal cards
  - **Light Mode Surface (Default):** Crisp white `#ffffff` background, `#f8fafc` elevated cards, `#0f172a` primary headings, `#475569` secondary copy (`color-scheme: light` enforced against auto-dark browser overrides)
  - **Dark Mode Surface:** Deep obsidian `#0f1117` background, `#161922` cards, `#f8fafc` headings, `#cbd5e1` body text (`[data-theme="dark"]`)

---

## 2. Typography (`styles.css?v=9`)
- **Display / Headings:** `'Plus Jakarta Sans'`, `700–800` weight, tight tracking (`-0.02em`)
- **Body Copy:** `'Inter'`, `400–600` weight, optimized for mobile readability (inputs `>=14px–16px` safe to prevent iOS Safari zoom)
- **Numeric / Timers / Prices:** `'JetBrains Mono'` (`font-mono-num`) for tabular alignment on countdown timers, live viewer counts, earnings outputs, and prices

---

## 3. Core Storefront UX & Micro-Interactions ([`index.html`](../index.html), [`app.js`](../app.js))
1. **Single-Line Sticky Urgency Header:**
   - Locks `⚡ URGENT`, `90% OFF FLASH SALE` (`75% OFF LAUNCH OFFER` post-expiry), `⏱ 10:00` countdown, optional `/kjboavhpoieabpraegnaln` currency toggle (`Test: ₹1 / $1`), `👁 32 viewing now`, and Light/Dark theme toggle onto a single non-wrapping horizontal bar (`flex-nowrap whitespace-nowrap`).
2. **Mobile Above-the-Fold Price Anchor Card (`lg:hidden`):**
   - Renders immediately beneath [`assets/images/hero_showcase.jpg`](../assets/images/hero_showcase.jpg?v=9) on mobile viewports so Instagram Reels visitors immediately see `₹1,999 → ₹199` (`$79 → $9`), 4 deliverable bullets, `⚡ Unlock Instant Access — ₹199 →`, and UPI/Card trust bar without scrolling.
3. **"Nothing to lose. Everything to gain." Guarantee Banner:**
   - 2-column showcase pairing the SVG **100% Money-Back Guarantee Gold Seal** (7-day risk-free refund) with 3 crisp FAQ cards and a direct checkout jump button (`scrollToCheckout('Guarantee Section CTA')`).
4. **Smooth Pointer Hover Zoom & Visual Order Bumps:**
   - Creator Header Avatar uses [`assets/insta_profile_closeup_hd.jpg`](../assets/insta_profile_closeup_hd.jpg?v=16) + [`favicon.svg`](../favicon.svg) corner mark.
   - Hero Banner ([`assets/images/hero_showcase.jpg`](../assets/images/hero_showcase.jpg?v=9)) scales `1.035x` on hover (`hero-hover-zoom`).
   - Order Bump #1 (*Uncensored Content Hack*) thumbnail uses [`assets/images/uncensored_hack_cover.png`](../assets/images/uncensored_hack_cover.png?v=18) (`1.10x` hover scale).
   - Order Bump #2 (*500+ Viral Reel Hooks & Auto-DM Pack*) thumbnail uses [`assets/images/persona_bali.jpg`](../assets/images/persona_bali.jpg?v=17) (`1.10x` hover scale).
5. **Interactive Sandbox (`#sec-ai-lab`), Revenue Chart (`#sec-analytics`) & Reel Simulator:**
   - `#sec-ai-lab` defaults to `🌴 Bali Travel` first pill (`persona_bali.jpg`) alongside `💎 Monaco Luxury` (`persona_maya.jpg`), `⚡ Seoul Street` (`persona_aira.jpg`), and `🏋️‍♂️ Dubai Fitness` (`persona_alex.jpg`).
   - Double-clicking/tapping the Hero Banner or AI Lab preview spawns an Instagram-style floating heart animation.
6. **Student Portal (`course-vault/`) & Instant PDF Receipt (`receipt.html`):**
   - Portal uses obsidian dark studio aesthetic (`#07080d` / `#151824`) with sidebar navigation across Days 1–5 (`18 Lessons`) and cryptographic VIP lock cards.
   - `receipt.html` opens in `<50ms` via `<link rel="prefetch">`, non-render-blocking Google Fonts (`media="print" onload="this.media='all'"`), and clean `@media print` A4 formatting (`Tax Invoice` for `INR`, `Payment Receipt` for `USD`).
