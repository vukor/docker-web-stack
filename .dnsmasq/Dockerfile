## Version: 0.2
FROM alpine
MAINTAINER Anton Bugreev <anton@bugreev.ru>

## Install packages
RUN apk update && \
    apk add dnsmasq

## Copy config
COPY dnsmasq.conf /etc/dnsmasq.conf
COPY zones /etc/dnsmasq.d

## Start service
CMD ["dnsmasq", "--keep-in-foreground"]

### allow ports
EXPOSE 53

