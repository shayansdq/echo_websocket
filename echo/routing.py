from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/',consumers.EchoConsumer.as_asgi()),
    path('ws/image/',consumers.EchoImageConsumer.as_asgi())
]