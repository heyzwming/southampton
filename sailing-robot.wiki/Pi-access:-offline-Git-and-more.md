To push to the Raspi without going through the internet, first ensure that you have ssh access to the Raspi. To save retyping the password each time you connect, copy your SSH public key to it:
```
    ssh-copy-id pi@192.168.12.1
```
# piaccess folder
The `/piaccess` folder contains a variety of scripts that are used to ease the connection with the raspberry pi. They have to be run on your local machine while connected to the raspberry pi wifi access point.

## GIT with the pi
### Setup the git repository on the pi
```
./setup_repo.sh
```
This script will setup the repository and the clone on the raspberry pi. 

`sailing-robot-bare` is a directory on the Raspi containing a 'bare clone', a git repository without a working directory. Don't worry about the details. We will push code to this from our laptop, and pull it to the working repo, `sailing-robot`. This usage is hidden with the script described below.

### Push code from a laptop to the pi
```
./push2pi.sh
```
Use this script to synchronise your laptop local repository with the raspberry pi one.

### Pull code from the raspberry pi
```
./pullfrompi.sh
```
This script will get the code from the raspberry pi to your local machine, you can then connect to the internet and use the usual `git push` to upload to github.

## Time
```
./time2pi.sh
```
At every boot the raspberry pi loses date and time, this script is here to "copy" the time from your local machine to the raspberry pi. For a more precise time on the pi, you should use the GPS and the script called `/utilities/setclock`.

## USB-ip
```
./usbip-bind.sh
```
USB-ip is a method to share a usb device over the network. The usual senario is to have our XSens IMU connected via usb on the raspberry pi and calibrating it with the GUI called `mtm` (or `mt`) on your laptop. For more detail you can have a look at our blog post about usbip: http://blog.sotonsailrobot.org/articles/usbip .

## 2D live plot
```
./live-2D-plot.sh
```
This script will run the matplot visualisation locally when ROS is running on the raspberry pi. Note that you need a working ROS environment on your local machine as well to run this script.

## ssh/sftp
```
./ssh
```
This is just a shortcut to connect via ssh to the boat, same for sftp