from django.db import models

# Create your models here.


class MusicReg(models.Model):
    name=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    release_date=models.DateField()
    genre=models.CharField(max_length=100)
    audio=models.FileField(upload_to='song')
    image=models.ImageField(upload_to='songimage')
    duration=models.CharField(max_length=50)
    album=models.CharField(max_length=100)


class Playlist(models.Model):
    song=models.ForeignKey(MusicReg,on_delete=models.CASCADE)