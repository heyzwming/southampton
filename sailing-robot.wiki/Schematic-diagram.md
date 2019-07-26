## Table of Contents
- [Pinouts \(to multiplexer\)](#user-content-pinouts-to-multiplexer)
  - [RC](#user-content-rc)
  - [AA Battery Pack](#user-content-aa-battery-pack)
  - [Sail Servo](#user-content-sail-servo)
  - [Rudder Servo](#user-content-rudder-servo)
  - [RPi](#user-content-rpi)
  - [To Itself](#user-content-to-itself)
- [Pinouts \(to RPi\)](#user-content-pinouts-to-rpi)
  - [IMU](#user-content-imu)
  - [GPS](#user-content-gps)
  - [Multiplexer](#user-content-multiplexer)
- [Pictures for Pinouts](#user-content-pictures-for-pinouts)
  - [For the Multiplexer](#user-content-for-the-multiplexer)
  - [For the RPi](#user-content-for-the-rpi)
  - [Full RPi GPIO Pins](#user-content-full-rpi-gpio-pins)

## Pinouts (to multiplexer)
### RC
| RC        | Multiplexer  |
| ------    |:------:      |
| Ch 1      | S1 - signal  |
| Ch 3      | S3 - signal  |
| Ch 5      | SEL - signal |
| VCC       | S4 - VS      |
| GND       | S4 - GND     |

### AA Battery Pack
| Battery | Multiplexer |
| ------  |:------:     |
| 5V      | M2 - VM     |
| GND     | M2 - GND    |

### Sail Servo
| Sail servo | Multiplexer   |
| ------     | ------        |
| Output     | OUT3 - signal |
| VCC        | OUT3 - VM     |
| GND        | OUT3 - GND    |

### Rudder Servo
| Rudder servo | Multiplexer   |
| ------       | ------        |
| Output       | OUT1 - signal |
| VCC          | OUT1 - VM     |
| GND          | OUT1 - GND    |

### RPi
| RPi           | Multiplexer  |
| ------        | ------       |
| GND; P1-9     | SEL - GND    |
| GPIO13; P1-33 | M1 - signal  |
| GPIO24; P2-18 | M3 - signal  |

### To Itself
| Multiplexer | Multiplexer |
| ------      | ------      |
| SEL - VM    | S2 - VS     |

## Pinouts (to RPi)
### IMU
| IMU    | RPi                  |
| ------ |:----------:          |
| SDA    | SDA (GPIO 2; P1-3)   |
| SCL    | SCL ( GPIO 3; P1-5)  |
| GND    | GND (P1-6)           |
| VIN    | 3.3V (P1-1)          |

### GPS
| GPS    | RPi                 |
| ------ |:----------:         |
| VCC    | 3.3V (P1-1)         |
| GND    | GND (P1-6)          |
| RX     | TX (GPIO 14; P1-8)  |
| TX     | RX (GPIO 15; P1-10) |

### Multiplexer
| Multiplexer   | RPi           |
| ------        | ------        |
| SEL - GND     | GND; P1-9     |
| M3 - signal   | GPIO24; P2-18 |

<!-- Since the Arduinos aren't used anymore these are commented out
## Pinouts (to Arduinos)
### Servos
| Servo                  | Uno 1      |
| ------                 |:----------:|
| Winch Output (Orange)  | P9         |
| Rudder Output (Orange) | P10        |

### Sensors
| Sensor                     | Uno 2      |
| ------                     |:----------:|
| Wind Speed Output (Green)  | P3         |
| Wind Direction Input (Red) | A0         |
-->

## Pictures for Pinouts
### Complete schematic
svg version available [here](https://raw.githubusercontent.com/Maritime-Robotics-Student-Society/Boat-construction/master/Electronics%20Mast/schematic.svg)
![](https://raw.githubusercontent.com/Maritime-Robotics-Student-Society/Boat-construction/master/Electronics%20Mast/schematic.png)






<!-- 
### For the Multiplexer
[![Multiplexer pinouts](http://i67.tinypic.com/bgwgfb.png)](http://i67.tinypic.com/bgwgfb.png "Multiplexer pinouts")

### For the RPi
[![RPi pinouts](http://i68.tinypic.com/sw6a9k.jpg)](http://i68.tinypic.com/sw6a9k.jpg "RPi pinouts")

### Full RPi GPIO pins
[![RPi pinouts](https://i.stack.imgur.com/sVvsB.jpg)](https://i.stack.imgur.com/sVvsB.jpg "RPi all pin")
-->




<!-- Since the Arduinos aren't used anymore these are commented out
### For the Servos
[![Sensors pinouts](http://bit.ly/24ATzlm)](http://bit.ly/24ATzlm "Servos pinouts")
### For the Sensors
[![Sensors pinouts](http://bit.ly/1Yahic8)](http://bit.ly/1Yahic8 "Sensors pinouts")
-->

<!-- 
This is the second half of the 2nd draft, which originally continued from the tables above

<a name="circuit" href="http://bit.ly/1WFafsN">
![Is your Internet that bad damn](http://bit.ly/1WFafsN)
</a>
(Click on it for full size; does not open in a new tab be warned)

## Port term explanations:
- RPi_USB_5V: The 5V rail from the RPi's USB cable, which powers the Arduinos
- RPi_USB_GND: The ground rail from the RPi's USB cable, which powers the Arduinos
- RPi_GND: One of the GND pins on the RPi (Pins 1-6)
- 5V: A 5V rail from the RPi's IO pins (Pins 2,4)
- {From,To}_power_bank: Do I really need to explain this

## Things to Note:
- There are two separate Unos; one works the sensors and the other works the servos. The labels for them in the schematics, Uno 1 and 2 are just meant to further show that they are distinct.
- Both Unos are model R3s.
- The RPi is an RPi 3 Model B.
- (For myself) make schematic pics for the RPi, and beautify the ones for the Unos.

-->

<!--
# Disclaimer
Whatever you see below you is the first draft of this whole thing. So don't bother looking at this,
# Good Afternoon
Below are the schematics for each component, all in swaggy PNG form. Use the Table o Links to get to the ones you want quicker than it'll take you to scroll the page and stop scrolling at the one you want, plus maybe some additional corrections if you scroll too far or not far enough. This is all possible thanks to technology. Thanks technology. (You're welcome Sim -- Technology)

# Table o Links
1. [Sensors](#sensors)
  1. [Compass](#compass)
  1. [GPS Sensor](#gps)
  1. [Wind Direction Sensor Dot Pine Elf Goddess](#windDirection)
  1. [Wind Speed Sensor Dot Pea En Gee](#windSpeed)
1. [Servos](#servos)
  1. [Winch Servo Dot Peri-peri-flavoured Enriched Gobstopper](#winchServo)
  1. [Rudder Servo Dot People Eat Gas](#rudderServo)

# <a name="sensors"></a>Sensors (from https://img42.com/collection/O9B9E)
## <a name="compass"></a>Compass
![Compass.png]()
## <a name="GPS"></a>GPS Sensor
![GPS.png]()
## <a name="windDirection"></a>Wind Direction Sensor
![Wind Speed Sensor dot Pingu](http://bit.ly/26E94gp)
## <a name="windSpeed"></a>Wind Speed Sensor
![Wind Direction Sensor dot PNG](http://bit.ly/1TbLZr6)

# <a name="servos"></a>Servos (from https://img42.com/collection/39pf7)
## <a name="winchServo"></a>Winch Servo
![Winch Servo dot Ping Pong](http://bit.ly/1SRdR6L)
## <a name="rudderServo"></a>Rudder Servo
![Rudder Servo dot jpeg haha just kidding it's still PNG](http://bit.ly/26ElPaz)
-->