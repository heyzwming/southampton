# Matplotlib Node
A node named `debugging_2D_plot_matplot` can be run to see a live plot of the boat, it can be used with the simulator, when playing back rosbags or in live when the boat is in the water (see `piaccess/live-2D-plot.sh`).

To display the plot just run this line after having launch the launchfile (with roslaunch) or while a rosbag is being played:
```
rosrun sailing_robot debugging_2D_plot_matplot
```

If used with a rosbag the parameter file used during the recording should be loaded as well with:
```
rosparam load  params-dump_XXX_20XX-XX-XXTXX.XX.XX.json
```
![](http://pix.toile-libre.org/upload/original/1525165331.png)

# Rviz
Rviz is a software part of the ROS environment, it is however sometimes hard to make it works specially on virtual machines, if having trouble with it you should use the matplotlib node.

If you want to plot a map bellow the boat the ros package `rviz_satellite` is needed:
``` 
cd path_to_your_repo/sailing-robot/src
git clone https://github.com/gareth-cross/rviz_satellite.git
cd ..
catkin_make
```

Then you can run `rviz` and use the configuration file: `path_to_your_repo/sailing-robot/utilities/config.rviz`

You will see the boat and an history over the last 50s.

Rviz visualisation is handled by the node called `debugging_2D_plot` and works in both simulation and real world (if you receive topics from the boat).

### Troubleshooting 
If you have the error: `For frame [map]: Fixed Frame [my_frame] does not exist`, run the command:

```
rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 map my_frame 100
```