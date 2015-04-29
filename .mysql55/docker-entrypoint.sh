#!/bin/bash

if [ "$1" = '/usr/libexec/mysqld' ]; then
	## init mysql
	test -d /var/lib/mysql/mysql || mysql_install_db

	## set permissions
	tempSqlFile='/tmp/mysql-first-time.sql'
	cat > "$tempSqlFile" <<-EOSQL
		-- Delete all current users
		DELETE FROM mysql.user ;
	
		-- Create root user
		GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}' ;
		
		-- Create work user for manage from non-localhost
		GRANT ALL ON *.* TO '$MYSQL_LOGIN'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}' ;
		
		-- Create work user for manage from localhost
		GRANT ALL ON *.* TO '$MYSQL_LOGIN'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}' ;
		      
		-- Delete database test
		DROP DATABASE IF EXISTS test ;
	EOSQL

	echo 'FLUSH PRIVILEGES ;' >> "$tempSqlFile"

	exec "$@" --init-file="$tempSqlFile"
fi

exec "$@"

