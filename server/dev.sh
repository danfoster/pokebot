#!/bin/sh
gunicorn -k flask_sockets.worker wsgi:app
