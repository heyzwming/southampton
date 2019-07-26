The software of our project is based on **Robot Operating System** (known as **ROS**). This distributed and modular operating system can help us to build software system more effectively. However, ROS is only officially supported on Ubuntu Linux system which is  inconvenient for Windows/Mac user. Here we have setup some system image with pre-installed ROS image. 


************************************
For Windows/macOS user:

 ## Use Virtual Machine (VM) with VirtualBox 

 * Download a copy of VirtualBox from <https://www.virtualbox.org>
 * Download [64 bit version](https://cdn.ubiquityrobotics.net/workstation-1.0.1.zip) VM image
 * Open VirtualBox app and import the image you have just downloaded with the option 'Use the existing virtual hard disk file'

![Import](https://i.imgur.com/P3vhzJv.png)

* login: `ubuntu`

* password: `ubuntu`

## Post installation setup
Once you have the virtual machine running there is still a couple of steps that needs to be done:
* Clone the github repository in your home folder:
```
git clone https://github.com/Maritime-Robotics-Student-Society/sailing-robot.git
```
* Install the needed dependencies for the sailing robot
```
~/sailing-robot/utilities/setup_scripts/Setup_ALL.sh workstation
```
* Run catkin_make in the sailing-robot folder
```
cd ~/sailing-robot
catkin_make
```
* Add the setup.bash to your .bashrc
```
echo "source ~/sailing-robot/devel/setup.bash" >> ~/.bashrc
```
* And that's all!