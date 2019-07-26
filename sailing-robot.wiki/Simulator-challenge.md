Welcome in this challenge, I'll be your guide during this tour ;)

So ROS, ROS is a complete system that is used to program the boat, all the code is written in python (but you won't have anything to program here).

## Nodes
ROS works with nodes, a node is a python script that can interact with other nodes via messages, it can publish or subscribe to messages.
You can see our nodes in the folder `sailing-robot/src/sailing_robot/scripts` (open some of the files here if you want to see how they are done, it is quite straight forward).

Today you are going to use the simulator, if you want to know a bit more how it was design you should read our [wiki page about the simulator](Simulator).

So you have nodes, now you want to run these nodes (otherwise they are not really useful). To do so you have what is called launch files.

## Launch files
Launch files are xml files that describes what to run and with which parameters, have a look in the folder `sailing-robot/src/sailing_robot/launch` 
Because you are going to use the simulator, open the file called `simulator.launch`

At the beginning of the file you load parameter files, and then launch some nodes.

To run the simulation, or in general to run the code on the boat you have to use the following command:

```
roslaunch path_to_the_launch_file.launch
```

And you can terminate it via ctrl+c

If you want to see what the boat is doing you can run (in an other terminal while roslaunch is running) the visualisation tool called `rviz`, you'll see the boat and some buoy!



## Parameters files
Parameter files are used to give ... parameters to our code, if you go in `sailing-robot/src/sailing_robot/launch/parameters` you'll see a lot of parameter files but they are not all of the same kind.
* `XXXX_waypoints.yaml`: these one are used to give the instructions to the codes, like the type of challenge, the location of waypoints to use and some related parameters, have a look in `viana_position_keeping_waypoints.yaml` and try to understand how it works.

* `simulator.yaml`: this one is only used with the simulator, not on the actual boat, and it contains environment variables (speed of the wind, its direction etc.) and some coefficients related to the simulation (but not really useful today)

* `default.yaml`: this one includes everything else, like some PID parameters, the rate at which everything is running etc.


# The challenge
Now that you are more familiar with ROS and its setup I want you to run a simulation of position keeping challenge with a wind coming from the north. Visualize all of this in `rviz`.

