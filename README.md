docker-web-stack
===========

This is docker projects for build web containers

How it's work
===========

1. Download project:

    ``$ git clone https://vukor@github.com/vukor/docker-web-stack.git``

2. Install docker and docker-compose on your system

3. [ OPTIONAL ] Change the docker-compose.yml. For example, you can change MYSQL_ROOT_PASSWORD or change php version (default php 5.6).

4. Create and start containers:
    
    `` cd docker-web-stack/ ``
    `` docker-compose up -d ``

5. Create your first virtual host:

    `` ./bin/create.prj.sh PRJNAME ``

After that put web files to dir ./www/PRJNAME/www/

6. For stop, start, restart containers run:
    
    `` docker-compose stop ``
    
    `` docker-compose start ``
    
    `` docker-compose restart ``

7. For connect to mysql server run:
    
    `` docker run -ti --link dockerwebstack_mysql_1:mysql --rm=true vukor/mysql55 bash -c 'exec mysql -p$MYSQL_ENV_MYSQL_ROOT_PASSWORD -h$MYSQL_PORT_3306_TCP_ADDR' ``

8. For create/restore db save sql-commands in ./backup/run.sql and run:
    
    `` docker run -ti -v `pwd`/backup:/backup --link dockerwebstack_mysql_1:mysql --rm=true vukor/mysql55 bash -c 'exec cat /backup/run.sql | mysql -p$MYSQL_ENV_MYSQL_ROOT_PASSWORD -h$MYSQL_PORT_3306_TCP_ADDR' ``


share dirs
===========

``.nginx/etc, .mysql5x/etc, .php5x/etc - config files``

``www - web files``

``logs - app logs``

