import re
import os
import shutil

scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'
assets_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\assets'

files = ['school.svg', 'job_seeker.svg', 'employee.svg']

for f in files:
    src_path = os.path.join(scratch_dir, f)
    dst_path = os.path.join(assets_dir, f)
    if os.path.exists(src_path):
        content = open(src_path, 'r', encoding='utf-8').read()
        hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', content))
        print(f"{f} contains hex colors: {hex_colors}")
        
        # We want to check if the main color is not #407BFF (often Storyset uses #3F51B5 or #6C63FF as default)
        # Let's replace any occurrences of standard Storyset colors like #3f51b5 or #6c63ff with #407BFF.
        # But wait! Storyset default green is #92E3A9, default indigo is #3F51B5, default violet is #6C63FF.
        # Let's replace standard storyset colors with #407BFF.
        # Let's write a general replacement:
        # #3F51B5 -> #407BFF (indigo)
        # #6C63FF -> #407BFF (violet)
        # #00B0FF -> #407BFF (blue)
        # #3F3D56 -> #263238 (dark charcoal)
        # We can do this replacement directly in the text.
        recolored = content
        
        # Let's look at the colors in the file:
        # If we see 3f51b5, 6c63ff, or other colors, we replace them.
        recolored = recolored.replace('#3F51B5', '#407BFF').replace('#3f51b5', '#407BFF')
        recolored = recolored.replace('#6C63FF', '#407BFF').replace('#6c63ff', '#407BFF')
        recolored = recolored.replace('#00B0FF', '#407BFF').replace('#00b0ff', '#407BFF')
        recolored = recolored.replace('#3F3D56', '#263238').replace('#3f3d56', '#263238')
        
        # Let's save it to assets
        with open(dst_path, 'w', encoding='utf-8') as out_f:
            out_f.write(recolored)
        print(f"Recolored and copied {f} to {dst_path}")
        
        # Delete old PNG if it exists
        old_png = os.path.join(assets_dir, f.replace('.svg', '.png'))
        if os.path.exists(old_png):
            os.remove(old_png)
            print(f"Removed old PNG: {old_png}")
