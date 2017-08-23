# Flask WebSocket uWSGI - Live Log File Follow

A toy test app.

Goal: live send the contents of a file on disk to connected web clients over WebSockets.

Uses Flask with Flask-SocketIO and runs through uWSGI for production deployment.

## Usage

```bash
./server.sh [start | stop | restart | reload] && tail -f uwsgi.log
```
