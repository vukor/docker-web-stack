## Version: 0.4
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## import centos 6 base key
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

### repo
## needs to install php 7.0
RUN yum install wget -y \
	&& wget http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm \
	&& wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm \
	&& rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm \
	&& rm -f remi-release-6*.rpm epel-release-6*.rpm

### create, configure user dev
RUN useradd dev -u 1000

### php
RUN yum -y --enablerepo=remi,remi-test install php70 \ 
	php70-php-cli \
	php70-php-mysqlnd \
	php70-php-mbstring \
	php70-php-gd \
	php70-php-fpm \
	php70-php-mssql \
	php70-php-xml \
	php70-php-tidy \
	php70-php-mcrypt \
	php70-php-pecl-mysql \
	ImageMagick \
	which
COPY ./etc/php-fpm.conf /etc/opt/remi/php70/php-fpm.conf
COPY ./etc/php-fpm.d/www.conf /etc/opt/remi/php70/php-fpm.d/www.conf
COPY ./etc/php.ini /etc/opt/remi/php70/php.ini

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

