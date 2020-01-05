from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'details/(?P<id>\d+)$', views.details, name='details'),
    url(r'post_update/', views.update, name='update'),
    url(r'post_announce/', views.announceupdate, name='announceupdate'),
    url(r'^$', views.news, name='news')
]