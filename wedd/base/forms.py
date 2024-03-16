from django import forms
from .models import Picture, Video
from . views import *


class PictureForm(forms.ModelForm):
    class Meta:
        models = Picture
        field = ['image']

class VideoForm(forms.ModelForm):
    class Meta:
        models = Video
        field = ['video']
        