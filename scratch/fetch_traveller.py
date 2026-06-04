import urllib.request
import re
import os

scratch_dir = r'C:\Users\metpa\OneDrive\Documents\shraddha institute\scratch'
os.makedirs(scratch_dir, exist_ok=True)

candidate_urls = [
    'https://storyset.com/illustration/traveling/rafiki',
    'https://storyset.com/illustration/travel/rafiki',
    'https://storyset.com/illustration/trip/rafiki',
    'https://storyset.com/illustration/tourist/rafiki',
    'https://storyset.com/illustration/journey/rafiki',
]

found = False
for url in candidate_urls:
    try:
        print(f"Trying url: {url}")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        matches = re.findall(r'https://stories\.freepiklabs\.com/storage/[^\s"\'\(\)]+\.svg', html)
        if matches:
            svg_url = matches[0]
            print(f"Found SVG URL for traveller: {svg_url}")
            
            # Download the SVG
            svg_content = urllib.request.urlopen(urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})).read()
            svg_path = os.path.join(scratch_dir, "traveller.svg")
            with open(svg_path, 'wb') as f:
                f.write(svg_content)
            print(f"Downloaded to {svg_path}")
            found = True
            break
    except Exception as e:
        print(f"Failed {url}: {e}")

if not found:
    print("Could not find any traveller illustration")
