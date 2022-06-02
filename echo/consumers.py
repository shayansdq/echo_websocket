from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class EchoConsumer(WebsocketConsumer):

    def connect(self):
        self.room_id = 'echo_1'

        async_to_sync(self.channel_layer.group_add)(
            self.room_id,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_id,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + ' - Sent by server')

    def echo_message(self, event):
        message = event.get('message')
        self.send(text_data=message)


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
