import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.group_name = f"chat_{self.username}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            username = text_data_json['receiver']
            user_group_name = f"chat_{username}"

            await self.channel_layer.group_send(
                user_group_name,
                {
                    'type': 'chat_message',
                    'message': text_data
                })

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=message)


class ChatConsumer2(AsyncConsumer):
    async def websocket_connect(self, event):
        self.user_id = self.scope['url_route']['kwargs']['username']
        self.group_name = f"chat_{self.user_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept',  # websocket_accept
        })

    async def websocket_disconnect(self, event):
        pass

    async def websocket_receive(self, event):
        pass
