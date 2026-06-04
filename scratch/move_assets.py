import os
import shutil

assets_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\assets'
scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'

# Rename and move cropped PNGs to assets
png_mappings = {
    'course_1.png': 'reading.png',
    'course_2.png': 'school.png',
    'course_3.png': 'job_seeker.png',
    'course_4.png': 'employee.png',
    'course_5.png': 'homemaker.png'
}

for src_name, dst_name in png_mappings.items():
    src_path = os.path.join(assets_dir, src_name)
    dst_path = os.path.join(assets_dir, dst_name)
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"Renamed & moved: {src_name} -> {dst_name}")
    else:
        print(f"File not found: {src_path}")

# Process and move SVGs
# For business.svg and professional.svg, just copy to assets
for svg_name in ['business.svg', 'professional.svg']:
    src_path = os.path.join(scratch_dir, svg_name)
    dst_path = os.path.join(assets_dir, svg_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied: {svg_name} to assets")

# For traveller.svg, replace green '#92E3A9' with blue '#407BFF' and copy to assets
traveller_src = os.path.join(scratch_dir, 'traveller.svg')
traveller_dst = os.path.join(assets_dir, 'traveller.svg')
if os.path.exists(traveller_src):
    content = open(traveller_src, 'r', encoding='utf-8').read()
    # Replace main green color with blue
    content_recolored = content.replace('#92E3A9', '#407BFF').replace('#92e3a9', '#407BFF')
    # Also if there's any other tint of green, let's check
    with open(traveller_dst, 'w', encoding='utf-8') as f:
        f.write(content_recolored)
    print("Recolored traveller.svg and copied to assets")
else:
    print("traveller.svg not found in scratch")
