# Calibration
### utilities/run_calibration.sh
To calibrate the compass and the wind direction sensor you only need to run `./run_calibration.sh` **while roscore is running** and follow the indications on the screen.

# Area scanning
### Waypoint generation: utilities/waypoint_generator_area_scanning.py
You need a waypoint parameter file with the following points:

![Area scanning wp](http://pix.toile-libre.org/upload/original/1472146433.png)

Then you just have to use that parameter file as an argument for the script:
```
./waypoint_generator_area_scanning.py path/waypoints.yaml
```
And it will create a new parameter file called `previous_name_auto_gen.yaml` that can be used directly in a launch file.

_Note that the points C and D are not mandatory, and can be set to dummy values before the competition (their coordinates can be deduced from A and B)_

### Analysis: utilities/analyse_area_scanning
This script needs the same parameter file as the waypoint generator script (with A and B), and the gps log file.

```
./analyse_area_scanning path/waypoints.yaml ../gps-trace.csv
```

_The parameter file used can be either the 'source' file (the one used in argument for the waypoint generator script) or the output of the waypoint generator script_

# Station keeping
### Analysis: utilities/analyse_station_keeping
This script analyses gps log file to compute the score for the station keeping challenge. The path to the gps log file as well as the coordinates of the buoy need to be set as variables at the beginning of the script.

# Obstacle avoidance
### waypoint generation: utilities/waypoint_generator_obstacle_avoidance.py
First you need a waypoint parameter file with wp1~4 defined as follow:
![Obstacle detection image](http://pix.toile-libre.org/upload/original/1472932308.png)

Then you can just run the script with the parameter file in argument:
```
./waypoint_generator_obstacle_avoidance.py path/waypoints.yaml
```
It will create a new parameter file to be used for the challenge.

# Set date and time
### utilities/setclock

This should be run each time we power up the raspi, so that we can find the
diagnostic logs later. It will prompt you for the current date, then use the
GPS receiver to get the time (UTC), and finally set the raspi's system clock.


# Find servo limits
### utilities/servo_key.py

Interactively manipulate a servo to find PWM limits. Key bindings:

- Left/Right: step pulse down/up
- Down/Up: set pulse to min/max (1000/2000)
- Home: set pulse to mid value (1500)

*Should only be needed if the physical boat configuration changes*

***


# Round buoy
### Waypoint generation: utilities/waypoint_generator_round_buoy.py
This script can be used to generate waypoints around a buoy for the boat to round it. 
The radius at which the waypoint will be from the buoy and the orientation of the path can be set at the beginning of the file. The file only needs as an argument a parameter file with the proper waypoint and will create a new parameter file with the generated waypoints.
```
./waypoint_generator_round_buoy.py ../src/sailing_robot/launch/parameters/sailingClub_waypoints.yaml
```
_This script is actually not useful for the competition_
