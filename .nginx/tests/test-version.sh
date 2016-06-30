#!/bin/bash

NGINX_VERSION=$1
if [ -z $NGINX_VERSION ]
then
  echo "Nginx version does not defined!"
  exit 1
fi

CURRENT_NGINX_VERSION=$(nginx -V 2>&1 | grep 'nginx version:')
CURRENT_NGINX_VERSION=${CURRENT_NGINX_VERSION#*/}
CURRENT_NGINX_VERSION=$(echo $CURRENT_NGINX_VERSION | cut -d '.' -f 1,2)

if [ $CURRENT_NGINX_VERSION == $NGINX_VERSION ]
then
  echo "Test version passed"
  exit 0
fi

echo "Test version failed"
exit 1

