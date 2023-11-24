from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'isExpert', 'expertinfo', 'description')

admin.site.register(UserProfile, UserProfileAdmin)