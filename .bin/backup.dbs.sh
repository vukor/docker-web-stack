#!/bin/bash

## init variables
cmd="mysql -h mysql -u${MYSQL_LOGIN} -p${MYSQL_PASSWORD}"
cmdbackup="mysqldump -h mysql -u${MYSQL_LOGIN} -p${MYSQL_PASSWORD}"
dbs=`${cmd} -N -e "SHOW DATABASES" | grep -E -v 'information_schema|performance_schema|mysql'`

## backup dbs
cd /backup || exit 1
for db in ${dbs}; do
  $cmdbackup ${db} | gzip > mysql.${db}.sql.gz
done

exit 0

