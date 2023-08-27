import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lfg_project.settings')

app = Celery('lfg_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
