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


# @socketio.on('connect')
# def handle_connect():
#     print('Client connected to the server')
#     # data = {"predicted": "what"}
#     # emit("predicted_query_type",json.dumps(data))
#
#     # Create a new QueryProcessor instance for each connection
#     query_processor = QueryProcessor()
#
#     # Store the QueryProcessor instance in the current request context
#     request.query_processor = query_processor


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

    # Uncomment and implement the other parts of your logic as needed
    # recommended_questions = query_processor.generate_recommended_questions(predicted_query_type)
    # minimum_elements = query_processor.find_minimum_elements(predicted_query_type)

    # Emit the results back to the client
    emit('predicted_query_type', json.dumps(predicted_query_type))
    # emit('recommended_questions', recommended_questions)
    # emit('minimum_elements', minimum_elements)


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=5000)
