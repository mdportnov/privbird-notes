#!/bin/bash

while ! python manage.py sqlflush > /dev/null 2>&1 ;do
    echo "Waiting for database..."
    sleep 1
done

echo "Preparing database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Creating superuser"
python manage.py createsuperuser --noinput

exec "$@"