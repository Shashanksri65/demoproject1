from django.db import models
from django.core.urlresolvers import reverse

# My models are here.

class Album(models.Model):
    artist = models.CharField(max_length=30)
    album_title = models.CharField(max_length=40)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=260)

    def get_absolute_url(self):
        return reverse('shashank:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=40)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title

