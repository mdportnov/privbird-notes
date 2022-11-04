#!/bin/bash

echo "Preparing database migrations"
python ./backend/manage.py makemigrations

echo "Apply database migrations"
python ./backend/manage.py migrate

echo "Collect static files"
python ./backend/manage.py collectstatic --noinput

echo "Creating superuser"
python ./backend/manage.py createsuperuser --noinput

exec "$@"