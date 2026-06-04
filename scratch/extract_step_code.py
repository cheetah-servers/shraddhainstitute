import json
import os

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            step = d.get('step_index')
            if 2800 <= step <= 3100:
                tool_calls = d.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    target = args.get("TargetFile") or args.get("Target") or ""
                    if "index.html" in target:
                        print(f"Step {step}, Tool: {tc.get('name')}")
                        if "ReplacementContent" in args:
                            print(f"  Rep size: {len(args['ReplacementContent'])}")
                            # print first 200 chars and last 200 chars
                            print(f"  Start: {args['ReplacementContent'][:200]}")
                            print(f"  End: {args['ReplacementContent'][-200:]}")
                        if "CodeContent" in args:
                            print(f"  Code size: {len(args['CodeContent'])}")
                            print(f"  Start: {args['CodeContent'][:200]}")
                            print(f"  End: {args['CodeContent'][-200:]}")
        except Exception:
            pass
