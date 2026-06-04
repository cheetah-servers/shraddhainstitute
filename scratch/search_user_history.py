import json

log_path = r"C:\Users\metpa\.gemini\antigravity-ide\brain\44788ed5-af25-49f9-9b08-07b6d6182e86\.system_generated\logs\transcript.jsonl"

user_messages = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
            if d.get("type") == "USER_INPUT":
                user_messages.append((d.get("step_index"), d.get("content")))
        except Exception as e:
            pass

print(f"Total user messages found: {len(user_messages)}")
for step_idx, content in user_messages:
    # Print only up to 200 chars to avoid massive output, but show the main text
    short_content = content.strip().replace('\n', ' ')
    if len(short_content) > 120:
        short_content = short_content[:120] + "..."
    print(f"Step {step_idx}: {short_content}")
