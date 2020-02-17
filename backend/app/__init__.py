from flask import Flask
from flask_socketio import SocketIO

from app.tweet_fetcher import TweetFetcher
from config import config

# TODO: install eventlet or gevent and gevent-websocket and remove async_mode='threading'
# Eventlet doesn't support emmiting messages from a long-living background thread without monkey-patching.
# Monkey-patching can't be done at the moment, because it breaks tweepy.
# Similar issue described here:
# https://stackoverflow.com/questions/34581255/python-flask-socketio-send-message-from-thread-not-always-working
socketio = SocketIO(cors_allowed_origins='http://localhost:3000', async_mode='threading')
tweet_fetcher = TweetFetcher()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    socketio.init_app(app)
    tweet_fetcher.init_app(app)
    return app


from . import events
