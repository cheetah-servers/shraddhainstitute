import json
import os

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

if not os.path.exists(log_path):
    print("Log path not found.")
    exit(1)

with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            d = json.loads(line)
            content = str(d)
            if "subtab" in content or "Daily Convers" in content or "school-sit" in content or "grammar-method" in content:
                print(f"Step {d.get('step_index')}, type={d.get('type')}, keys={list(d.keys())}")
                # check if there's any file content being modified or written
                tool_calls = d.get("tool_calls", [])
                for tc in tool_calls:
                    print(f"  Tool: {tc.get('name')}, args={list(tc.get('args', {}).keys())}")
                    if "ReplacementContent" in tc.get("args", {}):
                        rep = tc["args"]["ReplacementContent"]
                        if "subtab" in rep or "Daily" in rep:
                            print(f"    ReplacementContent size: {len(rep)}")
                            print(f"    ReplacementContent starts with: {rep[:100]}")
                    if "CodeContent" in tc.get("args", {}):
                        code = tc["args"]["CodeContent"]
                        if "subtab" in code or "Daily" in code:
                            print(f"    CodeContent size: {len(code)}")
                            print(f"    CodeContent starts with: {code[:100]}")
        except Exception as e:
            print(f"Error parsing line {i}: {e}")
