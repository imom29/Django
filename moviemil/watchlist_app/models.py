from django.db import models


class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(
        "StreamPlatform", on_delete=models.CASCADE, related_name="watchlist"
    )

    def __str__(self):
        return self.title


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name



class Reviews(models.Model):
    review_username = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(
        Watchlist, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return str(self.rating)