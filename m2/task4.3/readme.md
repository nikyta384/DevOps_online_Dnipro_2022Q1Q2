**Part 1**

1.

'D' = UNINTERRUPTABLE SLEEP,'R' = RUNNING,'S' = INTERRUPTABLE SLEEP,'T' = STOPPED,'Z' = ZOMBIE - 5 state

2.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c2.png)

3.

Proc - file system, who contain information about proccess in system.

4.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c4.png)

5.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c5.png)

6.

A kernel process inherits the environment of its parent process, when user process creating current user.


7.

Command 'top' show all proccess and states in status strings. Process 'top' have a running state.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c7.png)

8.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c8.png)

9.

top, htop, netstat and other.


10.

Main information - all task in system and their owner, PID, procent of taked memory space and CPU capacity, active time after start.

11.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c11.png)

12.


<Enter> or <Space> - Refresh-Display, ? or h - Help.


13.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/%D1%8113.png)

14.


Process priority meaning how mutch time will give defined proccess in defined state.


15.


renice -n <number of priority> -p <PID>


16.


kill <signal> <PID>. Command for showing list of given signals 'kill -l'
For example: kill -9 1456


17.


jobs - show background proccess, fg - start proccess in foreground mode, bg - start proccess in background mode, nohup - retranslate command output data not to the terminal, but to file nohup.out.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/c17.png)

**Part 2**

1.

Most frequently used command 'ssh username@host' where username - user of remote system and host - ip of remote host. Them require input host's password.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/cc1.png)

2.

Create ssh keys:
ssh-keygen
ssh username@host
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go= ~/.ssh && cat >> ~/.ssh/authorized_keys"

3.


ssh-keygen -t dsa/ecdsa/ed25519/rsa 
-t - types of ssh keys.


4.
  
![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/cc4.png)
