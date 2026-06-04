import os

def check_file(path):
    if not os.path.exists(path):
        print(f"File {path} does not exist")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Unescape if it has literal backslash-n
    unescaped = content.replace("\\n", "\n").replace("\\\"", "\"").replace("\\\\", "\\")
    
    print(f"\n--- Checking: {path} ---")
    print(f"Unescaped length: {len(unescaped)}")
    print(f"Contains 'Daily Convers.': {'Daily Convers.' in unescaped}")
    print(f"Contains 'subtab-panel': {'subtab-panel' in unescaped}")
    print(f"Contains 'grammar-method': {'grammar-method' in unescaped}")
    
    # Save the unescaped file
    out_path = path.replace(".html", "_unescaped.html").replace(".css", "_unescaped.css").replace(".js", "_unescaped.js")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(unescaped)
    print(f"Saved unescaped to {out_path}")

check_file("history_index_340.html")
check_file("history_index_2293.html")
check_file("history_style_342.css")
check_file("history_style_2295.css")
check_file("history_script_344.js")
check_file("history_script_2297.js")
