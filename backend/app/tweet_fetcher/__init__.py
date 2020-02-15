from tweepy import OAuthHandler, Stream


class TweetFetcher(object):
    def __init__(self):
        self.stream_factory = None

    def fetch_tweets(self, listener, **kwargs):
        if not self.stream_factory:
            raise AttributeError('Tweet fetcher not initialized')
        stream = self.stream_factory.create_stream(listener)
        stream.filter(**kwargs)

    def init_app(self, app):
        if app.config['TESTING']:
            from app.tweet_fetcher.test_utils import TestStreamFactory
            self.stream_factory = TestStreamFactory()
        else:
            self.stream_factory = StreamFactory(app.config)


class StreamFactory(object):
    def __init__(self, app_config):
        twitter_api_config_keys = {'CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET'}
        self.twitter_api_config = {k: v for k, v in app_config.items() if k in twitter_api_config_keys}
        absent_keys = twitter_api_config_keys - {key for key in self.twitter_api_config if self.twitter_api_config[key]}
        if absent_keys:
            raise RuntimeError("%s must be set" % absent_keys)

    def create_stream(self, listener):
        auth = OAuthHandler(self.twitter_api_config['CONSUMER_KEY'], self.twitter_api_config['CONSUMER_SECRET'])
        auth.set_access_token(self.twitter_api_config['ACCESS_TOKEN'], self.twitter_api_config['ACCESS_TOKEN_SECRET'])

        return Stream(auth, listener)
