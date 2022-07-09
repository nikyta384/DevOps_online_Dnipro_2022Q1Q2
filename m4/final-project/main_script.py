#! /usr/bin/python3

import os
import subprocess

os.chdir('./terraform')
print('----------------------------------------------\nterraform init-------------------------------')
os.system('terraform init')
print('----------------------------------------------\nterraform apply------------------------------')
os.system('terraform apply -auto-approve')
print('---------------------------------------------------------------------------------------------')
print("\n\nEnter yes when instances will have status '2/2 checks passed'\n\n")
yes = str(input())
if yes == 'yes':
	print("Good")
master_ip = 'aws ec2 describe-instances --region eu-west-3 --instance-ids --query Reservations[].Instances[].PublicIpAddress --filters "Name=tag:Name,Values=jenkins-master" --output=text'
slave_ip = 'aws ec2 describe-instances --region eu-west-3 --instance-ids --query Reservations[].Instances[].PublicIpAddress --filters "Name=tag:Name,Values=jenkins-slave-prod" --output=text'

m_ip = subprocess.check_output(master_ip, shell=True).decode()
m_ip = m_ip.strip()
print('---------------------------------------------------------------------------------------------')
print('master ip: '+ m_ip)
s_ip = subprocess.check_output(slave_ip, shell=True).decode()
s_ip = s_ip.strip()
print('slave-prod ip: ' + s_ip)

print('---------------------------------------------------------------------------------------------')
print('\n\nConnect to instances and bind master and slave\n\n')
os.chdir('..')

print("\n\nInput directory with private key for master:")
master_key = str(input())

file = open('hosts.txt', 'w')
file.write('[master]\nmaster  ansible_host='+str(m_ip)+'  ansible_user=ec2-user  ansible_ssh_private_key='+master_key)
file.close()

os.system("eval 'ssh-agent' && ssh-add "+master_key)

print("\n\nInput path of directory 'secrets' (creds for jenkins slave):")

cred_dir = str(input())

with open('ansible_playbook.yaml', 'r') as file1 :
  filedata = file1.read()

filedata = filedata.replace('replacedir', cred_dir)

with open('ansible_playbook.yaml', 'w') as file2:
  file2.write(filedata)
os.system("ansible-playbook ansible_playbook.yaml")

print('---------------------------------------------\nINFRASTRUCTURE READY TO WORK------------------')
