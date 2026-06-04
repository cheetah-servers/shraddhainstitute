from PIL import Image
import os
from collections import Counter

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
fname = 'media__1780537611394.png'
p = os.path.join(brain_dir, fname)
img = Image.open(p)
w, h = img.size
pix = img.load()

# Let's count colors inside the illustration canvas
colors = []
for x in range(300, 500):
    for y in range(200, 400):
        r, g, b = pix[x, y][:3]
        # Ignore white, black, grey
        if not (r > 240 and g > 240 and b > 240) and not (r < 30 and g < 30 and b < 30) and abs(r-g) > 10:
            colors.append((r, g, b))

counter = Counter(colors)
print("Most common colors:")
for c, count in counter.most_common(10):
    print(f"Color: #{c[0]:02x}{c[1]:02x}{c[2]:02x} ({c}), Count: {count}")
