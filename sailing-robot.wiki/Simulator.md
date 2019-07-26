The simulator is used to test the behaviour of the boat in different conditions without any hardware sensors or actuators. It is composed of several nodes that are going to substitute (and simulate) real hardware parts.

## The nodes:
- `simulation_velocity`: this node uses a polar plot to deduce the boat velocity from the wind direction, a punishment is also added after a tack. The minimum velocity of the boat as well as a multiplicative coefficient can be set in the parameter file.
- `simulation_position`: this node subscribe to `heading` and `velocity` to compute the next position of the boat. A water stream can also be specified in the parameter file. 
_Note that the initial position is defined based on the first waypoint in the waypoints parameter file._
- `simulation_heading`: this node compute the new heading based on the command of the rudder (topic `rudder_control`), and the boat velocity (topic `velocity`). For this node a rather physical approach was employed considering that the boat moves on a circle defined by its rudder and keel; the rudder angle will change the radius of the circle etc. A multiplicative coefficient can be defined in the parameter file to increase or decrease the effect of the rudder on the heading.
- `simulation_wind_apparent`: this node just publish the apparent wind direction and speed according to parameters set in the parameter file (because the apparent wind is used, the resulting value also depends on the velocity and the heading of the boat).
- `simulation_gps_fix`: this node is only used to be able to print gps log (publish `gps_fix` that contains the position and time)

## How to use the simulator:
- check if you have correctly set all the parameters you need for your simulation in parameter file (usually in `launch/parameters/simulator.yaml`)
- check if you have a proper waypoint parameter file for your simulation (usually `launch/parameters/XXX_waypoins.yaml`)
- check if you have a launch file with all the required nodes and the right parameter files loaded, an example called `simulator.launch` is in the launch folder.
- You can start the simulation with roslaunch: `roslaunch sailing_robot simulator.launch`
- If you want to monitor what the boat is doing you can use the dashboard and/or [2D plot](2D-plot-of-the-boat)

## Other uses of the simulator
An example of a multiboat simulation is present in the launch folder, this can be useful to test the effect of a parameter/algorithm on the boat. You can specified two different simulator parameter files, default parameter files etc.

Because the simulator is divided in nodes one can simulate some nodes and use real hardware for others (the most obvious one being the wind sensor).

## Limitations of the simulator
One should not rely on the simulator entirely because a lot of external variables are not considered: no heeling is simulated, the velocity of the boat only depends on the wind (and not on previous state of the boat), the sail settings are not used (!), no proper analysis of the boat behaviour was used to program the simulator, the simulated boat can't get full of water and thus sink etc.