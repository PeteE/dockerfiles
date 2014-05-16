#!/bin/bash

echo "Staring haproxy."
/usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg -db
