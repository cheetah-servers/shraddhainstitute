from PIL import Image
import os

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
media_files = [
    'media__1780536406822.png',
    'media__1780537480117.png',
    'media__1780537611394.png',
    'media__1780537782288.png',
    'media__1780537925162.png',
    'media__1780538093603.png'
]

for idx, fname in enumerate(media_files):
    p = os.path.join(brain_dir, fname)
    if not os.path.exists(p):
        continue
    img = Image.open(p)
    w, h = img.size
    pix = img.load()
    
    # We want to find the horizontal and vertical projection of white pixels
    # A canvas is a large area of white pixels. Let's find columns and rows that are mostly white.
    # More simply, let's look at a grid of pixels and print their colors, or find the bounding box of the illustration
    # drawing (which consists of colored pixels on a white canvas).
    # If the canvas itself is white, the drawing pixels are the non-white pixels.
    # Let's find the bounding box of the colored drawing inside the canvas.
    # We know the canvas is located roughly between x=150 and x=650.
    # Let's scan each column and row to see where the non-white pixels are.
    col_has_color = [False] * w
    row_has_color = [False] * h
    
    # We only scan between y=100 and y=500, and x=100 and x=700 to avoid headers, sidebar, etc.
    for x in range(100, 700):
        for y in range(100, 500):
            r, g, b = pix[x, y][:3]
            # If it is not white and not the grey background (usually #f0f0f0 or #e0e0e0)
            # Let's say if color is not close to white and not grey (where r, g, b are almost equal and between 200 and 245)
            is_white = (r > 240 and g > 240 and b > 240)
            is_grey = (abs(r - g) < 5 and abs(g - b) < 5 and r > 180 and r < 245)
            if not is_white and not is_grey:
                col_has_color[x] = True
                row_has_color[y] = True
                
    # Find bounding box of colored region
    color_cols = [x for x in range(w) if col_has_color[x]]
    color_rows = [y for y in range(h) if row_has_color[y]]
    
    if color_cols and color_rows:
        left, right = color_cols[0], color_cols[-1]
        top, bottom = color_rows[0], color_rows[-1]
        print(f"{fname}: detected colored bbox = ({left}, {top}, {right}, {bottom}), width={right-left}, height={bottom-top}")
    else:
        print(f"{fname}: no colored region detected")
