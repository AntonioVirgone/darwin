#!/bin/zsh

SCRIPT_DIR=${0%/*}
echo
echo -e "script directory is \e[1m$SCRIPT_DIR\e[0m"
echo

python manage.py makemigrations

python manage.py migrate
