import re
from bs4 import BeautifulSoup

html_path = r"c:\Users\metpa\OneDrive\Documents\shraddha institute\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("--- HTML Static Audit ---")

# 1. Heading Check
h1s = soup.find_all("h1")
print(f"Number of <h1> tags: {len(h1s)}")
for idx, h1 in enumerate(h1s):
    print(f" - h1 #{idx+1}: '{h1.text.strip()}' (ID: {h1.get('id')})")

# 2. Duplicate IDs Check
ids = {}
for el in soup.find_all(id=True):
    el_id = el.get("id")
    ids[el_id] = ids.get(el_id, 0) + 1

duplicate_ids = {k: v for k, v in ids.items() if v > 1}
if duplicate_ids:
    print(f"WARNING: Duplicate IDs found: {duplicate_ids}")
else:
    print("OK: No duplicate IDs found.")

# 3. Anchor links check
all_anchors = soup.find_all("a", href=True)
broken_links = []
for a in all_anchors:
    href = a.get("href")
    if href.startswith("#") and len(href) > 1:
        target_id = href[1:]
        if not soup.find(id=target_id):
            broken_links.append((a.text.strip(), href))

if broken_links:
    print(f"WARNING: Broken section links found: {broken_links}")
else:
    print("OK: All anchor section links correspond to active IDs.")

# 4. Images alt tags check
images = soup.find_all("img")
images_missing_alt = []
for img in images:
    if not img.get("alt"):
        images_missing_alt.append(img.get("src"))

if images_missing_alt:
    print(f"WARNING: Images missing alt attributes: {images_missing_alt}")
else:
    print("OK: All images have alt attributes.")

# 5. Interactive elements accessibility check (aria-expanded, role, labels)
modal_overlays = soup.find_all(class_="modal-overlay")
for modal in modal_overlays:
    print(f"Modal Found: class={modal.get('class')}, id={modal.get('id')}, role={modal.get('role')}, aria-modal={modal.get('aria-modal')}")

print("\nAudit completed.")
