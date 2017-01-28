import socket
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'data-md'	
socketio = SocketIO(app)

@app.route('/<key>')
def index(key):
	return render_template('index.html', key=key)

@socketio.on_error()
def error_handler(e):
    print 'Error: '+e

@socketio.on('message')
def handle_message(message):
	print message

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=int(5000))