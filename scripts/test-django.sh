if [ $DJANGO_BASE_DIR ]
then
  find $DJANGO_BASE_DIR/$1 -name $2 | entr python3 ./manage.py test --keepdb
else
  DJANGO_BASE_DIR=/home/serv/code/django/django-stripe-sandbox
  echo "DJANGO_BASE_DIR not specified. Using $DJANGO_BASE_DIR..."
  find $DJANGO_BASE_DIR/$1 -name $2 | entr python3 ./manage.py test --keepdb
fi
