import json
import time

#################################################################################
import socketio

# Create a Socket.IO client
sio = socketio.Client()
# Event handler for 'predicted_query_type' event
@sio.on('connection_status')
def handle_predicted_query_type(data):
    print(f'Predicted Query Type: {json.loads(data)}')

@sio.on('response')
def handle_predicted(data):
    print(f'final emit: {json.loads(data)}')

# Connect to the Flask-SocketIO server
sio.connect('http://35.229.156.211',wait_timeout=15)

# Send a user query to the server
sio.emit('connect')
user_query = {"query": "which","matchedStrings":{}}
sio.emit('userQuery', json.dumps(user_query))
# Keep the client running
sio.wait()

