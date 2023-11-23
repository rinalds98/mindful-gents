from django.shortcuts import render


def chat_page(request):
    """"""
    return render(request, "chatpage.html")


def chat_room(request, room_name, *args, **kwargs):
    
    anonym_name = None
    if not request.user.is_authenticated:        
        anonym_name = room_name

    context = {"anonym_name": anonym_name,
               "room_name": room_name}
    
    return render(request, "chatroom.html", context)

def get_open_rooms():
    pass
    