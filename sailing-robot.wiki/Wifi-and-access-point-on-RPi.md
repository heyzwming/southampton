We have `ssh` access to our RPi through WiFi connection. Default password for both RPi is: `sailrobot`



#Configuration notes
##The Pi Hut dongle
WiFi dongle supplied by thePihub is 'out of box' for RPi. 


##Edimax dongle type WiFi
https://gist.github.com/eduardschaeli/4734786

There is some issue of the official drivers for our WiFi dongle. And we need use the self made drivers to make the AP mode works.

https://jenssegers.com/43/Realtek-RTL8188-based-access-point-on-Raspberry-Pi

##Edimax omni-directional WiFi
Check kernel version of linux first
`uname -a`

Then download setup script based on linux version

```
wget https://dl.dropboxusercontent.com/u/80256631/8812au-4.1.7-v7-817.tar.gz
tar xzf 8812au-4.1.7-v7-817.tar.gz
./install.sh
```
Reboot and WiFi device will show in `iwconfig`