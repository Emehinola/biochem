from django.shortcuts import render
from posts.models import Announcement, Trending

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def home(request):
    blogs = Trending.objects.all()[:3]
    announces = Announcement.objects.all()
    context = {
        'title': 'Home',
        'blogs': blogs,
        'announces': announces
    }
    return render(request, 'index/home.html', context)

def login(request):
    return render(request, 'index/login.html')