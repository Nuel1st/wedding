from django.contrib import admin
from . models import Picture, Video

# Register your models here.


class PictureAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'upload_date']
    search_fields = ['user__username']

admin.site.register(Picture, PictureAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['user', 'video',  'upload_date']
    search_fields = ['user__username']

admin.site.register(Video, VideoAdmin)