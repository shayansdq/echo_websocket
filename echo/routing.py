from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/',consumers.echo_consumer.as_asgi())
]