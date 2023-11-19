# 2D-Projectile-Sim
Python program which shows the flight paths of a projectile on Earth and another planet subject to gravity. Does not take into account drag.

The user enters the initial speed, elevation angle, and height.
Flight paths for the projectile are shown for Earth and one of the following:
- Sun
- Mercury
- Venus
- Moon
- Mars
- Jupiter
- Saturn
- Uranus
- Neptune
- Pluto

As well as the flight path, the program displays the following results for both projectiles:
- Gravitational field strength
- Maximum height reached
- Displacement (magnitude, x and y components)
- Flight duration

## Code
The GUI uses tkinter for the window and turtle for the graph. The background for the turtle canvas is an external file.

The flight paths are calculated using SUVAT equations.
