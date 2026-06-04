with open("index_recovered.html", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
start = -1
end = -1
for i, line in enumerate(lines):
    if 'id="methodology"' in line or 'id="about"' in line:
        start = i
        print(f"Start in recovered at line {i+1}: {line}")
    if start != -1 and 'id="courses"' in line:
        end = i
        print(f"End in recovered at line {i+1}: {line}")
        break

if start != -1 and end != -1:
    print("Found methodology section in index_recovered.html:")
    for j in range(start, end + 1):
         print(f"{j+1}: {lines[j]}")
else:
    print("Not found start/end in index_recovered.html")
