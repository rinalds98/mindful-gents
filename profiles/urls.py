from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
]


urlpatterns = [
    path('information/', views.registration_view, name='information-hub.html'),
]