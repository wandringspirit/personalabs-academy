# 🔍 SEO, Social Graph & Conversion Metadata (`SEO.md`)

## 1. Current On-Page SEO Configuration (`index.html`)
- **Canonical Domain:** `https://personalabs.store/`
- **Title Tag:** `AI Influencer Accelerator – Start Your AI Creator Business | PersonaLabs Academy`
- **Meta Description:** `Get instant access to the AI Influencer Launch Kit by PersonaLabs Academy — a complete step-by-step system that shows you how to create, grow, and monetize AI influencers in 5 days using modern AI tools.`
- **Favicon & Brand Icon:** `favicon.svg` (`PL` monogram in electric orchid/violet gradient with gold AI spark).

---

## 2. Target High-Intent Keywords
| Keyword Cluster | Search / Social Intent | Target Landing Section |
| :--- | :--- | :--- |
| `how to create an AI influencer for free` | Beginner Tutorial / Tool Discovery | Overview + 5-Day Curriculum (`#sec-curriculum`) |
| `AI influencer course India ₹249` | Direct Commercial Purchase Intent | Hero Checkout Card (`https://personalabs.store`) |
| `consistent face AI model Instagram reels` | Technical Problem Solving | Character DNA & FaceSwap Modules |
| `FaceFusion NSFW bypass tutorial` | High-Curiosity Add-On Intent | Order Bump #1 (`Uncensored Content Hack`) |
| `viral reel hooks for AI creators` | Growth & Monetization Intent | Order Bump #2 (`500+ Viral Reel Hooks & Auto-DM Pack`) |

---

## 3. Performance & Core Web Vitals Checklist
- **Static Edge Delivery:** Hosted on Netlify Global CDN with zero server cold-start latency.
- **Image Optimization:** Hero showcase (`hero_showcase.jpg`), order bump thumbnails (`uncensored_hack_cover.jpg`, `persona_aira.jpg`), and creator avatar (`creator_avatar.jpg`) served as compressed JPEGs with hardware-accelerated CSS transforms (`will-change: transform`).
- **Zero-Blocking Checkout:** Google Sheets webhook uses non-blocking `fetch(..., { mode: 'no-cors', keepalive: true })` so checkout transitions happen in `<50ms`.
