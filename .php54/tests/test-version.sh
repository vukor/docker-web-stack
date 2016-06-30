#!/bin/bash

PHP_VERSION=$1
if [ -z $PHP_VERSION ]
then
  echo "PHP version does not defined!"
  exit 1
fi

CURRENT_PHP_VERSION=$(php -v | head -n1 | cut -d ' ' -f 2 | cut -d '.' -f 1,2)

if [ $CURRENT_PHP_VERSION == $PHP_VERSION ]
then
  echo "Test version passed"
  exit 0
fi

echo "Test version failed"
exit 1

