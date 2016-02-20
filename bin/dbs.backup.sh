#!/bin/bash

dir=`dirname ${0}`

## change to work dir
cd ${dir}/../ || exit 2

## Backup all your databases:
echo "*** Backing up all your databases.. ***"
docker-compose run --rm mysql bash -c 'exec /opt/backup.dbs.sh' || exit 1
echo "** Backing up done. *** "

exit 0

