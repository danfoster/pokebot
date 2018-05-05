#!/usr/bin/env python

from websocket import create_connection
import json

ws = create_connection("ws://localhost:8000/bot")

while True:
    m = ws.recv()
    d = json.loads(m)
    if d['action'] == "move":
        print("I would move {}".format(d['dir']))
    else:
        print("Unknown action: {}".format(d['action']))
