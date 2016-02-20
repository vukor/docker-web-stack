#!/bin/bash

dir=`dirname ${0}`

## change to work dir
cd ${dir}/../ || exit 2

## Restore all your databases:
echo "*** Restoring all your databases.. ***"
sleep 1
docker exec -ti mysql bash -c 'exec /opt/restore.dbs.sh' || exit 1
echo "*** Restoring databases done. ***"

exit 0

