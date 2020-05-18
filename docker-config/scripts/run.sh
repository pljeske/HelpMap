#!/usr/bin/env sh

python manage.py migrate --noinput
python manage.py initadmin
gunicorn HelpMap.wsgi -b djangoapp:3013