# 🚀 Deployment & Operations Guide (`DEPLOY.md`)

## 1. Live Production Architecture
- **Live Domain:** `https://personalabs.store`
- **Netlify Project:** `endearing-phoenix-5cc220`
- **GitHub Repository:** `https://github.com/wandringspirit/ai-influencer-course-website` (Branch: `main`)
- **Deployment Trigger:** Every `git push origin main` automatically deploys to `https://personalabs.store` in ~15 seconds.

---

## 2. How to Push Website Updates Live
Run the following commands from `C:\Projects\ai-influencer-course-website`:
```powershell
git status
git add index.html styles.css app.js course-vault/ assets/ *.md
git commit -m "Update storefront and documentation"
git push origin main
```
> **Note:** Large video files (`videos/`, `videos-captioned/`, `*.mp4`, `*.srt`, `*.zip`) are excluded in `.gitignore` so GitHub pushes and Netlify deploys stay instantaneous.

---

## 3. Dedicated Brand Gmail & 3-Folder Google Drive Setup (IMPORTANT REMINDER)
To keep your personal identity 100% private and manage add-on access cleanly:
1. **Create a Dedicated Brand Gmail Account:**
   - Create `personalabs.academy@gmail.com` (or `official.personalabs@gmail.com`).
   - **Never** share files from your personal Gmail account (`Google Drive -> Info -> Owner` displays the owner's email/name to anyone with the link).
2. **Upload 3 Separate Shared Folders in Google Drive:**
   - **Folder 1 (`01-Core-Course-Videos`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\01-Core-Course-Videos\` (19 Core Videos + `Bonus.docx` + `readme.docx` + `250-AI-Character-DNA-Prompt-Bible.html`).
     - Set sharing to: *Anyone with the link -> Viewer* (Disable download/reshare in Drive settings if desired).
   - **Folder 2 (`02-Uncensored-NSFW-Addon-Videos`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\02-Uncensored-NSFW-Addon-Videos\` (4 Exclusive NSFW FaceSwap Videos + `Uncensored-Content-Hack-VIP-Guide.html`).
     - Share link **ONLY** with buyers of **Order Bump #1 (`Uncensored Content Hack`)**.
   - **Folder 3 (`03-500-Viral-Hooks-And-Prompts-Pack`)**: Upload everything inside `C:\Projects\ai-influencer-course-website\videos-captioned\03-500-Viral-Hooks-And-Prompts-Pack\` (`500-Viral-Reel-Hooks-And-AutoDM-Pack.html` + `250-AI-Character-DNA-Prompt-Bible.html`).
     - Share link **ONLY** with buyers of **Order Bump #2 (`500+ Viral Reel Hooks & Auto-DM Pack`)**.
