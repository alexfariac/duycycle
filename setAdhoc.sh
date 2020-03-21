systemctl stop NetworkManager.service;
ifconfig $1 down;
iwconfig $1 essid redeadhoc mode ad-hoc channel 1 ap 00:11:22:33:44:55;
iwconfig $1;
ifconfig $1 up;
ifconfig $1 192.168.1.$2 netmask 255.255.255.0
