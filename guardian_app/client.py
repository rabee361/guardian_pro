from websocket import create_connection
import json

ws = create_connection("ws://127.0.0.1:8000/ws/chat/1/13")

info = {
    "message":"hey dude",
    # "user_id":2,
    # "chat_id":1
}
ws.send(json.dumps(info)) 
result = ws.recv()
print("Received '%s'" % result)
ws.close()