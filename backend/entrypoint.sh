#!/bin/bash

#echo "Preparing database migrations"
#python ./backend/manage.py makemigrations

echo "Apply database migrations"
python ./backend/manage.py migrate

#echo "Starting server."
#python ./backend/manage.py runserver 0.0.0.0:8000

exec "$@"