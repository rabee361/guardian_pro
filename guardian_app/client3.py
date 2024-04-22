from websocket import create_connection
import json

ws = create_connection("ws://85.31.237.33/ws/chat/1/")

info = {
    "message":"f u",
    "user_id":2,
    "chat_id":1
}
ws.send(json.dumps(info)) 
result = ws.recv()
print("Received '%s'" % result)
ws.close()