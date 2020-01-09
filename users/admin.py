from django.contrib import admin
from . models import Profile, Tokens

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tokens)