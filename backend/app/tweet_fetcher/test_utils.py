class TestStreamFactory:
    @staticmethod
    def create_stream(listener):
        return TestStream(listener)


class TestStream:
    def __init__(self, listener):
        self.listener = listener

    def filter(self, data='test'):
        self.listener.on_data(data)
