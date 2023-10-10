from channels.routing import ProtocolTypeRouter, URLRouter
import log.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        log.routing.websocket_urlpatterns
    ),
})
