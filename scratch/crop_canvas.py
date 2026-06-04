from PIL import Image
import os

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
assets_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\assets'

media_files = [
    'media__1780536406822.png',
    'media__1780537480117.png',
    'media__1780537611394.png',
    'media__1780537782288.png',
    'media__1780537925162.png',
    'media__1780538093603.png'
]

# We will analyze each image and save the cropped main preview canvas
for idx, fname in enumerate(media_files):
    p = os.path.join(brain_dir, fname)
    if not os.path.exists(p):
        continue
    img = Image.open(p)
    w, h = img.size
    pix = img.load()
    
    # Restrict search area to avoid headers, sidebar, side buttons, etc.
    # The Storyset canvas is centered horizontally around x=390 (from x=245 to 545).
    # The Lottie canvas is from x=150 to 550.
    # So we search x from 160 to 560, and y from 130 to 470.
    left, top, right, bottom = w, h, 0, 0
    for x in range(160, 560):
        for y in range(130, 470):
            r, g, b = pix[x, y][:3]
            is_white = (r > 248 and g > 248 and b > 248)
            is_page_grey = (abs(r - g) < 3 and abs(g - b) < 3 and r >= 235 and r <= 245)
            # If it has actual color
            if not is_white and not is_page_grey:
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
                
    if right > left and bottom > top:
        pad = 20
        crop_left = max(0, left - pad)
        crop_top = max(0, top - pad)
        crop_right = min(w, right + pad)
        crop_bottom = min(h, bottom + pad)
        
        cropped_drawing = img.crop((crop_left, crop_top, crop_right, crop_bottom))
        drawing_w, drawing_h = cropped_drawing.size
        
        # We can make it a square image
        canvas_size = max(drawing_w, drawing_h, 300)
        new_img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
        
        offset_x = (canvas_size - drawing_w) // 2
        offset_y = (canvas_size - drawing_h) // 2
        new_img.paste(cropped_drawing, (offset_x, offset_y))
        
        out_name = f"course_{idx}.png"
        out_path = os.path.join(assets_dir, out_name)
        new_img.save(out_path)
        print(f"Processed {fname} -> {out_name} (box: {crop_left}, {crop_top}, {crop_right}, {crop_bottom})")
    else:
        print(f"Could not find drawing in {fname}")
