# Docker

ROS and the other required software is now available in a docker image.  It has currently only been tested on Linux, but it should work on Mac and Windows. 

# Getting Docker and the image

The Docker application itself is available for Linux, MacOS 10.10.3 or higher and Windows 10 Pro, Enterprise and Education editions from the [Docker website.](https://docs.docker.com/engine/installation/). There are additional requirements listed there.

Once installed, the image can be downloaded and the environment set up by running:
```
/utilities/docker/build-all.sh
```

# Scripts

I have 3 scripts that I use that help with running and interacting with the container. These will work on Linux, should work on Mac and wont work on Windows. (If someone has a Mac or Windows and can edit this so it fits with them, it would be appreciated please.)

### start-container.sh

The docker image does not include a clone of the github repository, instead it sets up a direct link between /home/pi/sailing-robot within the container and your clone of the github repositiry on your computer. This allows the python code to be immediately available to ROS inside the container after you have edited it on your computer. This direct link works both ways, so anything that you edit within /home/pi/sailing-robot directly edits the corresponding files on your computer.

On macOS, you may need publish the port to host first `docker run -p 2222:22 -it sotonsailbot/ros:indigo`, start SSH service inside container, then access your container with `ssh -p 2222 pi@localhost`. 

When the above is run, you will find your self at the command prompt within the docker container.

For ROS to work, after you have confirmed that /home/pi/sailing-robot does point to the right location you need to run `catkin_make`.  You should only need to run this once, unless you re-clone the github repository.

### term-in-container.sh

When run in your computer, this will open another bash terminal on the container for you to use.  It will only work when the container is already running (thanks to the script `start-container.sh`).

### ssh-x-to-container.sh

This will ssh into the container with X-forwarding.  Again the container needs to be already running, you also need to have started the ssh server by running /home/pi/start-ssh-server within the container.

The password is 'raspberry'.
