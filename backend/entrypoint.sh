#!/bin/bash

echo "Preparing database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Creating superuser"
python manage.py createsuperuser --noinput

exec "$@"