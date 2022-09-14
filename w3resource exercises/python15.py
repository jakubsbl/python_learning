# 15. Write a Python program to get the volume of a sphere with radius 6.
# https://www.w3resource.com/python-exercises/python-basic-exercise-15.php
# V = 4/3 × π × r3

from math import pi

r = input("Please enter a radius of sphere to get the volume: ")
V = 4/3*pi*(int)(r)**3
print("The volume of sphere with your radius is: ", V)
