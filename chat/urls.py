# from django.contrib import admin
from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("room/<str:room_name>/", views.chat_room, name="chat"),
    path("", views.chat_page, name="index"),
]
