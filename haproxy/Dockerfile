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

# run script
ADD run.sh /

CMD ["/run.sh"]