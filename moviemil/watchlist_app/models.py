from django.db import models


class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name
