#!/bin/zsh
while getopts ':n:' arg; do
  case $arg in
    n) MODULE_NAME=$OPTARG;;
  esac
done

SCRIPT_DIR=${0%/*}
echo
echo -e "script directory is \e[1m$SCRIPT_DIR\e[0m"
echo

if [[ -n $MODULE_NAME ]]; then
  echo -e "create new module \e[1m$MODULE_NAME\e[0m"
  # Creare un nuovo modulo:
  python manage.py startapp $MODULE_NAME
echo
else
  echo -e "Error: Missing module name. Lunch command with -n MODULE_NAME"
  echo
fi


