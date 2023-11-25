from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['isExpert', 'expertinfo', 'description']
        labels = {
            'isExpert': 'Please confirm you are an expert/professional?',
            'expertinfo': 'What qualifies you as an expert/professional?',
            'description': 'Please describe any other relevant experience you have and list any qualifications:',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
