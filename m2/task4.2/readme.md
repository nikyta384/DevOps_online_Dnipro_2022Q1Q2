**Task4.2**

1.
/etc/passwd - username : password : userID : groupID : fullUserInfo : homeDirectory : LoginShell/etc/group - groupName
/etc/group - groupUser : groupPassword : groupID : UsersInGroup
Exist on the system users who have correct value in field login shell, fo example /bin/bash.

2.

UID - Unique identifier of user in OS. The system UIDs from 0 to 99 should be statically allocated by the system, and shall not be created by applications. The system UIDs from 100 to 499 should be reserved for dynamic allocation by system administrators and post install scripts using useradd. UID placed in 3 column in file /etc/passwd. 

3.

GID - Unique identifier of group in OS. 4 column in file /etc/passwd or 3 column in /etc/group.

4.

Last column in /etc/group determine belonging of user to the specific group.

5.

Command useradd <USERNAME>. Required parametr is be root user.

6.
  
Switch on root user. Command usermod -l <login-name> <old-name>.

7.
  
Directory /etc/skel is used to initiate home directory when a user is first created.

8.
  
Command userdel -f <username>.


9.
  
Lock - passwd -l <username>  usermod -l <username>, unlock - passwd -u <username>  usermod -u <username>.

10.
  
Exist command 'sudo passwd <user>' and stay field 'New password' empty.

11.
  
Show filetype and access right, user, group, size and file.
 
![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/b11.png)

  
12.
  
Access rights exist and for user, group and other. r - read, w - write, x - execute and '-' - not have permisions.

13.
  
-


14)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/b14.png)
 
15.
  
1 - x(execute), 2 - w(write), 4 -r(read). umask - provide permissions for future created files.

16.
  
stiky bit - feature for advanced management above file in directory, add file in directory can any users but remove file can only owner.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m2/b16.png)
 
17.
  
shebang !# /usr/bash - for example.
