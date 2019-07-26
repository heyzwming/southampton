An overview of the nodes and topics is in our repository: [Node Overview](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/notes/node-overview.svg) (open with inkscape)


## Topics
* [sailing_state](#sailing_state)
* [wind_direction_apparent](#wind_direction_apparent)
* [wind_direction_real](#wind_direction_real)
* [wind_direction_average](#wind_direction_average)
* [wind_speed_apparent](#wind_speed_apparent)
* [wind_speed_real](#wind_speed_real)
* [heading](#heading)
* [pitch](#pitch)
* [roll](#roll)
* [goal_heading](#goal_heading)
* [imu](#imu)
* [current_wp](#current_wp)
* [gps](#gps)
* [gps_satellites](#gps_satellites)
* [position](#position)
* [position_error](#position_error)
* [PoS_control](#PoS_control)
* [tack_sail](#tack_sail)
* [rudder_control](#rudder_control)
* [tack_rudder](#tack_rudder)
* [distance_to_waypoint](#distance_to_waypoint)
* [heading_to_waypoint](#heading_to_waypoint)
* [camera_detection](#camera_detection)
* [remote_control](#remote_control)
* [temporary_wp](#temporary_wp)

### Debug topics
* [debug_sailsheet_normalized](#debug_sailsheet_normalized)
* [debug_sailsheet_pwm](#debug_sailsheet_pwm)
* [led_blink](#led_blink)
* [debugging_2D_plot](#debugging_2D_plot)
* [debugging_2D_plot_origin](#debugging_2D_plot_origin)
* [debugging_2D_plot_wp](#debugging_2D_plot_wp)
* [gps_fix](#gps_fix)
* [gpd_satellites](#gps_satellites)
* [mag_x_comp](#mag_x_comp)
* [mag_y_comp](#mag_y_comp)
* [mag_x](#mag_x)
* [mag_y](#mag_z)
* [mag_z](#mag_y)



##### `coordinate system`
 
The coordinate system of the boat is z-axis down, y-axis point to star port.
See the picture below:
![Coordinate system](http://www.shipjournal.co/index.php/sst/article/viewFile/92/300/2798)



##### `sailing_state` 
Data type: `[String]`
   - `'normal'` sail towards goal heading
   - `'tack_to_port_tack'` and `'tack_to_stbd_tack'`overwrites goal heading

##### `wind_direction_apparent` 
Data type: `[Float64]`
   - angle 0 to 360 degrees, giving the direction the wind is coming from, relative to the boat; 0 degrees means boat is heading directly upwind (see figure below)

##### `wind_direction_real` 
Data type: `[Float32]`
   - angle 0 to 360 degrees, giving an estimate of the actual direction the wind is coming from, 0 degrees is North (see figure below)

##### `wind_direction_average` 
Data type: `[Float32]`
   - angle 0 to 360 degrees, giving the average direction the wind is coming from, 0 degrees is North (see figure below)
![Wind Direction](http://imgh.us/WindDirection.svg)

##### `wind_speed_apparent`
Data type: `[Float64]`
   - Speed in m/s

##### `wind_speed_real`
Data type: `[Float32]`
   - Speed in m/s


##### `heading` 
Data type: `[Float32]`
   - angle 0 to 360 degrees, giving the current heading of the boat; 0 degrees is North (see figure below)

##### `pitch`
Data type: `[Float32]`
   - pitch angle in radian between -pi and pi based on the accelerometer

##### `roll`
Data type: `[Float32]`
   - roll angle in radian between -pi and pi based on the accelerometer


##### `goal_heading` 
Data type: `[Float32]`
   - angle 0 to 360 degrees, heading that the boat is currently trying to achieve; 0 degrees is North (see figure below)



![figure](http://i.imgur.com/0W5tQSU.png)

##### `imu` 
Data type: self defined msg
* accx [Float32]
* accy [Float32]
* accz [Float32]
* gyrox [Float32]
* gyroy [Float32]
* gyroz [Float32]
* magx [Float32]
* magy [Float32]
* magz [Float32]


##### `current_wp`
Data type: nmea NavSatFix: [sensor_msgs/NavSatFix](http://wiki.ros.org/nmea_navsat_driver)
   - next point the path planning wants the boat to head to

##### `gps` 
Data type: nmea NavSatFix: [sensor_msgs/NavSatFix](http://wiki.ros.org/nmea_navsat_driver)
   - rough position from the gps

##### `gps_satellites`
Data type: `[Int16]`
   - Number of satellites detected by the GPS


##### `position` 
Data type: nmea NavSatFix: [sensor_msgs/NavSatFix](http://wiki.ros.org/nmea_navsat_driver)
   - estimate of the position based on imu and gps


##### `position_error`
Data type: `[Float32]`
   - In meters, giving the absolute error in global position. 

##### `PoS_control`
Data type: `[Float32]`
   - In degrees, giving the angle at which the sail should be, based on current heading and wind speed (see figure above)

##### `sail_servo`
Data type: `[UInt16]`
   - In degrees, giving maximum winch servo the control angle (0 to 90)

##### `tack_sail` (OVERWRITES: PoS_control)
Data type: `[Float32]`
   - In degrees, giving the angle at which the sail should be for completing a tack

##### `rudder_control`
Data type: `[Int16]`
   - In degrees, giving the angle at which the rudder should be for achieving the current goal heading (see figure above)

##### `tack_rudder` (OVERWRITES: rudder_control)
Data type: `[Float32]`
   - In degrees, giving the rudder angle for completing a tack manoeuvre

##### `distance_to_waypoint`
Data type: `[Float32]`
   - In metres, the cartesian distance between the boat's GPS location and the active waypoint. Only published while the current task is sailing to a waypoint.



##### `heading_to_waypoint`
Data type: `[Float32]`
   - The heading from the boat's GPS location to the active waypoint. Only published while the current task is sailing to a waypoint.
##### ` camera_detection`
Data type: `[String]`
   - publish `nothing` when nothing is detected, and `detected` when something is detected


### Debug topics


##### `debug_sailsheet_normalized`
Data type: `[Float32]`
   - The servo setting for the sail normalized between 0 and 1, 0 representing the sheet being fully in, 1 the sheet being fully out

##### `debug_sailsheet_pwm`
Data type: `[Float32]`
   - raw PWM value given to the sail pin

##### `led_blink`
Data type: `[Int32]`
   - rgb values given as an int with a shift of 300: 
 * red= `255*300*300 + 0*300 + 0`
 * green= `0*300*300 + 255*300 + 0`
 * lilac= `200*300*300 + 162*300 + 200`


##### `debugging_2D_plot`
Data type: `[MarkerArray]`
   - Pulish the history of the boat position for RViz

##### `debugging_2D_plot_origin`
Data type: `[NavSatFix]`
   - Pulish map origin position for RViz

##### `debugging_2D_plot_wp`
Data type: `[MarkerArray]`
   - Pulish the waypoints for RViz

##### `gps_fix`
Data type: `[gpswtime]`
   - Publish the gps time as well as the boat position

##### `gps_satellites`
Data tyoe: `[Int16]`
   - Publish the amount of satellites visible by the gps

##### `mag_x_comp`
Data type: `[Float32]`
   - magnetometer X compensated

##### `mag_y_comp`
Data type: `[Float32]`
   - magnetometer Y compensated

##### `mag_x`
Data type: `[Float32]`
   - raw magnetometer X

##### `mag_y`
Data type: `[Float32]`
   - raw magnetometer Y

##### `mag_z`
Data type: `[Float32]`
   - raw magnetometer Z



## Messages


##### `velocity`
Data type: self defined msg
* velx [Float32]
* vely [Float32]
* velz [Float32]


##### `gpswtime`
Data type: self defined msg
* fix [NavSatFix]
* time_h [uint16]
* time_m [uint16]
* time_s [uint16]


## Parameters
The parameters are defined in yaml files in the sailing_robot/launch/parameters folder.
A few notes on parameters:
* make sure you add a comment above each parameter, explaining it and specifying what units it is in
* getting parameters from the parameter server takes noticeably time (tens of ms), so don't use it in loops
* parameters are values that may change from experiment to experiment, but not during the experiment
* think python dictionary! Parameters can be interpreted as python dictionaries containing python dictionaries...
* more information: [ROS wiki](http://wiki.ros.org/Parameter%20Server)


## Internal variables

##### `goal_$$$`  
the output to be published
