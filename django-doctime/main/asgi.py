import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import videochat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "videocall.settings")

# application = get_asgi_application()
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            videochat.routing.websocket_urlpatterns
        )
    ),
})