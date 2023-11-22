from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpertiseForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def registration_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        expertise_form = ExpertiseForm(request.POST)

        if expertise_form.is_valid():
            is_expert = expertise_form.cleaned_data['isExpert']
            user_profile.isExpert = is_expert
            user_profile.save()
            return redirect('index')

    else:
        expertise_form = ExpertiseForm()

    context = {
        'expertise_form': expertise_form,
    }

    return render(request, 'registration.html', context)