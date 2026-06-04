import json

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

steps_to_extract = [1682, 1688, 1695]

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            step_idx = d.get("step_index")
            if step_idx in steps_to_extract:
                tool_calls = d.get("tool_calls", [])
                for tc in tool_calls:
                    name = tc.get("name")
                    args = tc.get("args", {})
                    out_name = f"scratch/step_{step_idx}_{name}.txt"
                    # We write the replacement content or target content
                    content = args.get("ReplacementContent") or ""
                    with open(out_name, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"Extracted step {step_idx} {name} to {out_name} (len: {len(content)})")
        except Exception as e:
            pass
