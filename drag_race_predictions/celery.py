import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drag_race_predictions.settings')

app = Celery('drag_race_predictions')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
