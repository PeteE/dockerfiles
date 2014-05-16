# run:  docker run -p 80:80 -p 443:443 -v /dev/log:/var/docker/log petee/haproxy
FROM centos

MAINTAINER Pete Erickson <pete.perickson@gmail.com>
EXPOSE 80 443

RUN yum install -y initscripts

# SRPM available here:  http://mindtouch-ops-public.s3.amazonaws.com/rpm/centos/6/SRPMS/haproxy-1.5-dev22.el6.src.rpm
# compiled with openssl and a patch to disable the networking check in init script
RUN rpm -i http://mindtouch-ops-public.s3.amazonaws.com/rpm/centos/6/x86_64/haproxy-1.5-dev22.el6.x86_64.rpm

ADD errorfiles/ /etc/haproxy/errorfiles
ADD ssl/ /etc/haproxy/ssl

# dummy config file
ADD haproxy.cfg /etc/haproxy/haproxy.cfg

RUN yum install -y MAKEDEV
RUN mkdir -p /var/docker
RUN /usr/sbin/mksock /var/docker/log

# run script
ADD run.sh /

CMD ["/run.sh"]
