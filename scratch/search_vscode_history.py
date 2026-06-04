import os
import glob
import json

appdata = os.environ.get("APPDATA")
vscode_history = os.path.join(appdata, "Code", "User", "History")

print("VS Code History Path:", vscode_history)
if os.path.exists(vscode_history):
    entries_files = glob.glob(os.path.join(vscode_history, "**", "entries.json"), recursive=True)
    print(f"Found {len(entries_files)} history entries files.")
    
    found_matches = []
    for ef in entries_files:
        try:
            with open(ef, "r", encoding="utf-8") as f:
                d = json.load(f)
                resource = d.get("resource", "")
                print(f"Resource in history: {resource}")
                if "shraddha" in resource.lower():
                    print(f"  MATCH FOUND: {resource} in {os.path.dirname(ef)}")
                    for entry in d.get("entries", []):
                        id_val = entry.get("id")
                        updated_at = entry.get("updatedAt")
                        file_path = os.path.join(os.path.dirname(ef), id_val)
                        if os.path.exists(file_path):
                            size = os.path.getsize(file_path)
                            found_matches.append((updated_at, file_path, resource))
        except Exception as e:
            pass
            
    found_matches.sort(key=lambda x: x[0], reverse=True)
    if found_matches:
        print("\nLatest history files:")
        for idx, (updated_at, path, res) in enumerate(found_matches[:15]):
            print(f"{idx}: {updated_at} - {path} - {res}")
else:
    print("VS Code history path does not exist.")
