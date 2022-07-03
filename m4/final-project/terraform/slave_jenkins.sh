#!/bin/bash

sudo yum update –y
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade
sudo yum install jenkins java-1.8.0-openjdk-devel -y
sudo yum install docker -y
sudo systemctl daemon-reload
sudo systemctl start jenkins
sudo systemctl enable docker.service
sudo systemctl start docker.service
mkdir /home/ec2-user/jenkins
chmod 777 /home/ec2-user/jenkins

