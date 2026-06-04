import os

keywords = ["dialogue", "metro", "reframing", "Where is"]
search_dir = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith((".py", ".txt", ".json", ".html", ".js", ".css", ".md")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        print(f"Found '{keyword}' in {path}")
            except Exception:
                pass
