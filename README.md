docker-web-stack
===========

This is docker projects for run web apps as containers

How it's work
===========

1. Download project:

    `` git clone https://vukor@github.com/vukor/docker-web-stack.git``

2. Install docker and docker-compose on your system

3. [ OPTIONAL ] Change the docker-compose.yml. For example, you can change MYSQL_ROOT_PASSWORD or change php version (default php 5.6).

4. Create and start containers:
    
    `` cd docker-web-stack/ ``

    `` docker-compose up -d ``

5. Create your first virtual host:

    `` ./bin/create.prj.py PRJNAME `` (then documentroot is ./htdocs/PRJNAME/)

	or

    `` ./bin/create.prj.py -v5 PRJNAME `` (then documentroot is ./htdocs/PRJNAME/www/)

    After that put web files to documentroot

6. For stop, start, restart containers run:
    
    `` docker-compose stop [container]``
    
    `` docker-compose start [container]``
    
    `` docker-compose restart [container]``

7. For connect to mysql server run:
    
    `` docker-compose run --rm mysql bash -c 'exec mysql -u $MYSQL_LOGIN -p$MYSQL_PASSWORD -h mysql' ``

8. For create/restore db save sql-commands in ./backup/run.sql and run:
    
    `` docker-compose run --rm mysql bash -c 'exec cat /backup/run.sql | mysql -u $MYSQL_LOGIN -p$MYSQL_PASSWORD -h mysql' ``


Share dirs
===========

``.nginx/etc, .mysql5x/etc, .php5x/etc - config files``

``htdocs - web files``

``logs - app logs``


Useful links
============
  - http://docs.docker.com/compose/
  - https://github.com/docker/compose/blob/master/docs/index.md

