import os

VAULT_HTML = r"C:\Projects\ai-influencer-course-website\course-vault\index.html"

def make_day_banner(day_num, vid_range):
    return f"""          <div style="margin-top:0.85rem;display:flex;align-items:center;gap:0.75rem;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.35);padding:0.55rem 0.95rem;border-radius:10px;flex-wrap:wrap;">
            <span style="font-size:1.1rem;">🎬</span>
            <div style="flex:1;min-width:200px;">
              <strong style="color:#34d399;font-size:0.84rem;display:block;">Step-by-Step HD Video Walkthroughs ({vid_range})</strong>
              <span style="color:#94a3b8;font-size:0.76rem;">Watch screen recordings on Google Drive, then copy prompts below:</span>
            </div>
            <a href="https://drive.google.com/drive/folders/1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm?usp=sharing" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:0.4rem;background:#10b981;color:#052e16;font-weight:700;font-size:0.8rem;padding:0.4rem 0.85rem;border-radius:8px;text-decoration:none;box-shadow:0 2px 10px rgba(16,185,129,0.25);">
              <span>▶️ Watch Day {day_num} Videos on Drive ↗</span>
            </a>
          </div>"""

def run():
    with open(VAULT_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    targets = [
        (2, "Learn how top AI agencies keep the exact same face across 500+ posts using IP-Adapter FaceID, InsightFace Swap, ControlNet OpenPose, and skin-imperfection LoRAs.", "Videos 5–8"),
        (3, "Static photos build trust, but 9:16 Vertical Reels bring 95% of your free organic followers. Master Kling AI, Hailuo MiniMax, Luma, Lip-Syncing, and the CapCut 60fps Upscale Hack.", "Videos 9–13"),
        (4, "How to launch a brand-new Instagram account without getting stuck in the \"0-View Jail\", trigger non-follower recommendations, and convert comments into DMs automatically.", "Videos 18–19"),
        (5, "You don't need 100,000 followers to make money. Learn how to monetize from your very first 1,000 followers using Affiliate Auto-DMs, Exclusive Vault Subscriptions, D2C Brand Deals, and AI Creation Retainers.", "Videos 20–22"),
    ]

    for d_num, para, v_range in targets:
        anchor = f"<p>{para}</p>\n        </div>"
        banner = make_day_banner(d_num, v_range)
        if f"Watch Day {d_num} Videos on Drive" not in html and anchor in html:
            repl = f"<p>{para}</p>\n{banner}\n        </div>"
            html = html.replace(anchor, repl, 1)
            print(f"[OK] Added Drive Video banner to Day {d_num}")

    with open(VAULT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print("All Days updated in course-vault/index.html!")

if __name__ == "__main__":
    run()
