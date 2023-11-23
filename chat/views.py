from django.shortcuts import render, redirect


def chat_room(request, *args, **kwargs):
    if not request.user.is_authenticated:
        # return redirect("login")
        return redirect("index.html")
    context = {}
    return render(request, "chatroom.html", context)
