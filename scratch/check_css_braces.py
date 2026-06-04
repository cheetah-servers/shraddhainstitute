with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

brace_count = 0
in_comment = False
in_string = None
errors = []

lines = content.splitlines()
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        char = line[j]
        # Handle block comments
        if not in_comment and j + 1 < len(line) and line[j:j+2] == '/*':
            in_comment = True
            j += 2
            continue
        elif in_comment and j + 1 < len(line) and line[j:j+2] == '*/':
            in_comment = False
            j += 2
            continue
        elif in_comment:
            j += 1
            continue
            
        # Handle braces
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count < 0:
                errors.append(f"Unexpected closing brace '}}' at line {i+1}")
                brace_count = 0
        j += 1

if brace_count > 0:
    errors.append(f"Unclosed open brace(s) at end of file. Remaining: {brace_count}")

if errors:
    print("Found CSS brace mismatch errors:")
    for err in errors:
        print(" -", err)
else:
    print("CSS braces are balanced and valid!")
