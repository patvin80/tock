#!/bin/bash
echo "------ Create database tables ------"
cd tock
python manage.py migrate --noinput --settings=tock.settings.production
python manage.py loaddata prod_user projects --settings=tock.settings.production
waitress-serve --port=$VCAP_APP_PORT tock.wsgi:application