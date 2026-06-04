from PIL import Image
import os

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
fname = 'media__1780537480117.png'
p = os.path.join(brain_dir, fname)
img = Image.open(p)
w, h = img.size
pix = img.load()

# Let's print colors along row y = 300
print("Colors along row y=300:")
for x in range(0, w, 20):
    print(f"x={x}: {pix[x, 300][:3]}")
