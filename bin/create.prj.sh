#!/bin/sh

## check on right argument
prjname=$1

if test -z ${prjname}
then
	echo "You forgot set prj name! Exiting.. \nUse: create.prj.sh PRJNAME"
	exit 1
fi

## create virtual host
workdir=$(dirname $0)

cd $workdir || exit 2

if test -f ../.nginx/etc/nginx/hosts/${prjname}.conf
then
	echo "prj host "${prjname}" already exists! Exiting.."
	exit 3
fi

sed "s/PRJ_NAME/${prjname}/g" ../.nginx/etc/nginx/hosts/template-conf > ../.nginx/etc/nginx/hosts/${prjname}.conf

## create document root
mkdir -p ../www/${prjname}/www/

## need restart docker-compose
echo "Finish.\nNow restart docker running\ndocker-compose restart"

exit 0

