from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from . models import Announcement, Trending, AnnouncementComment, TrendingComment
from . forms import AnnouncementCommentForm, TrendingCommentForm, TrendingForm, AnnouncementForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def news(request):
    blog = Trending.objects.all()
    context = {
        'title': 'Blog',
        'blogs': blog
    }
    return render(request, 'posts/news.html', context)

def details(request, id):
    blog = Trending.objects.get(id=id)
    comments = TrendingComment.objects.all()

    if request.method == "POST":
        comment_form = TrendingCommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.trend_id = id
            comment.author = request.user
            comment.save()
            return redirect(f"news/details/{id}")

    else:
        comment_form = TrendingCommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'commentform': comment_form
    }
    return render(request, 'posts/details.html', context)

def announce(request, id):
    announcements = Announcement.objects.get(id=id)
    comments = AnnouncementComment.objects.all()

    if request.method == "POST":
        comment_form = AnnouncementCommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.announce_id = id
            comment.author = request.user
            comment.save()

    else:
        comment_form = AnnouncementCommentForm()

    
    context = {
        'announcements': announcements,
        'comments': comments,
        'commentform': comment_form
    }
    return render(request, 'posts/announce.html', context)

def update(request):
    #instance = get_object_or_404(Trending, id=id)
    form = TrendingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect("news.html")

    context = {
        'title': 'post news',
        'form': form
    }
    return render(request, "posts/update.html", context)

def announceupdate(request):
    #instance = get_object_or_404(Trending, id=id)
    form = AnnouncementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect("home.html")

    context = {
        'title': 'post announcement',
        'form': form
    }
    return render(request, "posts/announceupdate.html", context)