import json

message = {
    "from": "laptop",
    "key": 123
}
stringmessage = json.dumps(message)

rmessage = json.loads(stringmessage)

print(rmessage["from"])
