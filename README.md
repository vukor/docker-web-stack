docker-web-stack
===========

This is docker projects for run web apps as containers - nginx, php, mysql, postfix, dnsmasq.

Docker images statistic
===========
* vukor/cron
 
[![](https://images.microbadger.com/badges/image/vukor/cron.svg)](http://microbadger.com/images/vukor/cron "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/vukor/cron.svg)](http://microbadger.com/images/vukor/cron "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/license/vukor/cron.svg)](http://microbadger.com/images/vukor/cron "Get your own license badge on microbadger.com")

* vukor/nginx

[![](https://images.microbadger.com/badges/image/vukor/nginx.svg)](http://microbadger.com/images/vukor/nginx "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/vukor/nginx.svg)](http://microbadger.com/images/vukor/nginx "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/license/vukor/nginx.svg)](http://microbadger.com/images/vukor/nginx "Get your own license badge on microbadger.com")

Necessary steps
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

* Go to your http:/localhost/
  You must see response from nginx - "410 Gone"

* If you use OSX (like me) - you also have to create alias 127.0.0.2 on loopback:

    `` sudo ifconfig lo0 127.0.0.2 alias ``


Manage your projects
===========

* You can create your first virtual host:

    `` ./bin/create.prj.py PRJNAME `` (then documentroot is ./htdocs/PRJNAME/)

	or

    `` ./bin/create.prj.py -v5 PRJNAME `` (then documentroot is ./htdocs/PRJNAME/www/)

    After that put your web files to documentroot


Manage your containers
===========

* For stop, start, restart, up and build for all or one of project container you have to run:
    
    `` docker-compose stop [container]``
    
    `` docker-compose start [container]``
    
    `` docker-compose restart [container]``
    
    `` docker-compose up -d [container]``
    
    `` docker-compose build [container]``


Manage your DNS zones
===========

* For example, you create project my-first-project.ru. But for working in your browser you need that domain myp-first-project.ru is resolve to 127.0.0.1

* For working this create your first zone:

    ``
    echo "address=/my-first-project.ru/127.0.0.1" > .dnsmasq/zones/my-first-project.ru
    ``

* Build and up image dnsmasq:
    
    `` docker-compose build dns ``

    `` docker-compose up -d dns ``

* And add to /etc/resolv.conf after your real nameservers:

    `` nameserver 127.0.0.2 ``

* Now you can resolve my-first-project.ru. and \*.my-first-project.ru. to 127.0.0.1


Manage databases
===========

1. For connect to mysql service run:
    
    `` make db-cmd ``

2. For backup all your databases run:
    
    `` make db-backup ``

    Your databases will be located in backup/ directory.

3. For restore all databases from backup/ directory to mysql service run:
    
    `` make db-restore ``


How update images (move it crontab in docker soon)
============

Run:

`` make upgrade ``

This command backup all your databases, upgrade docker images, run new updated containers and restore all your databases.


Manage crontab
===========

Now you have docker image vukor/cron for run cron jobs.

* For list current cron jobs run:

`` make crontabs ``

* For add or remove cron jobs, you have to edit file ".cron/cron-jobs" and run:

`` docker-compose build cron &% docker-compose up -d cron ``


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
