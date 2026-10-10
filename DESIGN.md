# 🎨 Design System & UI/UX Specification (`DESIGN.md`)

## 1. Visual Identity & Aesthetic Direction
- **Brand Name:** PersonaLabs Academy (`personalabs.store`)
- **Design Archetype:** High-Converting Editorial Creator Storefront (EarlyCaves / SuperProfile Split-Layout + Modern Interactive SaaS Elements)
- **Primary Palette:**
  - **Brand Orchid / Fuchsia:** `#e65ce4` → `#d946ef` (Primary CTA buttons, active bump borders, right-side signature polka-dot strip)
  - **Urgency Crimson:** `#991b1b` / `#dc2626` with `#fde047` (Yellow-300) timer badge
  - **Trust Emerald:** `#10b981` / `#059669` (Verified badges, live viewer indicator, savings pills)
  - **Light Mode Surface (Default):** Crisp white `#ffffff` background, `#f8fafc` elevated cards, `#0f172a` primary headings, `#475569` secondary copy (`color-scheme: light` enforced).
  - **Dark Mode Surface:** Deep obsidian `#0f1117` background, `#161922` cards, `#f8fafc` headings, `#cbd5e1` body text.

---

## 2. Typography
- **Display / Headings:** `'Plus Jakarta Sans'`, `700–800` weight, tight tracking (`-0.02em`).
- **Body Copy:** `'Inter'`, `400–600` weight, optimized for mobile readability.
- **Numeric / Timers / Prices:** `'JetBrains Mono'` (`font-mono-num`) for tabular alignment on countdown timers, live viewer counts, and prices.

---

## 3. Micro-Interactions & Conversion UX
1. **Single-Line Sticky Urgency Header:**
   - Keeps `⚡ URGENT`, `88% OFF FLASH SALE`, `⏱ 10:00` countdown, and `👁 32 viewing now` aligned on a single horizontal line (`flex-nowrap whitespace-nowrap`).
2. **Smooth Pointer Hover Zoom (`hero-hover-zoom`):**
   - Hovering over the 3-panel Hero Banner (`assets/images/hero_showcase.jpg`) smoothly scales the image by `1.035x` over `450ms` (`cubic-bezier(0.22, 1, 0.36, 1)`).
   - Hovering over Order Bump #1 (`uncensored_hack_cover.jpg`) and Order Bump #2 (`persona_aira.jpg`) scales thumbnails by `1.10x`.
3. **Double-Tap Floating Heart:**
   - Double-clicking/tapping the Hero Image spawns an Instagram-style floating heart animation.
