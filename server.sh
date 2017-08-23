#!/bin/bash
if [ "$1" == "start" ]; then
    /usr/local/bin/uwsgi --ini /home/vlad/Code/ws-test/uwsgi.ini --enable-threads &
elif [ "$1" == "reload" ]; then
    /usr/local/bin/uwsgi --reload /home/vlad/Code/ws-test/uwsgi.pid &
elif [ "$1" == "restart" ]; then
    kill $(cat /home/vlad/Code/ws-test/uwsgi.pid) && \
    sleep 3 && \
    /usr/local/bin/uwsgi --ini /home/vlad/Code/ws-test/uwsgi.ini --enable-threads &
elif [ "$1" == "stop" ]; then
    kill $(cat /home/vlad/Code/ws-test/uwsgi.pid) && sleep 3
else
    echo "Usage: $0 [start | stop | restart | reload]" >&2
    exit 1
fi
