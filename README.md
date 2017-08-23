# Flask WebSocket uWSGI - Live Log File Follow

A toy test app.

Goal: live send the contents of a file on disk to connected web clients over WebSockets.

Uses Flask with Flask-SocketIO and runs through uWSGI for production deployment.

## Usage

First modify `chdir` in uwsgi.ini to point to the dir you have this project in.

```bash
./server.sh [start | stop | restart | reload] && tail -f uwsgi.log
```
