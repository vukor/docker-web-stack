docker-web-stack
===========

This is docker projects for run web apps as containers


How it's work
===========

* Download project:

    `` git clone https://vukor@github.com/vukor/docker-web-stack.git ``

* Install docker and docker-compose on your system

* [ OPTIONAL ] Change the docker-compose.yml. For example, you can change MYSQL_ROOT_PASSWORD or change php version (default php 5.6).

* Create volume data:
    
    `` cd docker-web-stack/ ``
    
    `` docker volume create --name data ``

* Download images:

    `` docker-compose pull ``

* Create and start containers:

    `` docker-compose up -d ``

* Create your first virtual host:

    `` ./bin/create.prj.py PRJNAME `` (then documentroot is ./htdocs/PRJNAME/)

	or

    `` ./bin/create.prj.py -v5 PRJNAME `` (then documentroot is ./htdocs/PRJNAME/www/)

    After that put web files to documentroot

* For stop, start, restart containers run:
    
    `` docker-compose stop [container]``
    
    `` docker-compose start [container]``
    
    `` docker-compose restart [container]``

* Add zones (if you need) to files in directory .dnsmasq/zones

* Add to /etc/resolv.conf in head:

    `` nameserver 127.0.0.2 ``


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


The MIT License (MIT)
===========
Copyright (c) 2016 Anton Bugreev <anton@bugreev.ru>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
