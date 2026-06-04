import re
import os

scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'
for name in ['business', 'professional', 'traveller']:
    p = os.path.join(scratch_dir, f"{name}.svg")
    if os.path.exists(p):
        content = open(p, 'r', encoding='utf-8').read()
        hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', content))
        print(f"{name}.svg hex colors: {hex_colors}")
