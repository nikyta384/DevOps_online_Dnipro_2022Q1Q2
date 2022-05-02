**Task 5**

1. Configured static ip address on interfaces with Netplan.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/1.png)

2. Brought up DHCP server on ubuntu_server1 with isc-dhcp-server tool and configured /etc/dhcp/dhcpd.conf file.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/2.png)

3. Clients can't ping each other but can ping default gateway - interfaces on server.

4. Virtual lo interface on client1.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/3.png)

Configured routing to 172.18.13.1 via server1 and to 172.18.23.1 via 10.1.1.1 .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/4.1.png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/4.2.png)

5. Summarizing agress and mask for 172.18.13.1 and 172.18.23.1 .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/5.1.png)

Configure union route via server1 .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/5.2.png)

6. SSH connect to server1 and each clients.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/6.1.png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/6.2.png)

7. Iptables firewall witch first and second predetermined condition. 

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/7.1.png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/7.2.png)

8. Configured NAT on server1 for getting clients global network access.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m3/task5/8.png)
