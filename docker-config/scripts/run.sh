#!/usr/bin/env sh

python manage.py migrate --noinput
python manage.py initadmin
python manage.py inittestdata
python manage.py collectstatic --noinput
gunicorn HelpMap.wsgi -b 0.0.0.0:3013
