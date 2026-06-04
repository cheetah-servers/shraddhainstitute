import subprocess

git_show = subprocess.run(["git", "show", "HEAD:index.html"], capture_output=True, text=True, encoding="utf-8")
if git_show.returncode != 0:
    print("Error running git show")
    exit(1)

content = git_show.stdout
lines = content.splitlines()

for i, line in enumerate(lines):
    if '<section' in line or 'SECTION' in line or 'id=' in line:
        if any(keyword in line.lower() for keyword in ['about', 'method', 'courses', 'path', 'journey', 'hero']):
            print(f"Line {i+1}: {line.strip()}")
