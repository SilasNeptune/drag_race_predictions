from django.db import models

class Queen(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)
    current_city = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    episodes = models.ManyToManyField('episodes.Episode', through='appearances.Appearance')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
