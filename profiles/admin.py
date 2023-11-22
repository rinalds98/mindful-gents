from django.contrib import admin
from .models import UserProfile


list_display = ('user', 'isExpert')
admin.site.register(UserProfile)