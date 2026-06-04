import subprocess

git_show = subprocess.run(["git", "show", "fb38541:index.html"], capture_output=True, text=True, encoding="utf-8")
if git_show.returncode != 0:
    print("Error")
    exit(1)

content = git_show.stdout
lines = content.splitlines()
print(f"Total lines in fb38541:index.html: {len(lines)}")
for i, line in enumerate(lines):
    if '<section' in line:
        print(f"Line {i+1}: {line.strip()}")
