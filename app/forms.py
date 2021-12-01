from django.db.models import fields

# Django's imports
from django import forms

# Developer's import
from .models import Content


# Form for entering data
class PostForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ["channel_name", "text", 'image', 'file']
