#!/bin/bash

cd /backup || exit 1

## init variables
cmd="mysql -h mysql -u${MYSQL_LOGIN} -p${MYSQL_PASSWORD}"
dbs=`ls mysql.*.sql.gz | cut -d . -f 2`

## backup dbs
cd /backup || exit 1
for db in ${dbs}; do
  ${cmd} -e "create database ${db};"
  zcat mysql.${db}.sql.gz | ${cmd} ${db}
done

exit 0

