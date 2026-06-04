import urllib.request
import re
import os

scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'
os.makedirs(scratch_dir, exist_ok=True)

urls = {
    'business': 'https://storyset.com/illustration/business-deal/rafiki',
    'professional': 'https://storyset.com/illustration/teacher/rafiki',
    'traveller': 'https://storyset.com/illustration/travel-plans/rafiki'
}

for name, url in urls.items():
    try:
        print(f"Fetching {name} from {url}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Search for freepiklabs storage svg link
        matches = re.findall(r'https://stories\.freepiklabs\.com/storage/[^\s"\'\(\)]+\.svg', html)
        if matches:
            svg_url = matches[0]
            print(f"Found SVG URL for {name}: {svg_url}")
            
            # Download the SVG
            svg_content = urllib.request.urlopen(urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})).read()
            svg_path = os.path.join(scratch_dir, f"{name}.svg")
            with open(svg_path, 'wb') as f:
                f.write(svg_content)
            print(f"Downloaded to {svg_path}")
        else:
            print(f"No SVG matches found for {name}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")
