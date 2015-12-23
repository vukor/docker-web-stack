## Version: 0.3
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

### repo
## needs to install php 5.6
RUN yum install wget -y \
	&& wget http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm \
	&& wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \
	&& rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm \
	&& rm -f remi-release-6*.rpm epel-release-6*.rpm
COPY ./etc/yum.repos.d/remi.repo /etc/yum.repos.d/remi.repo

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
RUN yum install php php-cli php-mysql php-mbstring php-gd php-fpm php-mssql php-xml php-tidy php-mcrypt ImageMagick which -y
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

## allow ports
EXPOSE 9000

