from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from echo import routing as echo_websocket_routing
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            echo_websocket_routing.websocket_urlpatterns
        )
    )
})