import json

with open("index_recovered.html", "r", encoding="utf-8") as f:
    raw = f.read()

print(f"Length of raw: {len(raw)}")
print(f"Starts with: {raw[:100]}")

# Let's try loading it as JSON if it's a string, or unescaping
try:
    decoded = json.loads(raw)
    print(f"Decoded as JSON. Length: {len(decoded)}")
    print(f"Decoded starts with: {decoded[:100]}")
    with open("index_recovered_decoded.html", "w", encoding="utf-8") as f2:
        f2.write(decoded)
    print("Decoded written to index_recovered_decoded.html")
except Exception as e:
    print(f"Could not load as JSON: {e}")
