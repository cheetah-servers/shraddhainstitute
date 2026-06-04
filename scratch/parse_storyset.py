import re

content = open(r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0\.system_generated\steps\82\content.md', encoding='utf-8').read()
urls = re.findall(r'https?://[^\s"\'\(\)]+', content)
print("Found URLs:")
for u in urls:
    if 'svg' in u or 'png' in u or 'images' in u or 'rafiki' in u or 'freepik' in u:
        print(u)
