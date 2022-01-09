
from flask import Flask, render_template, session, copy_current_request_context, request
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock

from game import ComputerGame

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form.get("username", 'player')
    print(data)
    return render_template('index.html', async_mode=socket_.async_mode)

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)
@app.route("/play/<username>")
def play(username):
   return render_template('play.html', username=username)


@socket_.on('my_event', namespace='/test')
def test_message(message):
    print(message['data'])
    commads = ['scissors','rock', 'paper']
    if message['data'] in commads:
      print(message['data'])
      val = ComputerGame(message['data'])
      session['score'] = session.get('score', 0) + val[1]
      session['receive_count'] = session.get('receive_count', 0) + 1
      if session['score'] <= 9: 
        emit('my_response',
                {'data': val[0], 'count': session['receive_count'], 'score':session['score'], 'hand':val[2]})
      else:
          emit('my_response',
                {'data': 'You Win!'})
     

@socket_.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


if __name__ == '__main__':
    socket_.run(app, debug=True)