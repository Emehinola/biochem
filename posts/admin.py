from django.contrib import admin
from . models import Announcement, Trending, TrendingComment, AnnouncementComment

# Register your models here.

admin.site.register(Announcement)
admin.site.register(Trending)
admin.site.register(TrendingComment)
admin.site.register(AnnouncementComment)
