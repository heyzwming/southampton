The computer that uses the wifi extender can use its own built in wifi to serve as an access point so other can connect to the boat.

create_ap can be used for that: https://github.com/oblique/create_ap/blob/master/create_ap

then the command is the following one:

``` sudo create_ap pc_wifi extender_wifi wifi_SSID password ```

pc_wifi is the device interface (`wlan0` for example), and extender_wifi is the extender one (`wlan1` for example).

To identify name of device interface plug out WiFi extender and use `iwconfig` and see which interface disappeared.