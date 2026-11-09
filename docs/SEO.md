# 🔍 SEO, Social Graph & Conversion Metadata (`SEO.md`)

Last Updated: **November 9, 2026 (`v2.9.5`)**

## 1. Current On-Page SEO Configuration ([`index.html`](../index.html))
- **Canonical Domain:** `https://personalabs.store/`
- **Title Tag (`index.html` line 7):**  
  `Instant AI Influencer Prompt Vault & 1-Click Character Launch Kit (Only ₹199 Today) | PersonaLabs Academy`
- **Meta Description (`index.html` line 8):**  
  `Instant access to 250+ Character DNA Prompts, 1-Click Face-Lock Files, and the complete AI Influencer Launch Kit by PersonaLabs Academy. Only ₹199 today.`
- **Favicon & Brand Icon:** [`favicon.svg`](../favicon.svg) (`PL` monogram in electric orchid/violet gradient with gold AI spark).
- **Private Vault & Sandbox Crawl Block ([`vercel.json`](../vercel.json)):**
  - `/course-vault/(.*)` and `/kjboavhpoieabpraegnaln` both enforce `X-Robots-Tag: noindex, nofollow, noarchive` and `Cache-Control: private, no-cache, no-store, must-revalidate` so member portals, receipts, VIP pages, and the `₹1 / $1` test route are never indexed by Google.
  - All `course-vault/*.html` files also include `<meta name="robots" content="noindex, nofollow" />`.

---

## 2. Target High-Intent Keywords & Positioning
| Keyword Cluster | Search / Social Intent | Target Landing Section / Funnel Entry |
| :--- | :--- | :--- |
| `how to create an AI influencer for free` | Beginner Tutorial / Tool Discovery | Overview + 5-Day Curriculum (`#sec-curriculum`) + Organic Reels |
| `AI influencer course India ₹199` | Direct Commercial Purchase Intent | Hero Mobile Card & Floating Checkout (`https://personalabs.store`) |
| `consistent face AI model Instagram reels` | Technical Problem Solving | Character DNA Lab (`#sec-ai-lab`) & Comparison (`#sec-comparison`) |
| `FaceFusion NSFW bypass tutorial` | High-Curiosity Add-On Intent | Order Bump #1 (`Uncensored Content Hack`) |
| `viral reel hooks for AI creators` | Growth & Monetization Intent | Order Bump #2 (`500+ Viral Reel Hooks & Auto-DM Pack`) |

---

## 3. Performance & Core Web Vitals Architecture
- **Static Edge Delivery:** Hosted on **Vercel Global Edge CDN** (`216.198.79.1`, `buildCommand: null`, `outputDirectory: "."`) with zero server cold-start latency.
- **Instant Cache Invalidation (`vercel.json`):** `index.html`, `app.js?v=25`, and `styles.css?v=9` serve `Cache-Control: public, max-age=0, must-revalidate`.
- **Lean Runtime Asset Payload (`assets/` — only `8` images):**
  - Storefront imagery (`hero_showcase.jpg`, `ai_workflow_studio.jpg`, `uncensored_hack_cover.png`, `persona_bali.jpg`, `persona_maya.jpg`, `persona_aira.jpg`, `persona_alex.jpg`, `insta_profile_closeup_hd.jpg`) kept clean with duplicate/unused assets purged in `v2.9.5` and heavy video/studio folders excluded via [`.vercelignore`](../.vercelignore).
- **Zero-Blocking Prefetch & Telemetry:**
  - `course-vault/receipt.html` is preloaded via `<link rel="prefetch">` and renders in `<50ms` with non-blocking fonts (`media="print" onload="this.media='all'"`).
  - Google Sheets webhook (`CTA_CLICKED_SCROLL`, `PARTIAL_LEAD_CAPTURED`, `INITIATED_CHECKOUT`, `PAID_SUCCESS`) uses asynchronous non-blocking `fetch(..., { mode: 'no-cors' })` so UI transitions stay instant.
- **Instagram Organic SEO Discoverability (`@personalabsacademy`):**
  - Every one of the 11 scheduled Dancing Reels uses topical alt-free captions, structured bullet keywords, and a dedicated SEO Hashtag + Keyword Question First Comment ([`ORGANIC-MASTER-DANCING-REELS-CALENDAR.md`](../instagram-studio/ORGANIC-MASTER-DANCING-REELS-CALENDAR.md)).
