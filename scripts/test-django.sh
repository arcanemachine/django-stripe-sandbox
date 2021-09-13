if [ $DJANGO_BASE_DIR ]
then
  find $DJANGO_BASE_DIR -name "*.py" | entr python manage.py test --keepdb
else
  DJANGO_BASE_DIR=$PWD
  echo "DJANGO_BASE_DIR not specified. Using $DJANGO_BASE_DIR..."
  echo "\nUntil you have set a DJANGO_BASE_DIR environment variable, this script will need to be run from the root folder of your Django app"
  find $DJANGO_BASE_DIR -name "*.py" | entr python manage.py test $1 --keepdb
fi
