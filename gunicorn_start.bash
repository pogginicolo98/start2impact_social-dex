#!/bin/bash

NAME="social_dex"
DJANGODIR=/home/ubuntu/start2impact_social-dex/social_dex
SOCKFILE=/home/ubuntu/start2impact_social-dex/venv/run/gunicorn.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=social_dex.settings
DJANGO_WSGI_MODULE=social_dex.wsgi
echo "Starting $NAME as `whoami`"


cd $DJANGODIR
source /home/ubuntu/start2impact_social-dex/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
