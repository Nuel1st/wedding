from django.shortcuts import render, redirect
from django.forms import *
from django.views import *
from . models import Picture, Video

# Create your views here.


def home(request):
    return render(request, 'base/index.html')

def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid:
            picture = form.save(commit=False)
            picture.user = request.user
            picture.save()
            return redirect(picture_detail, pk=picture.pk)
    else:
        form = PictureForm()
    return render(request, 'base/upload_picture.html', {'form':form})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid:
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect(video_detail, pk=video.pk)
    else:
        form = VideoForm()
    return render(request, 'base/upload_video.html', {'form':form})
