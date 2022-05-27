from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from echo import routing as echo_websocket_routing
from chat import routing as chat_routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # echo_websocket_routing.websocket_urlpatterns,
            chat_routing.websocket_urlpatterns
        )
    )
})
