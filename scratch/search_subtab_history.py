import json
import os

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            content = str(d)
            if "subtab-panel" in content:
                # check if there's any file content being modified or written
                tool_calls = d.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    # Look for html replacements
                    if "index.html" in (args.get("TargetFile") or ""):
                        rep = args.get("ReplacementContent") or ""
                        chunks = args.get("ReplacementChunks") or []
                        for chunk in chunks:
                            rep += chunk.get("ReplacementContent") or ""
                        if "subtab-panel" in rep:
                            print(f"Step {d.get('step_index')}, Tool: {tc.get('name')}")
                            # Let's write the rep to a text file for inspection
                            with open(f"scratch/step_{d.get('step_index')}_subtab.txt", "w", encoding="utf-8") as out:
                                out.write(rep)
                            print(f"  Wrote step {d.get('step_index')} HTML containing subtab-panel to scratch")
        except Exception as e:
            pass
