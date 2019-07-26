Before installation, please make sure you have right version of Ubuntu on your computer, either [VM](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/wiki/Virtual-Machine-for-Windows-Mac-users) or [native](http://releases.ubuntu.com/14.04/). This tutorial is for user with fresh installed Ubuntu, if you are using virtual machine with Ubuntu and ROS preinstalled you can skip this part.

ROS Indigo Igloo is the previous long-term support release, is available for Ubuntu Trusty (14.04) and many other platforms. This tutorial follows official ROS Indigo install [instructions](http://wiki.ros.org/indigo/Installation).

### Setup your `sources.list`

~~~
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
~~~

### Set up your keys
~~~
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
~~~

### Installation
First, make sure your Debian package index is up-to-date:
~~~
sudo apt-get update
~~~
Desktop-Full Install: it includes ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception
~~~
sudo apt-get install ros-indigo-desktop-full
~~~

Update available packages for tab completion:
~~~
apt-cache search ors-indigo
~~~

### Initialize rosdep

~~~
sudo rosdep init
rosdep update
~~~

### Environment setup

~~~
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
~~~

Note: if you prefer use other shell please source the setup file into your own rc file.

e.g.
~~~
echo "source /opt/ros/indigo/setup.zsh" >> ~/.zshrc
source ~/.zshrc
~~~

### Getting rosinstall
~~~
sudo apt-get install python-rosinstall
~~~
rosinstall is a frequently used command-line tool in ROS that is distributed separately. It enables you to easily download many source trees for ROS packages with one command.