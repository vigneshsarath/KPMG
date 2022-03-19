#!/bin/bash

yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "KPMG Challenge1 from $(hostname -i)" > /var/www/html/index.html