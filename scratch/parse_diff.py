import os
import re

file_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\scratch\diff_index.txt"

with open(file_path, "r", encoding="utf-16le") as f:
    content = f.read()

# Split content by lines
lines = content.split('\n')
print(f"Total lines in diff_index.txt: {len(lines)}")

# Print first 50 lines to check structure
for l in lines[:100]:
    # Strip to ascii to avoid print errors
    ascii_line = l.encode('ascii', 'ignore').decode('ascii')
    print(ascii_line)
