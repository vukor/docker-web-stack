#!/bin/sh

DIR=`dirname "$0"`
cd $DIR

## build images
for image in postfix mysql55 php54 php56 php70 nginx; do
	cd ../.$image/ && docker build -t "vukor/$image" .
done

exit 0

