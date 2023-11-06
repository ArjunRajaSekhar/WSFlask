import json

#################################################################################
import socketio

# Create a Socket.IO client
sio = socketio.Client()


# Event handler for 'predicted_query_type' event
@sio.on('predicted_query_type')
def handle_predicted_query_type(data):
    print(f'Predicted Query Type: {data}')


# Connect to the Flask-SocketIO server
sio.connect('http://127.0.0.1:5000')

# Send a user query to the server
user_query = {"query": "what"}
sio.emit('user_query', json.dumps(user_query))

user_query = {"query": "which"}
sio.emit('user_query', json.dumps(user_query))
# Keep the client running
sio.wait()

