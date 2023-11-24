from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages

@login_required
def user_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)

        if profile_form.is_valid():
            is_expert = profile_form.cleaned_data['isExpert']
            user_profile.isExpert = is_expert
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('index')

    else:
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'registration.html', context)