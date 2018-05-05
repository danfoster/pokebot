#!/usr/bin/env python

from flask import Flask, render_template
from flask_sockets import Sockets


def create_app(env):
    app = Flask(__name__)
    sockets = Sockets(app)

    @sockets.route('/client')
    def echo_sockets(ws):
        while True:
            message = ws.receive()
            ws.send(message)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
