import json
import re

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

def extract_step(step_num, out_name):
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                d = json.loads(line)
                if d.get("step_index") == step_num and d.get("type") == "USER_INPUT":
                    content = d.get("content", "")
                    with open(out_name, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"Extracted step {step_num} to {out_name} (len: {len(content)})")
                    return True
            except Exception as e:
                pass
    return False

extract_step(310, "scratch/step_310.txt")
extract_step(818, "scratch/step_818.txt")
