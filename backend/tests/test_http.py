import unittest
from flask import current_app
from app import create_app


class HttpTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def assertReturns404(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_root_404(self):
        self.assertReturns404('/')

    def test_stream_tweets_404(self):
        self.assertReturns404('/stream_tweets/')

    def test_wrong_url_404(self):
        self.assertReturns404('/wrong/url/')
