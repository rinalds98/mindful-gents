from django.urls import path, re_path
from chat.consumers import ChatRoomConsumer

# "" routes to the URL ChatConsumer which
# will handle the chat functionality
websocket_urlpatterns = [

    path("", ChatRoomConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatRoomConsumer.as_asgi()),
]

