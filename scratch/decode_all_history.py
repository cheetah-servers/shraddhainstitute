import json
import os

files = [
    ("history_index_340.html", "history_index_340_decoded.html"),
    ("history_index_2293.html", "history_index_2293_decoded.html"),
    ("history_style_342.css", "history_style_342_decoded.css"),
    ("history_style_2295.css", "history_style_2295_decoded.css"),
    ("history_script_344.js", "history_script_344_decoded.js"),
    ("history_script_2297.js", "history_script_2297_decoded.js")
]

for src, dest in files:
    if os.path.exists(src):
        with open(src, "r", encoding="utf-8") as f:
            raw = f.read().strip()
        # If it is wrapped in quotes and has escaped sequences, let's load it as JSON
        if raw.startswith('"') and raw.endswith('"'):
            try:
                decoded = json.loads(raw)
                with open(dest, "w", encoding="utf-8") as out:
                    out.write(decoded)
                print(f"Decoded {src} to {dest}")
            except Exception as e:
                # If json.loads fails due to truncation or other issues, try simple eval or raw string escape decoding
                try:
                    decoded = bytes(raw, "utf-8").decode("unicode_escape")
                    with open(dest, "w", encoding="utf-8") as out:
                        out.write(decoded)
                    print(f"Fallback-decoded {src} to {dest}")
                except Exception as e2:
                    print(f"Error decoding {src}: {e2}")
        else:
            # Maybe it is already decoded or just a raw string
            print(f"{src} is not JSON wrapped")
    else:
        print(f"File {src} does not exist.")
