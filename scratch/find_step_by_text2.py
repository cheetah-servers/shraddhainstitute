import json

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            if d.get("type") == "USER_INPUT" and "do changes for befits section" in d.get("content", ""):
                print("Found match! Content length:", len(d.get("content", "")))
                with open("scratch/step_1220_content.txt", "w", encoding="utf-8") as out:
                    out.write(d.get("content", ""))
                break
        except Exception as e:
            pass
