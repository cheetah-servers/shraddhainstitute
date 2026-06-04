import os

search_dir = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86"

found_any = False
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith((".py", ".txt", ".json", ".html", ".js", ".css", ".md")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if 'subtab-panel' in content and ('div' in content or 'section' in content or 'button' in content):
                    if 'daily' in content and 'school' in content:
                        print(f"Match found in: {path}")
                        found_any = True
            except Exception:
                pass

if not found_any:
    print("No matches found for HTML subtab-panel markup in artifacts.")
