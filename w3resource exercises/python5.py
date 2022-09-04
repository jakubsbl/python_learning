# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# https://www.w3resource.com/python-exercises/python-basic-exercise-5.php

from tokenize import Name
from unicodedata import name


name = input("Input your First Name : ")
surname = input("Input your Last Name : ")
print (surname + " " + name )