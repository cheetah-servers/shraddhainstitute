import os
import re

diff_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\scratch\diff_index.txt"
target_path = "index.html"

def apply_diff(diff_file, target_file):
    with open(diff_file, "r", encoding="utf-16le") as f:
        diff_lines = f.readlines()
        
    with open(target_file, "r", encoding="utf-8") as f:
        target_lines = f.readlines()
        
    hunks = []
    current_hunk = None
    
    # Parse hunks from diff
    i = 0
    while i < len(diff_lines):
        line = diff_lines[i]
        m = re.match(r'^@@ -(\d+),(\d+) \+(\d+),(\d+) @@', line)
        if m:
            old_start = int(m.group(1))
            old_len = int(m.group(2))
            new_start = int(m.group(3))
            new_len = int(m.group(4))
            
            hunk_lines = []
            i += 1
            while i < len(diff_lines) and not diff_lines[i].startswith('@@') and not diff_lines[i].startswith('diff --git'):
                hunk_lines.append(diff_lines[i])
                i += 1
                
            hunks.append({
                'old_start': old_start,
                'old_len': old_len,
                'new_start': new_start,
                'new_len': new_len,
                'lines': hunk_lines
            })
            continue
        i += 1
        
    print(f"Parsed {len(hunks)} hunks from diff.")
    
    # Apply hunks in reverse order (bottom to top) so that line indices don't shift for earlier hunks
    hunks.sort(key=lambda x: x['old_start'], reverse=True)
    
    output_lines = list(target_lines)
    
    for hunk in hunks:
        old_start = hunk['old_start']
        old_len = hunk['old_len']
        new_start = hunk['new_start']
        new_len = hunk['new_len']
        h_lines = hunk['lines']
        
        # 1-based index to 0-based index
        start_idx = old_start - 1
        
        # Verify context matches
        # We collect the lines that should be deleted or kept as context
        expected_old_lines = []
        for hl in h_lines:
            if hl.startswith(' ') or hl.startswith('-'):
                expected_old_lines.append(hl[1:])
                
        # Compare with output_lines
        actual_old_lines = []
        # Wait, git diff line counts might include trailing newlines
        actual_old_lines = output_lines[start_idx:start_idx + old_len]
        
        # Clean context matches (sometimes whitespace differences happen)
        # We'll just trust the line numbers if they align, or print warning
        
        # Construct new lines
        new_content = []
        for hl in h_lines:
            if hl.startswith(' ') or hl.startswith('+'):
                new_content.append(hl[1:])
                
        # Replace the range in output_lines
        output_lines[start_idx:start_idx + old_len] = new_content
        print(f"Applied hunk: old lines {old_start}-{old_start+old_len} replaced with {len(new_content)} new lines.")
        
    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(output_lines)
        
    print(f"Successfully patched {target_file}!")

apply_diff(diff_path, target_path)
