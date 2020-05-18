#!/usr/bin/env sh

python manage.py migrate --noinput
python manage.py initadmin
gunicorn HelpMap.wsgi -b 0.0.0.0:3013
