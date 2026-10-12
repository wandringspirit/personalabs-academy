# 🚀 Deployment & Operations Guide (`DEPLOY.md`)

## 1. Live Production Architecture (`v2.9.0`)
- **Live Domain:** `https://personalabs.store` & `https://www.personalabs.store`
- **Secret Live Payment Test Route (`₹1 INR / $1 USD`):** `https://www.personalabs.store/kjboavhpoieabpraegnaln`
- **GitHub Repository:** `https://github.com/wandringspirit/personalabs-academy` (Branch: `main`, **Private** repository so `/course-vault/` VIP filenames and `/docs/` stay hidden from public search)
- **Git Author Identity (Required for Vercel Hobby Auto-Deploy):**
  `wandringspirit <209062033+wandringspirit@users.noreply.github.com>`
  *(Uses GitHub's privacy-protected noreply email so no personal Gmail is ever exposed in commits AND Vercel Hobby recognizes every push from `wandringspirit` automatically!)*
- **Active CDN Host:** **Vercel Global Edge CDN** (`A @` → `216.198.79.1`, `CNAME www` → `847062401d7e0c68.vercel-dns-017.com`, 100 free production deploys/day)
- **Host Config:** [`vercel.json`](../vercel.json) (Zero-build static deployment, `/kjboavhpoieabpraegnaln` rewrite, instant cache invalidation on `index.html`/`app.js`/`styles.css`, and `X-Robots-Tag: noindex, nofollow` on `/course-vault/*`)

---

## 2. Connected Production IDs & Endpoints
- **Razorpay Live Key ID (`INR`):** `rzp_live_TmX62nNGuBaTUc`
- **PayPal Live Client ID (`USD`):** `BAARfEN6AEZqn7tB4CWb08mUBhJqBYzxwPkmMnxJNkQ77mGxuYUiisrNiiYhtg75Gg12nHMXKAS38v_p1E`
- **Meta Business Portfolio ID:** `1761523878300294` (`PersonaLabs Academy`)
- **Meta Ad Account ID (`INR`, `Asia/Kolkata`):** `2218391099056783` (`PersonaLabs Academy Ads`)
- **Meta Pixel / Dataset ID:** `1661173205598260` (`PersonaLabs Academy Pixel`)
- **Google Sheets Orders DB (`personalabsacademy@gmail.com`):** `1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc` (22 Columns)
- **Google Apps Script Webhook URL (`Version 3`):** `https://script.google.com/macros/s/AKfycbzxKGXLOy1g2TebrWch0aGHdvTp7iYffCULRApdjlEerdum6p2Sj4mAWa5awzM_JrOm/exec`
- **3 Restricted Google Drive Folders (`personalabsacademy@gmail.com`):**
  1. `01-Core-Course-Videos`: `1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`
  2. `02-Uncensored-NSFW-Addon-Videos`: `10HGXWcRMR898lbQnTX41G--fPLKoBOvW`
  3. `03-500-Viral-Hooks-And-Prompts-Pack`: `1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`

---

## 3. How to Push Website Updates Live (Auto-Deploys in ~8 Seconds)
Run the following commands from the project root:
```powershell
git status
git add index.html styles.css app.js vercel.json course-vault/ assets/ docs/
git commit -m "Update storefront and documentation"
git push origin main
```
> **Note:**
> 1. Always keep `git config user.email` set to `209062033+wandringspirit@users.noreply.github.com` so Vercel Hobby automatically builds and deploys every push within ~8 seconds.
> 2. When updating `app.js` or `styles.css`, increment the `?v=XX` query string in [`index.html`](../index.html) (`app.js?v=21`).
> 3. Large video files (`videos/`, `videos-captioned/`, `ads-ready/`, `*.mp4`, `*.srt`, `*.zip`) are excluded in `.gitignore` so GitHub pushes and static CDN deploys stay instantaneous.
