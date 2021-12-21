#!/bin/bash

echo "Collect Static Files"
python3 manage.py collectstatic --noinput

echo "Apply Database Migrations"
python3 manage.py migrate

echo "Load default data"
python3 manage.py loaddata_cus ./*/default_data/*.yaml
# python3 manage.py loaddata_cus ./*/default_data/*.yaml --force

echo "compile language translation messages"
python3 manage.py compilemessages

# echo "kill celery worker"
# pkill -9 -f 'celery worker'

echo "Start Server"
nginx -g "daemon on;" && uwsgi --ini /etc/uwsgi/uwsgi.ini