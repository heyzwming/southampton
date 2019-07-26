
# Sensors

We have two set of hardware setups. Namely 2016's Magellan to 2017's Zhenghe.

2016 hardware list

| Name  |Model   |  Document | Library  | Node  |
|---|---|---|---|---|
|  Accelerometer & Compass | LSM303D  | [Polulu](https://www.pololu.com/file/0J703/LSM303D.pdf)  |  |[sensor_driver_imu](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_imu) & [sensor_driver_wind_direction](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_wind_direction)|
|  Gyro  |  L3GD20H |  [Polulu](https://www.pololu.com/file/0J731/L3GD20H.pdf) |  | [sensor_driver_imu](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_imu)  |
|  GPS  |    Ublox MAX M8Q     |     [Ublox](https://www.u-blox.com/sites/default/files/MAX-M8-FW3_DataSheet_%28UBX-15031506%29.pdf)     |      |[sensor_driver_gps](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_gps) |

2017 hardware list

| Name  |Model   |  Document | Library  | Node  |
|---|---|---|---|---|
|  IMU | Xsens MTi 3 | [Xsens](https://www.mouser.com/catalog/specsheets/xsens_DatasheetMTi1series.pdf)  | [ROS XSens](http://wiki.ros.org/ethzasl_xsens_driver) |[sensor_service_imu](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_service_imu) |
| Wind sensor  |    LSM303D    |    [Polulu](https://www.pololu.com/file/0J703/LSM303D.pdf) |        | [sensor_driver_wind_direction](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_wind_direction)                            |
|  GPS  |    Ublox MAX M8Q     |     [Ublox](https://www.u-blox.com/sites/default/files/MAX-M8-FW3_DataSheet_%28UBX-15031506%29.pdf)     |      |[sensor_driver_gps](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/sensor_driver_gps) |



# Actuator
|  Name |Model   |  Document  |  Library | Node  |
|---|---|---|---|---|
|  Rudder servo | Futaba S3003  |   |  [pigpio](http://abyz.co.uk/rpi/pigpio/) |  [actuator_driver_rudder](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/actuator_driver_rudder) |
|  Sail servo  |  HiTec 785 HB | [Google drive](https://drive.google.com/file/d/0B0FZNysk4zLXREdoMUFxT0JMZkE/view)  | [pigpio](http://abyz.co.uk/rpi/pigpio/) |  [actuator_driver_rudder](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/actuator_driver_rudder)  |