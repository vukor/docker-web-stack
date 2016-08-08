#!/bin/bash

function CheckVersion()
{
  if [[ -z $1 || -z $2 ]]
  then
    echo "Docker image and/or work version does not defined!"
    exit 1
  fi

  DOCKER_IMAGE=$1
  WORK_VERSION=$2

  docker run --rm $DOCKER_IMAGE /tests/test-version.sh $WORK_VERSION
}

case $1 in

  build )
    for image in vukor/nginx vukor/mysql:5.5 vukor/php:5.3 vukor/php:5.4 vukor/php:5.5 vukor/php:5.6 vukor/php:7.0
    do
      docker build --rm=true --pull -t vukor/nginx .nginx
    done
    ;;

  test )
    echo "Test version nginx"
    CheckVersion vukor/nginx 1.10
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version mysql"
    CheckVersion vukor/mysql:5.5 5.5
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version PHP 5.3"
    CheckVersion vukor/php:5.3 5.3
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version PHP 5.4"
    CheckVersion vukor/php:5.4 5.4
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version PHP 5.5"
    CheckVersion vukor/php:5.5 5.5
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version PHP 5.6"
    CheckVersion vukor/php:5.6 5.6
    if [ $? != 0 ]; then exit 1; fi
    
    echo "Test version PHP 7.0"
    CheckVersion vukor/php:7.0 7.0
    if [ $? != 0 ]; then exit 1; fi
    ;;

  * ) echo "Use: test" && exit 1 ;;

esac

exit 0

