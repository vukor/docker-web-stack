## Version: 1.1
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## import centos 6 base key
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

### repo
## needs to install php 5.4
RUN yum install wget -y && wget -q -O - https://www.atomicorp.com/installers/atomic | sed 's/!\ $NON_INT/$NON_INT/' | sh

### build, configure libiconv 1.x (needs for php)
RUN yum install tar gcc -y && \
    cd /tmp && \
    wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz && \
    tar -xvzf ./libiconv-1.14.tar.gz && \
    cd ./libiconv-1.14/ && \
    ./configure --prefix=/usr/local && \
    make && make install && \
    cd /tmp && rm -rf /tmp/libiconv* && \
    echo "export LD_PRELOAD=/usr/local/lib/preloadable_libiconv.so" >> /etc/bashrc

### create, configure user dev
RUN useradd dev -u 1000

### php
RUN yum install php php-cli php-mysqlnd php-mbstring php-gd php-fpm php-mssql php-xml php-tidy php-pear php-devel php-mcrypt ImageMagick which -y
COPY ./etc/php-fpm.conf /etc/php-fpm.conf
COPY ./etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf
COPY ./etc/php.ini /etc/php.ini
RUN pecl install xdebug 

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

## allow ports
EXPOSE 9000

