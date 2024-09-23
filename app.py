from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

shahzod = 0


@app.route('/test', methods=['POST', 'GET'])
def hello_world():
    data = request.get_json()
    socketio.emit('new_data', data)
    if data and 'temperatura' in data and data['temperatura'] >= 30:
        print(shahzod)
        return jsonify({"status": 1, "switch": shahzod})
    else:
        print(shahzod)
        return jsonify({"status": 0, "switch": shahzod})


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('switch_state')
def handle_switch_state(data):
    global shahzod
    switch_state = data.get('switch')
    shahzod = switch_state
    print('Switch state received:', switch_state)


if __name__ == '__main__':
    socketio.run(app)
