#!/usr/bin/bash

stty sane  # prevent garbled text over ssh
if [ $DJANGO_BASE_DIR ]
then
  python $DJANGO_BASE_DIR/manage.py testserver --addrport 0.0.0.0:7000 $DJANGO_BASE_DIR/cypress/fixtures/empty.json --noinput
else
  echo "DJANGO_BASE_DIR environment variable not specified. Using current directory..."
  echo "This script should be run from the root folder of your Django app"
  python $PWD/manage.py testserver --addrport 0.0.0.0:7000 $PWD/cypress/fixtures/empty.json --noinput
fi
