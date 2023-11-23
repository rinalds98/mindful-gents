# from django.contrib import admin
from django.urls import path
from chat.views import chat_room

app_name = "chat"
urlpatterns = [
    path("", chat_room, name="chat"),
]
