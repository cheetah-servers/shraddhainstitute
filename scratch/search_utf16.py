import os

file_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\scratch\diff_index.txt"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-16le") as f:
        content = f.read()
    print("Content length:", len(content))
    
    # Search for keywords
    for keyword in ["courses-slider", "card-stack", "benefits", "methodology", "empowers"]:
        pos = content.lower().find(keyword.lower())
        if pos != -1:
            print(f"Keyword '{keyword}' found at position {pos}")
            # print it safely by encoding to utf-8 or stripping non-ascii
            snippet = content[max(0, pos-100):min(len(content), pos+200)].strip().replace('\n', ' ')
            safe_snippet = snippet.encode('ascii', 'ignore').decode('ascii')
            print("  Snippet:", safe_snippet)
else:
    print("File does not exist.")
