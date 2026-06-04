from PIL import Image
import os
import hashlib

brain_dir = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0'
media_files = [
    'media__1780536406822.png',
    'media__1780537480117.png',
    'media__1780537611394.png',
    'media__1780537782288.png',
    'media__1780537925162.png',
    'media__1780538093603.png'
]

for f in media_files:
    p = os.path.join(brain_dir, f)
    if os.path.exists(p):
        h = hashlib.md5(open(p, 'rb').read()).hexdigest()
        print(f"{f}: md5={h}")
