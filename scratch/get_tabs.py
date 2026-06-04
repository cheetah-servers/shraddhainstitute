from PIL import Image
import os

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
for idx, f in enumerate(os.listdir(brain_dir)):
    if f.startswith('media__') and f.endswith('.png'):
        p = os.path.join(brain_dir, f)
        img = Image.open(p)
        # Let's inspect the text content or properties of the image
        # We can crop the top-left area to see if it's localhost or lottiefiles, etc.
        # Let's crop x in [0, 200], y in [0, 50] (typically contains page title or browser tab)
        tab_img = img.crop((40, 10, 250, 45))
        # Save it to scratch
        tab_img.save(f"C:\\Users\\metpa\\OneDrive\\Documents\\shraddha institute\\scratch\\tab_{f}")
        print(f"Saved tab_{f}")
