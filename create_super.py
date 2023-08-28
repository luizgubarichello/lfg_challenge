import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lfg_project.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
UserModel = get_user_model()

if not UserModel.objects.filter(username='luiz').exists():
    user=UserModel.objects.create_user('luiz', password='luiz')
    user.is_superuser=True
    user.is_staff=True
    user.save()