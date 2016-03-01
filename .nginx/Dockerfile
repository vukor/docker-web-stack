## Version: 0.5
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## create user dev
RUN useradd dev -u 1000

## import centos 6 base key
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

## nginx
RUN rpm --import http://nginx.org/keys/nginx_signing.key && \
    rpm -Uvh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm && \
    sed -i 's/gpgcheck=0/gpgcheck=1/' /etc/yum.repos.d/nginx.repo && \
    yum install nginx which -y 
COPY ./etc/nginx/nginx.conf /etc/nginx/nginx.conf

### etc
## set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime

### volumes
## nginx virtual hosts
VOLUME ["/etc/nginx/hosts/"]

## web
VOLUME ["/home/dev/logs/"]
VOLUME ["/home/dev/htdocs/"]

### main
CMD ["/usr/sbin/nginx"]

### allow ports 
EXPOSE 80
EXPOSE 443

