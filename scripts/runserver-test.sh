#!/usr/bin/bash

stty sane  # prevent garbled text over ssh
if [ $DJANGO_BASE_DIR ]
then
  python $DJANGO_BASE_DIR/manage.py runserver 0.0.0.0:7000 cypress/fixtures/empty.json
else
  echo "DJANGO_BASE_DIR environment variable not specified. Using current directory..."
  python $PWD/manage.py testserver --addrport 0.0.0.0:7000 cypress/fixtures/empty.json
fi
