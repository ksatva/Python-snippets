Devices:
1. Gentoo 
2. ubuntu_dev (VBox)
3. kali_dojo (VBox)
4. ASUS (android phone) 

Install 'openssh server' and 'openssh client' on all the devices for bidirectional access
Guide:
1.
2. https://help.ubuntu.com/lts/serverguide/openssh-server.html
3.
4.

##COMMANDS
##--1---------------
#'Gentoo' to 'ubuntu_dev':
ssh -p 3022 k@127.0.0.1

#'Gentoo' to 'ASUS phone':
ssh -p 2222 ASUS-X01AD-k@192.168.43.72

#'Gentoo' to 'kali_dojo':
?????
ssh -p 3022 k@127.0.0.1

##--2----------------
#'ubuntu_dev' to 'Gentoo' 
ssh -p 22 root@192.168.43.133

#'ubuntu_dev' to 'ASUS phone'
ssh -p 2222 ASUS-X01AD-k@192.168.43.72

#'ubuntu_dev' to 'kali_dojo'
?????

##--3-----------<test>------
#'kali_dojo' to 'Gentoo' <test>
ssh -p 22 root@192.168.43.133

#'kali_dojo' to 'ubuntu_dev' <test>
ssh -p 3022 k@127.0.0.1

#'kali_dojo' to 'ASUS phone' <test>
ssh -p 2222 ASUS-X01AD-k@192.168.43.72

##--4-----------------
#'ASUS phone' to 'Gentoo'
???

#'ASUS phone' to 'ubuntu_dev'
???

#'ASUS phone' to 'kali_dojo'
???


##to see open ssh ports
netstat -tuplen

TODO: Code it to a python UI
find other ssh port numbers

##secure copy
scp -p 3022 /home/k/development k@127.0.0.1:~/Desktop/
#https://www.howtogeek.com/66776/HOW-TO-REMOTELY-COPY-FILES-OVER-SSH-WITHOUT-ENTERING-YOUR-PASSWORD/

READ for more:
https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account