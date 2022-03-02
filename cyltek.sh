#!/bin/bash

sleep 3
killall wpa_supplicant
sleep 1
wpa_supplicant -Dnl80211 -iwlan0 -c/data/wifi/wpa_supplicant.conf &
sleep 3
dhcpc.script start wlan0

cd /data/CYL-Thermal

sleep 3
insmod cdc-acm.ko
echo 0 > /proc/mtprintk

./Cyber_run.sh
sleep 1
./run.sh