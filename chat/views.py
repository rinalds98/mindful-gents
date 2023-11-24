from django.shortcuts import render, redirect
from chat.models import OpenRoom
from django.contrib.auth.decorators import login_required


def chat_page(request):
    """Render chat access page"""
    return render(request, "chatpage.html")


def chat_room(request, room_name, *args, **kwargs):
    """Render chat room page"""
    anonym_name = None
    if not request.user.is_authenticated:
        anonym_name = room_name

    # create a new OpenRoom object
    current_room, created = OpenRoom.objects.get_or_create(
        chat_room_name=room_name, chat_room_url=request.path)

    context = {"anonym_name": anonym_name,
               "room_name": room_name,
               "current_room": current_room}
    return render(request, "chatroom.html", context)


@login_required
def chat_lobby(request):
    open_rooms = OpenRoom.objects.all()

    url_base = request.get_host()
    print("path:", url_base)

    context = {
        "open_rooms":  open_rooms,
    }
    return render(request, "chatlobby.html", context)


def leave_room(request, pk):
    room = OpenRoom.objects.get(id=pk)
    print(room)
    room.delete()
    return redirect('index')
