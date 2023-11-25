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
    
    if not get_referer(request):
        raise Http404
    else: 
        anonym_name = None
        if not request.user.is_authenticated:
            anonym_name = room_name[:-4]
        

    context = {
        "anonym_name": anonym_name,
        "room_name": room_name,
        # "current_room": current_room,
        }

    return render(request, "chatroom.html", context)


@login_required
def chat_lobby(request):
    open_rooms = OpenRoom.objects.all()

    context = {
        "open_rooms":  open_rooms,    
    }
    
    return render(request, "chatlobby.html", context)


def leave_room(request, room_name):
    try:
        room = OpenRoom.objects.get(chat_room_name=room_name.replace(" ", ""))
        room.delete()
    except Exception as e:
        print(type(e), e)

    if not request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect("../lobby")
