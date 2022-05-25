from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=text_data)


class EchoImageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        return super().disconnect(close_code)

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data='Server: ' + text_data)
        elif bytes_data:
            self.send(bytes_data=bytes_data)
