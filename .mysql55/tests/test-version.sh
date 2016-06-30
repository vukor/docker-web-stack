#!/bin/sh

MYSQL_VERSION=$1
if [ -z $MYSQL_VERSION ]
then
  echo "MySQL version does not defined!"
  exit 1
fi

if mysql --version | grep -q ${MYSQL_VERSION}
then
  echo "Test version passed"
  exit 0
fi

echo "Test version failed"
exit 1

