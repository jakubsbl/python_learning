# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
## https://www.w3resource.com/python-exercises/python-basic-exercise-17.php


def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(1899))
print(near_thousand(901))   
print(near_thousand(899))
