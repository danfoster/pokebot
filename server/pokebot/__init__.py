#!/usr/bin/env python

from flask import Flask, render_template
from geventwebsocket.exceptions import WebSocketError
from flask_sockets import Sockets
import json


def create_app(env):
    app = Flask(__name__)
    sockets = Sockets(app)
    bots = []

    @sockets.route('/client')
    def client(ws):
        while True:
            message = ws.receive()
            print(message)
            for bot in bots:
                bot.send(message)

    @sockets.route('/bot')
    def bot(ws):
        print("Bot Connected")
        bots.append(ws)
        try:
            while not ws.closed:
                ws.receive()
        except ConnectionResetError:
            pass
        except WebSocketError:
            pass
        finally:
            bots.remove(ws)
            print("Bot Disconnected")

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
