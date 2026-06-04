import json

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            step_index = d.get("step_index")
            source = d.get("source")
            content = d.get("content", "")
            
            # Print only user inputs
            if d.get("type") == "USER_INPUT":
                print(f"Step {step_index} User: {content}")
        except Exception as e:
            pass
