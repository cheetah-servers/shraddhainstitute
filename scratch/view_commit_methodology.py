import subprocess

commits = ["c142dff", "53612b2", "fb38541"]

for commit in commits:
    print(f"\n================= COMMIT: {commit} =================")
    git_show = subprocess.run(["git", "show", f"{commit}:index.html"], capture_output=True, text=True, encoding="utf-8")
    if git_show.returncode != 0:
        print(f"Could not show commit {commit}")
        continue
    content = git_show.stdout
    lines = content.splitlines()
    found = False
    for i, line in enumerate(lines):
        if 'id="methodology"' in line or 'id="about"' in line or 'methodology' in line.lower() or 'our method' in line.lower():
            print(f"Line {i+1}: {line.strip()}")
            found = True
    if not found:
        print("No methodology markers found in this commit.")
