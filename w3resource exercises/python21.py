# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# https://www.w3resource.com/python-exercises/python-basic-exercise-21.php

number = input("Please enter your number to check is even or odd: ")


if int(number) == 0:
    print("0 cannot be devided by 2, enter another number")
elif int(number) % 2 == 0:
    print ("Your number is even")
else:
    print ("Your number is odd.")