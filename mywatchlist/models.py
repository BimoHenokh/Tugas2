from django.db import models

class MyWatchlistItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()
