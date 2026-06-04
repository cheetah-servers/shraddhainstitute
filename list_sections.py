import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all section tags and comment lines near them
lines = content.split('\n')
for i, line in enumerate(lines):
    if '<section' in line or 'SECTION' in line:
        print(f"Line {i+1}: {line.strip()}")
