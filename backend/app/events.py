import json

import flask
from tweepy import StreamListener

from app import tweet_fetcher, socketio


class WebSocketListener(StreamListener):
    def __init__(self):
        super().__init__()
        self.namespace = flask.request.namespace
        self.sid = flask.request.sid

    def on_data(self, raw_data):
        tweet = self._parse_tweet(raw_data)
        socketio.emit('tweet', tweet, namespace=self.namespace, room=self.sid)
        return True

    @staticmethod
    def _parse_tweet(raw_data):
        data = json.loads(raw_data)
        author = data['user']['name']
        text = data['text']
        return dict(author=author, text=text)


@socketio.on('subscribe', namespace='/tweet_streaming')
def on_subscribe(params):
    listener = WebSocketListener()
    socketio.start_background_task(tweet_fetcher.fetch_tweets, listener, **params)
