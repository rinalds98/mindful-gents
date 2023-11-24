from django.db import models

# Create your models here.
class OpenRoom(models.Model):
    chat_room_name = models.CharField(max_length=50)
    chat_room_url = models.CharField(max_length=200)
    