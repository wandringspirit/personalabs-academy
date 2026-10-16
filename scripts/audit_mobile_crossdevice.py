import os
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

VAULT_DIR = r"C:\Projects\ai-influencer-course-website\course-vault"
ROOT_DIR = r"C:\Projects\ai-influencer-course-website"

print("="*80)
print("DEEP MOBILE & CROSS-DEVICE RESPONSIVENESS AUDIT")
print("="*80)

html_files = [f for f in os.listdir(VAULT_DIR) if f.endswith(".html")]

issues = {
    "ios_input_zoom": [],
    "table_overflow_risk": [],
    "code_overflow_risk": [],
    "fixed_width_risk": [],
    "missing_images": [],
    "query_param_loss_on_back": []
}

for fname in sorted(html_files):
    fpath = os.path.join(VAULT_DIR, fname)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. Check iOS Safari Auto-Zoom Risk (<input>, <select>, <textarea> with font-size < 16px)
    inputs = soup.find_all(["input", "select", "textarea"])
    if inputs:
        # Check if styles specify font-size < 16px
        style_blocks = "".join([s.get_text() for s in soup.find_all("style")])
        font_matches = re.findall(r'(?:input|select|textarea)[^{]*\{[^}]*font-size:\s*([^;]+);', style_blocks, re.I)
        for fs in font_matches:
            fs_clean = fs.strip()
            # If px < 16px or rem < 1rem
            if ('px' in fs_clean and float(re.search(r'[\d.]+', fs_clean).group()) < 16) or \
               ('rem' in fs_clean and float(re.search(r'[\d.]+', fs_clean).group()) < 1.0):
                issues["ios_input_zoom"].append((fname, fs_clean))

    # 2. Check Table Overflow on Mobile (<table without responsive wrapper)
    tables = soup.find_all("table")
    for t in tables:
        parent = t.parent
        parent_class = parent.get("class", [])
        parent_style = parent.get("style", "")
        # Check if table itself or parent has overflow-x auto or table-responsive class
        t_style = t.get("style", "")
        if "overflow" not in t_style and "overflow" not in str(parent_style) and "table-responsive" not in parent_class:
            # check CSS
            t_class = t.get("class", ["table"])
            issues["table_overflow_risk"].append((fname, t_class))

    # 3. Check Code Blocks Overflow (<pre>, .prompt-code, .script-code)
    code_blocks = soup.find_all(class_=re.compile(r'(prompt-code|script-code|code)'))
    style_blocks = "".join([s.get_text() for s in soup.find_all("style")])
    if code_blocks and "overflow-x" not in style_blocks and "overflow:" not in style_blocks:
        issues["code_overflow_risk"].append(fname)

    # 4. Check Fixed Widths > 320px in CSS
    fixed_widths = re.findall(r'width:\s*([4-9]\d{2}|[1-9]\d{3,})px', style_blocks)
    if fixed_widths:
        issues["fixed_width_risk"].append((fname, set(fixed_widths)))

    # 5. Check Image Sources Exist on Disk
    imgs = soup.find_all("img")
    for img in imgs:
        src = img.get("src", "")
        if src and not src.startswith("http") and not src.startswith("data:"):
            img_path = os.path.normpath(os.path.join(VAULT_DIR, src.split("?")[0]))
            if not os.path.exists(img_path):
                issues["missing_images"].append((fname, src, img_path))

    # 6. Check Back Link Query Preservation
    back_links = soup.find_all("a", href=re.compile(r'index\.html$'))
    if back_links:
        # Check if there is JS updating href with location.search
        if "location.search" not in content and "URLSearchParams" not in content:
            issues["query_param_loss_on_back"].append(fname)

print("--- 1. iOS SAFARI AUTO-ZOOM AUDIT (font-size < 16px on inputs) ---")
if issues["ios_input_zoom"]:
    for f, fs in issues["ios_input_zoom"]:
        print(f"⚠️  WARNING: In {f}, input font-size is '{fs}' (<16px). iOS Safari will force-zoom page on tap!")
else:
    print("✅ PASSED: No iOS Safari input zoom triggers detected.")

print("\n--- 2. TABLE HORIZONTAL OVERFLOW ON MOBILE ---")
if issues["table_overflow_risk"]:
    for f, tc in issues["table_overflow_risk"]:
        print(f"⚠️  WARNING: In {f}, table with class {tc} may cause horizontal blowout on screens <400px if not wrapped in overflow-x: auto!")
else:
    print("✅ PASSED: Tables wrapped or formatted for small screens.")

print("\n--- 3. CODE & PROMPT BLOCK SCROLLING ---")
if issues["code_overflow_risk"]:
    for f in issues["code_overflow_risk"]:
        print(f"⚠️  WARNING: In {f}, code blocks may overflow screen width.")
else:
    print("✅ PASSED: Code blocks have overflow scroll / wrapping configured.")

print("\n--- 4. FIXED PIXEL WIDTHS (>320px) AUDIT ---")
if issues["fixed_width_risk"]:
    for f, widths in issues["fixed_width_risk"]:
        print(f"ℹ️  INFO: In {f}, fixed pixel widths found: {widths} (Verify min-width vs max-width vs media queries)")
else:
    print("✅ PASSED: No dangerous fixed pixel widths found.")

print("\n--- 5. IMAGE ASSET INTEGRITY ---")
if issues["missing_images"]:
    for f, src, p in issues["missing_images"]:
        print(f"❌ FAILED: In {f}, image src='{src}' NOT found at: {p}")
else:
    print("✅ PASSED: All local images resolve correctly.")

print("\n--- 6. QUERY PARAMETER PRESERVATION (BACK LINKS) ---")
if issues["query_param_loss_on_back"]:
    for f in issues["query_param_loss_on_back"]:
        print(f"⚠️  WARNING: In {f}, back button navigates to 'index.html' directly, stripping URL query parameters (email/tx/vt1/vt2)!")
else:
    print("✅ PASSED: Back navigation maintains session query parameters.")

print("\n" + "="*80)
