#!/bin/sh

sleep 10
python manage.py makemigrations

sleep 10
python manage.py migrate

sleep 5
python create_super.py

python manage.py runserver 0.0.0.0:8000