terraform {
  required_version = ">= 0.12"
}

provider "aws" {
  region = "eu-west-3"
}

data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  owners = ["amazon"] # Canonical
}

resource "aws_instance" "web2" {
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "t2.micro"
  subnet_id       = "subnet-0725f7fb0a2058c9b"
  private_ip      = "172.31.1.102"
  key_name        = "server1"
  security_groups = ["sg-05250449ef418effb"]
  user_data       = "${file("slave_jenkins.sh")}"
  tags = {
    Name = "jenkins-slave-prod"
  }
}


resource "aws_instance" "web1" {
  ami             = data.aws_ami.amazon_linux.id
  instance_type   = "t2.micro"
  subnet_id       = "subnet-0725f7fb0a2058c9b"
  private_ip      = "172.31.1.101"
  key_name        = "paris"
  security_groups = ["sg-05250449ef418effb"]
  user_data       = "${file("master_jenkins.sh")}"
  tags = {
    Name = "jenkins-master"
  }
}  
