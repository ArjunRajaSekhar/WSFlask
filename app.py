import json

from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


class QueryProcessor:
    def __init__(self):
        pass

    def predict_query_type(self, user_query):
        # Implement the logic to predict the query type here
        return "query returned " + str(user_query)

    # Uncomment and implement the other methods as needed
    # def generate_recommended_questions(self, query_type):
    #     # Implement the logic to generate recommended questions here
    #     pass
    #
    # def find_minimum_elements(self, query_type):
    #     # Implement the logic to find minimum elements here
    #     pass


@app.route('/')
def index():
    print("test logging")
    return "<h1>Test App</h1>"


@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')


@socketio.on('user_query')
def handle_user_query(data):
    inputDict = json.loads(data)
    user_query = inputDict["query"]
    query_processor = QueryProcessor()
    # Retrieve the QueryProcessor instance from the request context
    if query_processor is None:
        return  # Handle the case where the instance is not found

    # Continue with processing the user query using the query_processor instance
    predicted_query_type = query_processor.predict_query_type(user_query)

    # Emit the results back to the client
    emit('predicted_query_type', json.dumps(predicted_query_type))


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=5000)
