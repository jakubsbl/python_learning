# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# https://www.w3resource.com/python-exercises/python-basic-exercise-12.php

import calendar 
y = int(input("Input the year : "))
m = int(input("Input the month : "))

print(calendar.month(y,m))