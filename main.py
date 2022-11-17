import time
from flask_socketio import SocketIO, send
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = 'lox'
socket = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socket.on('message')
def handleNumber(num):
    while True:
        time.sleep(1)
        num += 1
        print("Number:" + str(num))
        send(num, broadcast=True)


if __name__ == "__main__":
    socket.run(app)
