# 🚀 Deployment & Operations Guide (`DEPLOY.md`)

## 1. Live Production Architecture (`v2.9.5`)
- **Live Domain:** `https://personalabs.store` & `https://www.personalabs.store`
- **Secret Live Payment Test Route (`₹1 INR / $1 USD`):** `https://www.personalabs.store/kjboavhpoieabpraegnaln` *(Currently `testSandboxPage.enabled: true` in [`app.js`](../app.js) line 1908 — set to `false` when testing is finished so visits automatically redirect to `/`)*
- **GitHub Repository:** `https://github.com/wandringspirit/personalabs-academy` (Branch: `main`, **Private** repository so `/course-vault/` VIP filenames and `/docs/` stay protected)
- **Git Author Identity (Required for Vercel Hobby Auto-Deploy):**
  `wandringspirit <209062033+wandringspirit@users.noreply.github.com>`
  *(Uses GitHub's privacy-protected noreply email so no personal Gmail is ever exposed in commits AND Vercel Hobby recognizes every push from `wandringspirit` automatically.)*
- **Active CDN Host:** **Vercel Global Edge CDN** (`A @` → `216.198.79.1`, `CNAME www` → `847062401d7e0c68.vercel-dns-017.com`, 100 free production deploys/day)
- **Host Config:** [`vercel.json`](../vercel.json) (Zero-build static deployment, `/kjboavhpoieabpraegnaln` rewrite, `max-age=0, must-revalidate` cache policy on `index.html`/`app.js`/`styles.css`, and `X-Robots-Tag: noindex, nofollow, noarchive` on `/course-vault/*` and `/kjboavhpoieabpraegnaln`) + [`.vercelignore`](../.vercelignore).

---

## 2. Connected Production IDs & Endpoints
- **Razorpay Live Key ID (`INR`):** `rzp_live_TmX62nNGuBaTUc`
- **PayPal Live Client ID (`USD`):** `BAARfEN6AEZqn7tB4CWb08mUBhJqBYzxwPkmMnxJNkQ77mGxuYUiisrNiiYhtg75Gg12nHMXKAS38v_p1E`
- **Meta Business Portfolio ID:** `1761523878300294` (`PersonaLabs Academy`)
- **Instagram Creator Asset ID (`@personalabsacademy`):** `1338150602718052`
- **Meta Ad Account ID (`INR`, `Asia/Kolkata`):** `2218391099056783` (`PersonaLabs Academy Ads` — *currently halted / zero prepaid balance since Nov 8 organic pivot*)
- **Meta Pixel / Dataset ID:** `1661173205598260` (`PersonaLabs Academy Pixel`)
- **Google Sheets Orders DB (`personalabsacademy@gmail.com`):** `1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc` (22 Columns, `Logs` + `Orders` tabs)
- **Google Apps Script Webhook URL (`Version 3`):** `https://script.google.com/macros/s/AKfycbzxKGXLOy1g2TebrWch0aGHdvTp7iYffCULRApdjlEerdum6p2Sj4mAWa5awzM_JrOm/exec`
- **3 Restricted Google Drive Folders (`personalabsacademy@gmail.com`):**
  1. `01-Core-Course-Videos`: `1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm`
  2. `02-Uncensored-NSFW-Addon-Videos`: `10HGXWcRMR898lbQnTX41G--fPLKoBOvW`
  3. `03-500-Viral-Hooks-And-Prompts-Pack`: `1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN`

---

## 3. How to Push Updates Live (Auto-Deploys in ~8–15 Seconds)
Run the following commands from the project root (`C:\Projects\ai-influencer-course-website`):
```powershell
git status
git add index.html styles.css app.js vercel.json .vercelignore .gitignore favicon.svg assets/ course-vault/ docs/ README.md GEMINI.md
git commit -m "chore: update storefront and documentation"
git push origin main
```
> **Operational Notes:**
> 1. Always keep `git config user.email` set to `209062033+wandringspirit@users.noreply.github.com` so Vercel Hobby builds and deploys every push automatically without exposing a personal email.
> 2. When editing [`app.js`](../app.js) or [`styles.css`](../styles.css), bump the `?v=XX` cache-buster query strings in [`index.html`](../index.html) (currently `app.js?v=25` and `styles.css?v=9`).
> 3. Run the automated storefront & vault QA scripts before major releases:
>    - `python scripts/deep_audit_vault.py`
>    - `python scripts/audit_mobile_crossdevice.py`
> 4. Large local media (`videos-captioned/`, `*.mp4`, `*.srt`, `*.zip`) and browser/log artifacts (`instagram-studio/.browser_session/`, `instagram-studio/schedule_logs/`) are ignored in [`.gitignore`](../.gitignore), and non-web studio/doc folders are excluded in [`.vercelignore`](../.vercelignore) *(note: Vercel CLI honors `.vercelignore` directly; Git-integrated Vercel deploys upload the full Git tree minus `.gitignore`, while `vercel.json` enforces `noindex` on `/course-vault/*`)*.
