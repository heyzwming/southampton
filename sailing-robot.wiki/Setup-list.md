If one person is absent, their responsibility is shared amongst the rest, but it is clear what tasks have to be done by someone else now

PIER + TONY
- assemble boat
- attach sails
- check remote control works
- tell Nana and Sophia/Thomas when RPi is online; 
- waterproof
- get ready for calibration
- set up gopro if we use it

TONY
- set up wifi
- check wifi laptop can ssh onto boat
- set up wind sensor

### Software setup
SOPHIA + THOMAS
- git pull
- check if there is a more recent launch file
- git push if needed
- set time   (if script doesnt work: sudo date -s 2016-08-25T17:30:45 )
- run roscore
- run calibration script (compass + wind direction)
- run launch file
    check if data from wind direction and compass make sens
        - apply a heeling angle to the boat and see if the heading changes (topic 'heading')
- check if sail servo is moving in relation to the wind direction
- monitor boat position with rviz
- put the boat in water and check if it actually floats, if not use a buoyancy aid or use autosub code instead of sailing boat one



