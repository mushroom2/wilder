from django.db import models
from django.utils import timezone


class Card(models.Model):
    cardfrom = models.ForeignKey('auth.User')
    cardto = models.EmailField()
    text = models.TextField()
    title = models.TextField()
    priority = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MyTrack(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    track = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    trackname = models.CharField(max_length=256, default='no name')

    def __str__(self):
        return self.trackname