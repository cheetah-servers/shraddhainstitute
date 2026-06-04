with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

keywords = ["methodology-showcase", "showcase-player-frame", "showcase-video"]
for keyword in keywords:
    if keyword in content:
        print(f"Found keyword '{keyword}' in style.css")
