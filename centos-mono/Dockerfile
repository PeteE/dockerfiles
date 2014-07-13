FROM centos

MAINTAINER Pete Erickson <pete.perickson@gmail.com>

# http://download.opensuse.org/repositories/home:/tpokorra:/mono/CentOS_CentOS-6/home:tpokorra:mono.repo
ADD mono.repo /etc/yum.repos.d/mono.repo
yum install -y mono-opt mono-xsp-opt

CMD ["/bin/bash"]
