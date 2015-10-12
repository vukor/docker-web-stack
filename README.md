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

How manage databases
===========

1. For connect to mysql service run:
    
    `` make db-cmd ``

2. For backup all your databases run:
    
    `` make db-backup ``

    Your databases will be located in backup/ directory.

3. For restore all databases from backup/ directory to mysql service run:
    
    `` make db-restore ``

How update images
============
Run:

`` make upgrade ``

This command backup all your databases, upgrade docker images, run new updated containers and restore all your databases.

How manage docker images
===========

1. For build all images in project run:
    
    `` make build ``

2. For push all images in project run:
    
    `` make push ``

Share dirs
===========

``.nginx/etc, .mysql5x/etc, .php5x/etc - config files``

``htdocs - web files``

``logs - app logs``

``backup - mysql backups``

Useful links
============
  - http://docs.docker.com/compose/
  - https://github.com/docker/compose/blob/master/docs/index.md

