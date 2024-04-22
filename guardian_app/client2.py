from websocket import create_connection
import json
import threading

# WebSocket server URL
server_url = "ws://85.31.237.33/ws/chat/1/"

# Function to send a message
def send_message(ws, message, user_id, chat_id):
    info = {
        "message": message,
        "user_id": user_id,
        "chat_id": chat_id
    }
    ws.send(json.dumps(info))

# Function to receive a message
def receive_message(ws):
    result = ws.recv()
    print("Received '%s'" % result)
    return result

# Function to handle the conversation loop
def conversation_loop(ws, user_id, chat_id):
    while True:
        try:
            # Send a message
            message = input("Enter your message: ")
            send_message(ws, message, user_id, chat_id)
            
            # Wait for a response
            response = receive_message(ws)
            print("Response: ", response)
            
            # Check if the response indicates the end of the conversation
            if response == 'END_CONVERSATION':
                break
        except Exception as e:
            print("Error occurred:", e)
            break

# Main function to start the conversation
def main():
    # Connect to the WebSocket server
    ws = create_connection(server_url)
    
    # Start the conversation loop in a separate thread
    conversation_thread = threading.Thread(target=conversation_loop, args=(ws,  1,  1))
    conversation_thread.start()
    
    # Wait for the conversation thread to finish
    conversation_thread.join()
    
    # Close the WebSocket connection
    ws.close()

if __name__ == "__main__":
    main()
