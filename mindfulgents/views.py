from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def crisis(request):
    return render(request, 'crisis.html')

def information(request):
    return render(request, 'information-hub.html')

# custom 404 view
def error_404(request, exception):
    return render(request, 'error404.html', status=404)

