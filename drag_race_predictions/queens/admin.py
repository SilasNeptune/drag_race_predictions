from django.contrib import admin
from drag_race_predictions.queens.models import Queen

class QueenAdmin(admin.ModelAdmin):
    list_display = ['name', 'race', 'hometown', 'current_city', 'date_of_birth']
    ordering = ['name']

admin.site.register(Queen, QueenAdmin)
