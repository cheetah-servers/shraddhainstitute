with open("history_index_2293.html", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
start = -1
for i, line in enumerate(lines):
    if 'id="methodology"' in line or 'methodology' in line:
        start = i
        print(f"Found line {i+1}: {line}")

if start != -1:
    print("Context around start:")
    for j in range(max(0, start - 5), min(len(lines), start + 40)):
        print(f"{j+1}: {lines[j]}")
else:
    print("No methodology section in history_index_2293.html")
