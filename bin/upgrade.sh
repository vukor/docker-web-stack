#!/bin/bash

## Start
echo "** Starting upgrade.. **"

dir=`dirname ${0}`

## change to work dir
cd ${dir}/../ || exit 2

## Backup all your databases:
echo "*** Backing up all your databases.. ***"
docker-compose run --rm mysql bash -c 'exec /opt/backup.dbs.sh' || exit 1
echo "** Backing up done. *** "

## Upgrade docker images
echo "*** Upgrading docker images.. ***"
docker-compose pull || exit 1
echo "*** Upgrading done. ***"

## Stop docker containers
echo "*** Stopping docker containers.. ***"
docker-compose stop || exit 1
echo "*** Stopping done. ***"

## Create and run new docker containers
echo "*** Creating and running new docker containers.. ***"
docker-compose up -d || exit 1
echo "*** Docker containers are started. ***"

## Restore all your databases:
echo "*** Restoring all your databases.. ***"
sleep 1
docker-compose run --rm mysql bash -c 'exec /opt/restore.dbs.sh' || exit 1
echo "*** Restoring databases done. ***"

## Finish
echo "** Upgrade succesfully finished. **"

exit 0

