from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='pictures/')
    # description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    # description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.image