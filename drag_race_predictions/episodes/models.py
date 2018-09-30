from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=255)
    original_air_date = models.DateField()
    episode_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
