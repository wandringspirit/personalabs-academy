# 🚀 Deployment & Operations Guide (`DEPLOY.md`)

## 1. Live Production Architecture
- **Live Domain:** `https://personalabs.store` & `https://www.personalabs.store` (`https://ai-influencer-course-website.vercel.app`)
- **GitHub Repository:** `https://github.com/wandringspirit/ai-influencer-course-website` (Branch: `main`, **Private** repository so `/course-vault/` VIP filenames and `/docs/` stay hidden from public search)
- **Git Author Identity:** `PersonaLabs Academy <personalabsacademy@gmail.com>`
- **Active CDN Host:** **Vercel Global Edge CDN** (`A @` → `216.198.79.1`, `CNAME www` → `847062401d7e0c68.vercel-dns-017.com`, 100 free production deploys/day)
- **Host Config:** [`vercel.json`](../vercel.json) (Zero-build static deployment, instant cache invalidation on `index.html`/`app.js`/`styles.css`, and `X-Robots-Tag: noindex, nofollow` on `/course-vault/*`)

---

## 2. Switching from Netlify (300-Credit Cap) to Vercel Free (100 Deploys/Day)
Why **Vercel Hobby (Free)** instead of GitHub Pages Free:
- GitHub Pages Free requires making the GitHub repository **Public**, which would expose `/docs/` and the secret VIP filenames inside `/course-vault/` (`uncensored-vip-8f92a1c4.html` & `hooks-vip-3d7e91b2.html`).
- **Vercel Free** deploys directly from your **Private** GitHub repository (`wandringspirit/ai-influencer-course-website`) for **$0 forever**, giving you **100 production deploys per day (3,000/month)** instead of Netlify's 20/month.

### 3-Click Setup (Whenever We Next Push Website Changes):
1. Sign in to **[vercel.com](https://vercel.com)** using **Continue with GitHub** (`wandringspirit`).
2. Click **Add New → Project** → Import `wandringspirit/ai-influencer-course-website` → Click **Deploy** ([`vercel.json`](../vercel.json) configures everything automatically).
3. In Vercel **Project Settings → Domains**, add `personalabs.store` and update your Namecheap DNS records (`dns1.registrar-servers.com`):
   - **`A` Record (`@`):** `76.76.21.21` (replaces Netlify's `75.2.60.5`)
   - **`CNAME` Record (`www`):** `cname.vercel-dns.com`

---

## 3. How to Push Website Updates Live
Run the following commands from `C:\Projects\ai-influencer-course-website`:
```powershell
git status
git add index.html styles.css app.js vercel.json course-vault/ assets/ docs/
git commit -m "Update storefront and documentation"
git push origin main
```
> **Note:** Large video files (`videos/`, `videos-captioned/`, `ads-ready/`, `*.mp4`, `*.srt`, `*.zip`) are excluded in `.gitignore` so GitHub pushes and static CDN deploys stay instantaneous.

---

## 4. Dedicated Brand Gmail & 3-Folder Google Drive Setup
To keep your personal identity 100% private and automate add-on access:
1. **Use Only Your Brand Gmail Account (`personalabsacademy@gmail.com`):**
   - **Never** share files from your personal Gmail account (`Google Drive -> Info -> Owner` displays the owner's email/name to viewers).
2. **Upload 3 Separate Restricted Folders in Google Drive (`personalabsacademy@gmail.com`):**
   - **Folder 1 (`01-Core-Course-Videos`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\01-Core-Course-Videos\` (19 Core Videos + `Bonus.docx` + `readme.docx` + `250-AI-Character-DNA-Prompt-Bible.html`).
   - **Folder 2 (`02-Uncensored-NSFW-Addon-Videos`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\02-Uncensored-NSFW-Addon-Videos\` (4 Exclusive NSFW FaceSwap Videos + `Uncensored-Content-Hack-VIP-Guide.html`).
   - **Folder 3 (`03-500-Viral-Hooks-And-Prompts-Pack`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\03-500-Viral-Hooks-And-Prompts-Pack\` (`500-Viral-Reel-Hooks-And-AutoDM-Pack.html` + `250-AI-Character-DNA-Prompt-Bible.html`).
3. **Keep All 3 Folders Set to `Restricted` & Paste IDs into Google Apps Script:**
   - See [`docs/GOOGLE-SHEETS-DATABASE-SETUP.md`](GOOGLE-SHEETS-DATABASE-SETUP.md) — `DriveApp.addViewer(buyerEmail)` automatically grants Viewer access to each buyer's Gmail immediately upon verified checkout.
