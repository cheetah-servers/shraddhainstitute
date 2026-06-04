import os

css_path = r"c:\Users\metpa\OneDrive\Documents\shraddha institute\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# We look for the comment indicating the start of Scroll Reveal Utilities
# Both \r\n and \n styles are handled.
marker = "/* ==========================================\n   SCROLL REVEAL UTILITIES"
marker_rn = "/* ==========================================\r\n   SCROLL REVEAL UTILITIES"

first_idx = content.find(marker)
if first_idx == -1:
    first_idx = content.find(marker_rn)

if first_idx == -1:
    print("Could not find the first occurrence of the marker.")
    exit(1)

# Find the second occurrence after the first one
second_idx = content.find(marker, first_idx + len(marker))
if second_idx == -1:
    second_idx = content.find(marker_rn, first_idx + len(marker_rn))

if second_idx == -1:
    print("Could not find the second occurrence of the marker.")
    exit(1)

print(f"First occurrence index: {first_idx}")
print(f"Second occurrence index: {second_idx}")
print("Section to remove (first 100 chars):")
print(content[first_idx:first_idx+100])
print("...")
print("Section to remove (last 100 chars):")
print(content[second_idx-100:second_idx])

# Perform the deletion
new_content = content[:first_idx] + content[second_idx:]

with open(css_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully cleaned up style.css!")
