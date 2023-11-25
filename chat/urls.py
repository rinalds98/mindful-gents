from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("room/<str:room_name>/", views.chat_room, name="chat"),
    path("", views.chat_page, name="index"),
    path("lobby/", views.chat_lobby, name="lobby"),
    path("leave_room/<str:room_name>", views.leave_room, name="leave_room"),
]
