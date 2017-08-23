from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="./")
application = app # so uWSGI can find the app

# gevent_uwsgi is not available when not running under uWSGI
socketio = SocketIO(app, async_mode="gevent_uwsgi", allow_upgrades=True)
#socketio = SocketIO(app, allow_upgrades=True)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('get_logs', namespace='/logs')
def get_logs():
    socketio.emit("log", "A")
    for line in follow_file('./test.log'):
        print("for line")
        print(line)
        socketio.emit("log", line)
    socketio.emit("log", "B")
    socketio.send("C")

'''
Follow the live contents of a text file.
https://code.activestate.com/recipes/578424-tailing-a-live-log-file-with-python/
'''
def follow_file(filename):
    stream = open(filename, 'r')
    line = ''
    for block in iter(lambda:stream.read(1024), None):
        print("follow_file - for")
        if '\n' in block:
            print("follow_file - newline")
            # Only enter this block if we have at least one line to yield.
            # The +[''] part is to catch the corner case of when a block
            # ends in a newline, in which case it would repeat a line.
            for line in (line+block).splitlines(True)+['']:
                if line.endswith('\n'):
                    yield line
            # When exiting the for loop, 'line' has any remaninig text.
        elif not block:
            # Wait for data.
            print("follow_file - blocking/sleep")
            socketio.sleep(1)

if __name__ == "__main__":
    socketio.run(app, port=3000, debug=True)
