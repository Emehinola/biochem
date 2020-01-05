from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'profile_update', views.profile_update, name='profile_update'),
    url(r'^$', views.profile, name='profile')
]