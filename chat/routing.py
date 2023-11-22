from django.urls import path, include
from chat.consumers import ChatRoomConsumer

# "" routes to the URL ChatConsumer which
# will handle the chat functionality
websocket_urlpatterns = [
    path("", ChatRoomConsumer.as_asgi()),
]
