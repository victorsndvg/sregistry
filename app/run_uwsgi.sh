#!/bin/bash
python manage.py makemigrations
python manage.py migrate auth
python manage.py makemigrations users
python manage.py makemigrations main
python manage.py makemigrations api
python manage.py makemigrations logs
python manage.py migrate
python manage.py collectstatic --noinput
service cron start
uwsgi uwsgi.ini
