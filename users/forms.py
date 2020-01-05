from django.db import models
from django.contrib.auth.models import User
from django import forms
from . models import Profile

# Create your models here.

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