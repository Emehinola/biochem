from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(default="download.png", upload_to="posts_pics")
    body = models.TextField()
    category_choices = [
        ('Assignment', 'Assignment'),
        ('Suggestion', 'Suggestion')
    ]
    category = models.CharField(max_length=50, choices=category_choices)
    level = models.CharField(max_length=10, default="")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Announcements"
        ordering = ['-time']

class Trending(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(default="download.png", upload_to="posts pics")
    body = models.TextField()
    category_choices = [
        ('School news', 'School news'),
        ('General news', 'General news')
    ]
    category = models.CharField(max_length=50, choices=category_choices)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Trending"
        ordering = ['-time']


class TrendingComment(models.Model):
    trend = models.ForeignKey("Trending", on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = "News Comment"


class AnnouncementComment(models.Model):
    announce = models.ForeignKey("Announcement", on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    class Meta:
        verbose_name_plural = "Announcement Comment"

