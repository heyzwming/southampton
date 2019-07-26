# Water test check list:
## To do before the test:
* Charge batteries: 
  * power bank (for the pi)
  * 4 AA for the servos
  * 8 AA for the remote control
  * laptops (Tabarly)
* Write launch file for the day
* Check weather forecast (and tide)

## To do just before leaving for the test location:
* Git pull on Tabarly
* Power up the raspberry pi, ssh to it
* Send the last version of the code to the pi (with `push2pi.sh` script in /piaccess)
* Try Xsens calibration (with `mt` and piaccess script)
* Decide which set of sails to bring (adapt the launch file accordingly)
* Test connectivity of i2c devices (with `i2cdetect -y 1`)
* Test servos end stop with `test-calibration.launch` launch file

Optional:
* Check wind sensor output
* Check Xsens reading 
* Check GPS fix

## To bring:
* Water for operators 
* A towel to dry the boat
* boat keel
* Remote control (with its AA batteries)
* Tabarly
* Wifi extender 
* Boat stand (chair)
* Spare parts:
  * GPS
  * wifi dongle
  * wires
  * wind sensor
* Water proofing material:
  * tampons
  * tape
  * silicone
* Cable ties
* Toolbox
* Bumblebee tape
* A print version of the wiki (especially for wiring)
* set of sails
* Batteries
* rubber bands (for wind vane)
* pen
* print of the test location wiki page (map+waypoints)
* this checklist
* Chest waiders
* Business cards

## To do at the test location:
* Connect the mast/windsensor wire
* Connect the pi to the battery and try to ssh to it
* Calibrate and check the Xsens IMU (without the mast on)
* Assemble the mast and sails
* Calibrate wind sensor
* Check remote control and servo wiggle with `test-calibration.launch` launch file
* Check launch file for the day (check parameter file used as well)
* Check if a GPS fix can be obtained (with `rostopic echo /position` for example)
* Once we have a GPS fix, set the time on the raspberry pi with the script: `utilities/setclock`
* Waterproof the boat: both the servo control hatch and the raspberry pi one
* Run the launch file in a **screen** before putting the boat in the water
* If all the previous steps were a success you can put the boat in the water \o/ (and monitor with the dashboard and/or `piaccess/live-2D-plot.sh`)

## To do after a test
* Commit any changes that have been made on the raspberry pi
* Commit any changes that have been made on tabarly (don't forget notes in recorded_data/notes)
* Run `pullfrompi.sh` on tabarly
* Get bag and log files from the raspberry pi onto tabarly and run syncthing
* Investigate what went wrong
* Write a blog post about the sailing day ;)