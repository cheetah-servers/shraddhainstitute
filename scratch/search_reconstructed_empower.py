import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for how learning english empowers you or benefits
matches = list(re.finditer(r'(empower|benefit|card-stack)', content, re.IGNORECASE))
print(f"Found {len(matches)} occurrences:")
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"Pos {m.start()} (context): {content[start:end].strip().replace('\n', ' ')}")
