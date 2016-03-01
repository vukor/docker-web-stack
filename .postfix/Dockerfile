## Version: 0.2
FROM centos:centos6
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## import centos 6 base key
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

## create user dev
RUN useradd dev -u 1000

## postfix
RUN yum install postfix rsyslog -y
RUN chmod 5755 /usr/sbin/postdrop /usr/sbin/postqueue

### etc

## postfix settings
RUN postconf -e \
	inet_interfaces="all" \
	inet_protocols="ipv4" \
	relay_domains="dev4masses.com, online-media.ru" \
	default_transport="error"

## set timezone
RUN cp -f /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime

### main
CMD ["sh", "-c", "service rsyslog start ; service postfix start ; tail -F /var/log/maillog"]

## allow ports
EXPOSE 25

