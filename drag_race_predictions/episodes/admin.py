from django.contrib import admin
from drag_race_predictions.episodes.models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'original_air_date', 'episode_number']
    ordering = ['episode_number']

admin.site.register(Episode, EpisodeAdmin)
