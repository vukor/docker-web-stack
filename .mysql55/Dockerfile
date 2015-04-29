## Version: 0.0.2
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## repo
# needs to install mysql 5.5
RUN yum install wget -y && wget -q -O - https://www.atomicorp.com/installers/atomic | sed 's/!\ $NON_INT/$NON_INT/' | sh

## mysql
RUN yum install mysql mysql-server -y
RUN mkdir -m 770 /var/log/mysql && chown mysql:mysql /var/log/mysql
ADD ./etc/my.cnf /etc/my.cnf

## create user dev
RUN useradd dev -u 1000

### etc
## set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime
RUN yum install which -y

### volumes

## php-fpm
VOLUME ["/var/log/mysql/"]

### main
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/libexec/mysqld"]

### allow ports 
EXPOSE 3306

