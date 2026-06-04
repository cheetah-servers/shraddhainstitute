import os
from PIL import Image

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'

# Ensure scratch directory exists
os.makedirs(scratch_dir, exist_ok=True)

# List of media files in order
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
        print(f"Skipping {fname} - does not exist")
        continue
    
    img = Image.open(p)
    w, h = img.size
    
    # We will search for non-white pixels inside a central bounding box where the illustration is
    # to avoid header/sidebar elements
    # For Storyset, the illustration is in the center-left. For Lottie, it is in the center-left.
    # Let's crop:
    # Lottie canvas: x in [50, 600], y in [100, 500]
    # Storyset canvas: x in [240, 540], y in [300, 840]
    # Let's write a robust crop for each based on the file contents.
    # Alternatively, let's crop a few standard regions and print information.
    # Let's do a bounding box detection on the central region [50, 700] x [100, 500]
    left, top, right, bottom = w, h, 0, 0
    pix = img.load()
    
    # Define search region to avoid browser chrome (top bar is ~80px, bottom taskbar is ~40px, right sidebar is ~300px)
    search_x_min = 40
    search_x_max = 700
    search_y_min = 100
    search_y_max = 500
    
    for y in range(search_y_min, search_y_max):
        for x in range(search_x_min, search_x_max):
            r, g, b = pix[x, y][:3]
            # If the pixel is not white or near-white (background of canvas is white)
            if not (r > 245 and g > 245 and b > 245):
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
                
    if right > left and bottom > top:
        # Add some padding
        pad = 20
        left = max(0, left - pad)
        top = max(0, top - pad)
        right = min(w, right + pad)
        bottom = min(h, bottom + pad)
        
        cropped = img.crop((left, top, right, bottom))
        out_path = os.path.join(scratch_dir, f"cropped_{idx}.png")
        cropped.save(out_path)
        print(f"Cropped {fname} -> {out_path} (box: {left}, {top}, {right}, {bottom})")
    else:
        # Fallback: crop center-left
        cropped = img.crop((100, 100, 600, 500))
        out_path = os.path.join(scratch_dir, f"cropped_{idx}.png")
        cropped.save(out_path)
        print(f"Fallback crop {fname} -> {out_path}")
