from django import forms

class ExpertiseForm(forms.Form):
    EXPERT_CHOICES = [
        (True, 'Yes, I am an expert'),
        (False, 'No, I am not an expert'),
    ]

    isExpert = forms.ChoiceField(
        choices=EXPERT_CHOICES,
        widget=forms.RadioSelect,
        label='Are you an expert?'
    )