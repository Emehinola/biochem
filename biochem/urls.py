"""biochem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from index import views as index_views
from posts import views as post_views
from users import views as users_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url('news/', include('posts.urls')),
    url(r'login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'announcement/(?P<id>\d+)$', post_views.announce, name='announce'),
    path('admin/', admin.site.urls),
    url(r'home/', index_views.home, name='home'),
    url(r'profile/', include('users.urls')),
    url('', include('index.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
