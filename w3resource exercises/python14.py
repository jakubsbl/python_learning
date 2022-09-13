# 4. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# https://www.w3resource.com/python-exercises/python-basic-exercise-14.php

from datetime import date


day1 = date(1996, 8, 17)
day2 = date(1993, 8, 27)
difference = day1 - day2
print(difference.days)
