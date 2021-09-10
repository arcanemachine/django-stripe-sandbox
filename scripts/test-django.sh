if [ $DJANGO_BASE_DIR ]
then
  # find $DJANGO_BASE_DIR/$1 -name $2 | entr python3 ./manage.py test --keepdb
  nodemon --ext "$1/*.py" --exec "./manage.py test $1.$2 --keepdb"
else
  DJANGO_BASE_DIR=/home/serv/code/django/django-stripe-sandbox
  echo "DJANGO_BASE_DIR not specified. Using $DJANGO_BASE_DIR..."
  # echo "find $DJANGO_BASE_DIR/$1 -name $2 | entr python3 ./manage.py test --keepdb"
  # find $DJANGO_BASE_DIR/$1 -name $2 | entr python3 ./manage.py test --keepdb
  nodemon --ext "$1/*.py" --exec "./manage.py test $1.$2"
fi
