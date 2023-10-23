from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(message):
    response = get_chatbot_response(message)
    emit("message", response)

def get_chatbot_response(message):
    # Your chatbot logic goes here
    return "Hello, I am a chatbot!"

if __name__ == "__main__":
    socketio.run(app)
