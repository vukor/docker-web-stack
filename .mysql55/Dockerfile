## Version: 0.5
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## import centos 6 base key
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

## repo
# needs to install mysql 5.5
RUN yum install wget -y && wget -q -O - https://www.atomicorp.com/installers/atomic | sed 's/!\ $NON_INT/$NON_INT/' | sh

## mysql
RUN yum install mysql mysql-server which -y
RUN mkdir -m 770 /var/log/mysql && chown mysql:mysql /var/log/mysql
COPY ./etc/my.cnf /etc/my.cnf

## create user dev
RUN useradd dev -u 1000

### etc
## set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime

### volumes
VOLUME ["/var/log/mysql/"]

## copy mysql backup/restore scripts
COPY ./opt /opt

### main
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/libexec/mysqld"]

### allow ports 
EXPOSE 3306

