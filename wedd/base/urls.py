from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns=[
    path('', views.home, name= 'home'),
    path('upload-picture/', views.upload_picture, name='upload-picture'),
    path('upload-video/', views.upload_video, name='upload-video')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Melhem & Christie"
admin.site.site_title = "Melhem & Christie"
admin.site.site_index_title = " Welcome to our wedding "