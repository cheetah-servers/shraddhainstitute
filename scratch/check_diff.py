import subprocess

git_diff = subprocess.run(["git", "diff", "index.html"], capture_output=True, text=True, encoding="utf-8")
diff_lines = git_diff.stdout.splitlines()

# Print lines of the diff that mention methodology
for line in diff_lines:
    if 'methodology' in line.lower() or 'showcase' in line.lower() or 'portal' in line.lower():
        print(line)
