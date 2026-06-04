import os

files = ["history_index_340.html", "history_index_2293.html"]
for file in files:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\nFile: {file}")
        print(f"Contains 'subtab-panel': {'subtab-panel' in content}")
        print(f"Contains 'grammar-method': {'grammar-method' in content}")
        print(f"Contains 'Daily Convers.': {'Daily Convers.' in content}")
        if 'subtab-panel' in content:
            # print where it is
            lines = content.splitlines()
            for idx, line in enumerate(lines):
                if 'subtab-panel' in line:
                    print(f"Line {idx+1}: {line.strip()}")
    else:
        print(f"File {file} does not exist.")
