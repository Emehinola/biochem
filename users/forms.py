from django.db import models
from django.contrib.auth.models import User
from django import forms
from . models import Profile
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class RegisterForm(UserCreationForm):
    token = forms.CharField(max_length=6, label="Your token here")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'token']
        help_texts = { 
            'username':None, 
            'email': None
        }

class ProfileForm(forms.ModelForm):
    department = forms.CharField(max_length=30)
    level = forms.CharField(max_length=10)
    matric_number = forms.CharField(max_length=10)
    gender_choices = [
        ("male", "Male"),
        ("female", "Female")
    ]
    gender = forms.ChoiceField(choices=gender_choices)
    phone = forms.CharField(max_length=14)

    class Meta:
        model = Profile
        fields = ['department', 'level', 'matric_number', 'gender', 'phone']