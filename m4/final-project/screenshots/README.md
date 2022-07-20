# Final project

student **Pavlovskyi Mykyta**

**PAVLOVSKYI-BLOG**

Description: this if full authomaticaly predefined infrastructure including 2 ec2-instances on AWS one of which Jenkins-master, second - jenkins slave and in the same time mini-production.

**Step-by-step actions:**

1. We have empty AWS Paris location.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(2).png)

2. Previously, in repository not include folder 'secrets' with predefined script connect master to slave and Jenkins credentials in format xml.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(3).png)

3. I wrote simple python main script which manage terraform, ansible and other bash scripts. We run this script and watch command 'terraform init' and 'terraform apply'.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(4).png)

4. This is output data.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(5).png)

5. In AWS Paris region creating and initializing 2 instances.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(6).png)

6. Some time later instances have status '2/2 checks passed'.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(7).png)

7. Confirm this enter 'yes'.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(8).png)

8. Script show master and slave with own ip addresses. Next step - run predefined ansible playbook. For this we should enter path of master's ssh private key and path secrets directory. After that ansible copy secrets on master instance and runing post_script_master.sh. Now ansible completed successfull.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(10).png)

9. We have ready to work jenkins master and slave, credetials and installed plugins.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(11).png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(12).png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(13).png)

10. Specifying Github webhook.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(14).png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(15).png)

11. Creating item - pipeline 'pavlovskyi-blog'. Marking webhook build trigger.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(16).png)

12. Markins pipeline definition, scm and my project repository.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(17).png)

13. Marking branch and Jenkinsfile path.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(18).png)

14. For example we build 0.1.0 current version.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(19).png)

15. Build complete successfull.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(20).png)

16. Current aplication version - v1 - 0.1.0 .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(21).png)

17. Now we edit version in Jenkinsfile and index.html .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(24).png)

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(25).png)

18. Build starting after commit.

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(26).png)

19. Build complete. Current application version - v2 - 0.2.0 .

![](https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2/blob/develop/m4/final-project/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20(27).png)

