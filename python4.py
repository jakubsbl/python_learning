# Write a Python program which accepts the radius of a circle from the user and compute the area.
# The area of cicle is pi*r^2
# https://www.w3resource.com/python-exercises/python-basic-exercise-4.php

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
