## Version: 0.4
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

### repo
## needs to install php 5.4
RUN yum install wget -y && wget -q -O - https://www.atomicorp.com/installers/atomic | sed 's/!\ $NON_INT/$NON_INT/' | sh

### create user dev
RUN useradd dev -u 1000

### php
RUN yum install php php-cli php-mysql php-mbstring php-gd php-fpm php-mssql php-xml php-tidy ImageMagick which -y
COPY ./etc/php-fpm.conf /etc/php-fpm.conf
COPY ./etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf
COPY ./etc/php.ini /etc/php.ini

### etc
## set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime
RUN ln -s /usr/bin/identify /usr/local/bin/identify && ln -s /usr/bin/convert /usr/local/bin/convert

### volumes
## php-fpm
VOLUME ["/etc/php-fpm.d/"]

## web
VOLUME ["/home/dev/logs/"]
VOLUME ["/home/dev/htdocs/"]

### main
CMD ["/usr/sbin/php-fpm","--nodaemonize"]

## allow ports 
EXPOSE 9000

