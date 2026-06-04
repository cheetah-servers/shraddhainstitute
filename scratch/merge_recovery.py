import json
import re

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

def merge_recover(file_name):
    # 1. Load clean Git version of the file
    with open(file_name, "r", encoding="utf-8") as f:
        clean_lines = f.readlines()
    
    # 2. Extract viewed lines from transcript
    views = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                step_idx = d.get("step_index")
                
                # Ignore steps 1900 and later to avoid corrupted JSON-escaped versions
                if step_idx >= 1900:
                    continue
                    
                if d.get("type") == "VIEW_FILE" and d.get("status") == "DONE":
                    content = d.get("content", "")
                    tc_args = d.get("tool_calls", [{}])[0].get("args", {})
                    path = tc_args.get("AbsolutePath") or ""
                    
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

    # Sort views by step index so later override earlier
    views.sort(key=lambda x: x[0])
    
    recovered_lines = {}
    for step_idx, segment in views:
        for line_num, line_content in segment.items():
            if "<truncated" in line_content:
                continue
            recovered_lines[line_num] = line_content

    # Merge clean_lines and recovered_lines
    max_line = max(len(clean_lines), max(recovered_lines.keys()) if recovered_lines else 0)
    merged_output = []
    
    for i in range(1, max_line + 1):
        if i in recovered_lines:
            merged_output.append(recovered_lines[i] + "\n")
        elif i <= len(clean_lines):
            merged_output.append(clean_lines[i-1])
        else:
            merged_output.append("\n")

    # Write merged result back to file
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(merged_output)
    
    print(f"Merged and recovered {file_name}: total {len(merged_output)} lines.")
    return True

merge_recover("index.html")
merge_recover("style.css")
merge_recover("script.js")
