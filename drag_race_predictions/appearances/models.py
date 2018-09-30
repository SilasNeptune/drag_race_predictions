from django.db import models
from drag_race_predictions.episodes.models import Episode
from drag_race_predictions.queens.models import Queen

class Appearance(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    queen = models.ForeignKey(Queen, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
