from PIL import Image
import os

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
for f in os.listdir(brain_dir):
    if f.startswith('media__') and f.endswith('.png'):
        p = os.path.join(brain_dir, f)
        img = Image.open(p)
        print(f"{f}: size={img.size}, format={img.format}")
