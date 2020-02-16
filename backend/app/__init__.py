from flask import Flask
from flask_socketio import SocketIO

from app.tweet_fetcher import TweetFetcher
from config import config

socketio = SocketIO(cors_allowed_origins='http://localhost:3000')
tweet_fetcher = TweetFetcher()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    socketio.init_app(app)
    tweet_fetcher.init_app(app)
    return app


from . import events
