from django.shortcuts import render
from . forms import ProfileForm
from . models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_update(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES or None)
        if profile_form.is_valid:
            check_form = profile_form.save(commit=False)
            check_form.user = request.user
            check_form.save()

    else:
        profile_form = ProfileForm()

    context = {
        'form': profile_form,
        'title':'Profile Update'
    }
    return render(request, 'users/profileupdate.html', context)

@login_required
def profile(request):
    prof = Profile.objects.get(user_id=request.user.id)
    context = {
        'title':'profile',
        'prof': prof
    }
    return render(request, 'users/profile.html', context)