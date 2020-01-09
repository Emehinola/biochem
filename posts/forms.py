from django import forms
from . models import AnnouncementComment, TrendingComment
from . models import Announcement, Trending

class TrendingCommentForm(forms.ModelForm):
    body = forms.Textarea()

    class Meta:

        model = TrendingComment
        fields = ['body']

class AnnouncementCommentForm(forms.ModelForm):
    body = forms.Textarea()

    class Meta:

        model = AnnouncementComment
        fields = ['body']

class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    image = forms.FileField()
    body = forms.Textarea()
    level = forms.CharField(max_length=10)
    category_choices = [
        ('Assignment', 'Assignment'),
        ('Suggestion', 'Suggestion')
    ]
    category = forms.ChoiceField(choices=category_choices)

    class Meta:
        fields = ['title', 'image', 'body', 'level', 'category']
        model = Announcement

class TrendingForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    image = forms.FileField()
    body = forms.Textarea()
    category_choices = [
        ('School news', 'School news'),
        ('General news', 'General news')
    ]
    category = forms.ChoiceField(choices=category_choices)

    class Meta:
        fields = ['title', 'image', 'body', 'category']
        model = Trending