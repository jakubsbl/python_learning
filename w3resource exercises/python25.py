# 25. Write a Python program to check whether a specified value is contained in a group of values.
# https://www.w3resource.com/python-exercises/python-basic-exercise-25.php

lst = input("Please enter list of numbers e.g. 1,5,10,15: ")
x = input("Please enter a number to check is in list or no: ")


if x in lst:
    print("Your number is in list")
else:
    print("Your number isn't in list")