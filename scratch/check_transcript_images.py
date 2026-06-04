import json

transcript_path = r'C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        step = json.loads(line)
        if step.get('source') == 'USER_EXPLICIT' or step.get('type') == 'USER_INPUT':
            print(f"Step {step.get('step_index')}: {step.get('content')}")
            # print tool calls or files if any
            if 'tool_calls' in step:
                print(f"  Tool calls: {step['tool_calls']}")
