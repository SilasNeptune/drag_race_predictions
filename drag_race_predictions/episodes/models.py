from django.db import models
from drag_race_predictions.seasons.models import Season

class Episode(models.Model):
    title = models.CharField(max_length=255)
    original_air_date = models.DateField()
    episode_number = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    queens = models.ManyToManyField('queens.Queen', through='appearances.Appearance')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
