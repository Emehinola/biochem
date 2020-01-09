from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tokens(models.Model):
    token = models.CharField(max_length=6)
    used = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name_plural = 'Tokens'
        ordering = ['-time']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, upload_to="profile_pics")
    department = models.CharField(max_length=30)
    level = models.CharField(max_length=10) 
    matric_number = models.CharField(max_length=10)
    gender_choices = [
        ("male", "Male"),
        ("female", "Female")
    ]
    gender = models.CharField(max_length=6, choices=gender_choices)
    phone = models.CharField(max_length=14)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ['-time']

    def __str__(self):
        return self.matric_number