import os
import re
import sys
from bs4 import BeautifulSoup

# Ensure utf-8 output on Windows console
sys.stdout.reconfigure(encoding='utf-8')

VAULT_DIR = r"C:\Projects\ai-influencer-course-website\course-vault"
ROOT_DIR = r"C:\Projects\ai-influencer-course-website"

print("="*80)
print("DEEP AUDIT OF COURSE VAULT & DELIVERY SYSTEM")
print("="*80)

vault_files = [f for f in os.listdir(VAULT_DIR) if f.endswith(".html")]
print(f"Auditing {len(vault_files)} HTML files in course-vault: {vault_files}\n")

EXPECTED_DRIVE_IDS = {
    "core": "1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm",
    "uncensored": "10HGXWcRMR898lbQnTX41G--fPLKoBOvW",
    "hooks": "1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN"
}

findings = {
    "broken_internal_links": [],
    "outdated_drive_links": [],
    "drive_links_found": [],
    "missing_viewport": [],
    "hardcoded_local_paths": [],
    "onclick_handlers": [],
    "js_errors_or_dom_issues": [],
    "button_or_interactive_elements": [],
    "media_queries_found": {}
}

for fname in sorted(vault_files):
    fpath = os.path.join(VAULT_DIR, fname)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. Viewport Check
    viewport = soup.find("meta", attrs={"name": "viewport"})
    if not viewport:
        findings["missing_viewport"].append(fname)
    
    # 2. Hardcoded local path check
    local_matches = re.findall(r'(file:///|[A-Za-z]:\\[^"\'\s<>]+)', content)
    if local_matches:
        findings["hardcoded_local_paths"].append((fname, local_matches))
        
    # 3. All <a> links
    for a in soup.find_all("a", href=True):
        href = a['href'].strip()
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        
        # Check Google Drive links
        if "drive.google.com" in href:
            match = re.search(r'folders/([a-zA-Z0-9_-]+)', href)
            folder_id = match.group(1) if match else "UNKNOWN"
            anchor_text = a.get_text(strip=True)[:40]
            findings["drive_links_found"].append((fname, href, folder_id, anchor_text))
            
            if folder_id not in EXPECTED_DRIVE_IDS.values():
                findings["outdated_drive_links"].append((fname, href, folder_id, anchor_text))
        
        # Check internal relative links
        elif not href.startswith("http://") and not href.startswith("https://") and not href.startswith("mailto:") and not href.startswith("tel:"):
            clean_href = href.split("?")[0].split("#")[0]
            if clean_href:
                target_path = os.path.normpath(os.path.join(VAULT_DIR, clean_href))
                if not os.path.exists(target_path):
                    findings["broken_internal_links"].append((fname, href, clean_href, a.get_text(strip=True)[:40]))

    # 4. Check all onclick handlers
    for el in soup.find_all(attrs={"onclick": True}):
        onclick = el['onclick']
        findings["onclick_handlers"].append((fname, onclick, el.name, el.get_text(strip=True)[:30]))

    # 5. Extract style / CSS media queries
    styles = soup.find_all("style")
    mq_list = []
    for s in styles:
        text = s.get_text()
        mqs = re.findall(r'@media[^{]+', text)
        mq_list.extend([m.strip() for m in mqs])
    findings["media_queries_found"][fname] = mq_list

print("--- 1. VIEWPORT & RESPONSIVE TAGS ---")
if findings["missing_viewport"]:
    print(f"❌ FAILED: Missing viewport meta tag in: {findings['missing_viewport']}")
else:
    print("✅ PASSED: All 5 vault HTML pages contain responsive viewport meta tags.")

print("\n--- 2. HARDCODED LOCAL PATHS ---")
if findings["hardcoded_local_paths"]:
    print(f"❌ FAILED: Potential local file paths found:")
    for f, matches in findings["hardcoded_local_paths"]:
        print(f"   In {f}: {matches}")
else:
    print("✅ PASSED: Zero hardcoded local paths found.")

print("\n--- 3. INTERNAL LINK AUDIT (BROKEN LINKS) ---")
if findings["broken_internal_links"]:
    print(f"❌ FAILED: {len(findings['broken_internal_links'])} broken internal link(s) detected:")
    for f, href, clean, text in findings["broken_internal_links"]:
        print(f"   [File: {f}] Link: '{href}' -> Target '{clean}' MISSING on disk! (Anchor: '{text}')")
else:
    print("✅ PASSED: 100% of internal links resolve to valid on-disk files.")

print("\n--- 4. GOOGLE DRIVE LINK AUDIT ---")
print(f"Total Google Drive links detected: {len(findings['drive_links_found'])}")
for fname, href, fid, text in findings["drive_links_found"]:
    matched_type = [k for k, v in EXPECTED_DRIVE_IDS.items() if v == fid]
    t_str = matched_type[0].upper() if matched_type else "UNKNOWN/OUTDATED"
    print(f"   [{fname}] -> [{t_str}] Folder ID: {fid} | Anchor: '{text}'")

if findings["outdated_drive_links"]:
    print(f"\n❌ FAILED: {len(findings['outdated_drive_links'])} outdated Drive link(s) detected:")
    for item in findings["outdated_drive_links"]:
        print(f"   File: {item[0]} | Link: {item[1]} | ID: {item[2]}")
else:
    print("✅ PASSED: All Google Drive links match the 3 active public folders.")

print("\n--- 5. MEDIA QUERIES / RESPONSIVENESS AUDIT ---")
for f, mqs in findings["media_queries_found"].items():
    print(f"   [{f}] -> {len(mqs)} media query rules defined: {mqs}")

print("\n--- 6. ONCLICK HANDLERS IN VAULT ---")
print(f"Total onclick handlers detected: {len(findings['onclick_handlers'])}")
unique_funcs = set()
for f, onclick, el_name, text in findings["onclick_handlers"]:
    func_name = onclick.split("(")[0].strip()
    unique_funcs.add((f, func_name))
for f, fn in sorted(unique_funcs):
    print(f"   [{f}] Function invoked: {fn}()")

print("\n" + "="*80)
print("AUDIT SCRIPT COMPLETE")
print("="*80)
