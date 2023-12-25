#!/bin/bash

# This script is used to change the IP address of the nearest cache server

IP1=192.168.0.3 # @IP adresse du serveur cache plus proche
IP2=192.168.1.2 # @IP adresse du deuxieme serveur cache plus proche
IP3=192.168.2.2 # @IP adresse du troisieme serveur cache plus proche
IP4=192.168.3.2 # @IP adresse du quatrieme serveur cache plus proche

if ping -c 1 $IP1 &>/dev/null 2>&1 ; then
    sed -i "s/$IP2/$IP1/g; s/$IP3/$IP1/g; s/$IP4/$IP1/g" /etc/named/alger.esi.dz.zone

elif ping -c 1 $IP2 &>/dev/null 2>&1 ; then
    sed -i "s/$IP1/$IP2/g; s/$IP3/$IP2/g; s/$IP4/$IP2/g" /etc/named/alger.esi.dz.zone

elif ping -c 1 $IP3 &>/dev/null 2>&1 ; then
    sed -i "s/$IP1/$IP3/g; s/$IP2/$IP3/g; s/$IP4/$IP3/g" /etc/named/alger.esi.dz.zone

else
    sed -i "s/$IP1/$IP4/g; s/$IP2/$IP4/g; s/$IP3/$IP4/g" /etc/named/alger.esi.dz.zone

fi

systemctl restart named