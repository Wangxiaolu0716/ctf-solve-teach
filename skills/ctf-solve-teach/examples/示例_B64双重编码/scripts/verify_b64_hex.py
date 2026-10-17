import base64, sys
raw = open(sys.argv[1], encoding="utf-8").read().strip()
print(bytes.fromhex(base64.b64decode(raw).decode()).decode())
