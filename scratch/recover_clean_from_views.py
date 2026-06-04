import json
import re

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

def recover_file(file_name, output_name):
    views = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get("step_index")
                
                # Ignore steps 1900 and later to avoid the corrupted JSON-escaped versions
                if step_idx >= 1900:
                    continue
                    
                if d.get("type") == "VIEW_FILE" and d.get("status") == "DONE":
                    content = d.get("content", "")
                    tc_args = d.get("tool_calls", [{}])[0].get("args", {})
                    path = tc_args.get("AbsolutePath") or ""
                    
                    # Also parse path from File Path header in content if AbsolutePath is not set
                    path_match = re.search(r'File Path:\s*`file:///([^`]+)`', content)
                    if path_match:
                        path = path_match.group(1).replace("%20", " ")
                        
                    if path and file_name in path.lower():
                        lines = content.split('\n')
                        parsed_segment = {}
                        for l in lines:
                            m = re.match(r'^(\d+):\s*(.*)$', l.strip())
                            if m:
                                line_num = int(m.group(1))
                                line_content = m.group(2)
                                parsed_segment[line_num] = line_content
                        if parsed_segment:
                            views.append((step_idx, parsed_segment))
            except Exception as e:
                pass

    if not views:
        print(f"No views found for {file_name}")
        return False

    # Sort views by step index so later views override earlier ones
    views.sort(key=lambda x: x[0])
    full_file = {}
    for step_idx, segment in views:
        for line_num, line_content in segment.items():
            # If the line content contains '<truncated', do NOT overwrite a good line with it
            if "<truncated" in line_content:
                continue
            full_file[line_num] = line_content

    if not full_file:
        print(f"No content resolved for {file_name}")
        return False

    max_line = max(full_file.keys())
    print(f"Reconstructed {file_name} up to line {max_line}. Total lines: {len(full_file)}")
    
    # Check for missing lines
    missing_count = 0
    for i in range(1, max_line + 1):
        if i not in full_file:
            missing_count += 1
    if missing_count > 0:
        print(f"  WARNING: {missing_count} missing lines in {file_name}!")
        
    with open(output_name, "w", encoding="utf-8") as out:
        for i in range(1, max_line + 1):
            out.write(full_file.get(i, f"/* MISSING LINE {i} */") + "\n")
    return True

recover_file("index.html", "index_recovered.html")
recover_file("style.css", "style_recovered.css")
recover_file("script.js", "script_recovered.js")
