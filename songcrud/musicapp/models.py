from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    Artiste = models.ForeignKey('Artiste', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    artiste_id = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    Song = models.ForeignKey('Song', null=True, blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    song_id = models.CharField(max_length=15)

    def __str__(self):
        return self.content