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
        return self._is_still_subscribed()

    @staticmethod
    def _parse_tweet(raw_data):
        data = json.loads(raw_data)
        author = data['user']['name']
        text = data['text']
        return dict(author=author, text=text)

    def _is_still_subscribed(self):
        # Not a very clean way to find out, if the subscriber is still listening.
        # It's better to check via a callback function, but it leads to an error because there's no request available
        # at the moment when socketio.emit is called.
        rooms = socketio.server.manager.rooms
        return self.namespace in rooms and self.sid in rooms[self.namespace].keys()

    def on_error(self, status_code):
        print('tweepy streaming error. Status: %s' % status_code)


@socketio.on('subscribe', namespace='/tweet_streaming')
def on_subscribe(params):
    listener = WebSocketListener()
    socketio.start_background_task(tweet_fetcher.fetch_tweets, listener, **params)
