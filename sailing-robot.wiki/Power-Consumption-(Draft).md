# Oi this just be a draft first

# Did you know that electric products need power to be used?
Really? That's insane.
# I know.

Calculated the power consumption of our entire circuit. But just what makes up our circuit?

# The Things That Make Up Our Circuit
The things that make up our circuit are:
- Two Arduino Unos
- An RPi
- Two servos: one for the rudder and another for the winch
- Three sensors: GPS, wind direction and wind speed
I think.

So the currents that each use are:

<table id="currentTable">
  <tr>
    <th> Component </th>
    <th> Current Usage/mA </th>
  </tr>
  <tr>
    <td> Uno(each) </td>
    <td> 50 </td>
  </tr>
  <tr>
    <td> RPi </td>
    <td> 300 max. (all four cores at 100%) </td>
  </tr>
  <tr>
    <td> Winch servo </td>
    <td> 230 (running), 50 (idle) </td>
  </tr>
  <tr>
    <td> Rudder servo </td>
    <td> 140±50 (max), 15 (idle) </td>
  </tr>
  <tr>
    <td> GPS </td>
    <td> 21 </td>
  </tr>
  <tr>
    <td> Wind direction sensor </td>
    <td> Wow I don't actually know this please hold </td>
  </tr>
  <tr>
    <td> Wind speed sensor </td>
    <td> Same goes wow what in the world </td>
  </tr>
</table>

# Wiring circuit
So, we've got two separate circuits, each powered up with a power bank. [This one here to be exact <s>I think</s>](https://www.http://goo.gl/15cRik). The schematics for each circuit are shown right below. This can also be found in [this page](http://bit.ly/1ToVjsJ) on its own:


<a name="circuit" href="http://bit.ly/1OP9Z7P" target="blank">
![Is your Internet that bad damn](http://bit.ly/1OP9Z7P)
</a>
<!-- https://img42.com/Z1zvj -->
(Click on it for full size; opens in a new tab)

For more info on the wirings and stuff, feel free to [check out that page](http://bit.ly/1ToVjsJ).

# So How Long Can The Power Banks Stay Alive???
