import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "educa.settings")

django_asgi_app = get_asgi_application()

# import is below is needed to ensure the application
# registry is populated before importing code that may import ORM models.
from chat.routing import websocket_urlpatterns  # noqa

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)
