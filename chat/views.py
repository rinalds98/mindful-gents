from django.shortcuts import render, redirect, Http404
from chat.models import OpenRoom
from django.contrib.auth.decorators import login_required
from random import randint


def chat_page(request):
    """Render chat access page"""
    return render(request, "chatpage.html")


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def chat_room(request, room_name):
    """Render chat room page"""

    anonym_name = None
    if not request.user.is_authenticated:
        anonym_name = room_name

    # create a new OpenRoom object
    
    rooms = [room.chat_room_name for room in OpenRoom.objects.all()]

    suffix = "".join([str(randint(0,9)) for x in range(4)])
    display_name = f"{room_name}_{suffix}"
    current_room = OpenRoom.objects.create(
            chat_room_name=display_name, chat_room_url=request.path)
        

    context = {
        "anonym_name": anonym_name,
        "room_name": room_name,
        "current_room": current_room,
        }

    return render(request, "chatroom.html", context)


@login_required
def chat_lobby(request):
    open_rooms = OpenRoom.objects.all()

    context = {
        "open_rooms":  open_rooms,    
    }
    
    return render(request, "chatlobby.html", context)


def leave_room(request, pk):
    room = OpenRoom.objects.get(id=pk)

    room.delete()
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect("../lobby")
