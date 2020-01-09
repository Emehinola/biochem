from django.shortcuts import render
from . forms import ProfileForm
from . models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render, redirect
from . forms import RegisterForm
from . models import Tokens

# Create your views here.
@login_required
def index(request):
    return render(request, 'index/index.html')

def register(request):
    
    tokens = Tokens.objects.all()

    if "token" in request.POST:
        token = request.POST['token']
        form = RegisterForm(request.POST)
        if form.is_valid:
            for i in tokens:
                if i.token == token and not i.used:
                    form.save()
                    return redirect("profile_update")
                else:
                    pass
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile_update(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES or None)
        if profile_form.is_valid:
            check_form = profile_form.save(commit=False)
            check_form.user = request.user
            check_form.save()
            return redirect("profile")

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