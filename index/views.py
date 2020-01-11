from django.shortcuts import render
from posts.models import Announcement, Trending
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request, 'index/index.html')

@login_required
def home(request):
    blogs = Trending.objects.all()[:3]
    announces = Announcement.objects.all()[:200]
    context = {
        'title': 'Home',
        'blogs': blogs,
        'announces': announces
    }
    return render(request, 'index/home.html', context)

def login(request):
    return render(request, 'index/login.html')