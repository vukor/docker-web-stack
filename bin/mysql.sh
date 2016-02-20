#!/bin/bash

dir=`dirname ${0}`

## change to work dir
cd ${dir}/../ || exit 2

docker exec -ti mysql bash -c 'exec mysql -u $MYSQL_LOGIN -p$MYSQL_PASSWORD -h mysql'

exit 0

