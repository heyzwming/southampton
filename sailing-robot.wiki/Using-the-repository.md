First, get [ROS](http://www.ros.org/) set up. This can be done with a [virtual machine](Virtual-Machine-for-Windows-Mac-users), using our [docker image](Docker) or [installing ROS](Install-of-ROS) directly on the system (laptop, raspberry pi etc.).

Now, clone the repository. If you're not familiar with git, you'll want to read [guide](https://guides.github.com/introduction/flow/) soon, but for now, you can run this command in a terminal:

    git clone https://github.com/Maritime-Robotics-Student-Society/sailing-robot.git

You now have a copy of the code on your computer. Change into the new folder:

    cd sailing-robot

This folder is a [catkin workspace](http://wiki.ros.org/catkin/workspaces). To get started, run:

    catkin_make
    source devel/setup.bash  # This sets up environment variables

To run the tests:

    catkin_make run_tests

To launch the nodes

    roslaunch sailing_robot test-all-systems.launch