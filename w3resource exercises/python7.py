# 7. Write a Python program to accept a filename from the user and print the extension of that.
# https://www.w3resource.com/python-exercises/python-basic-exercise-7.php

filename = input("Please input the filename: ")
file_extension = filename.split(".")
print("The extension of the file is: " + repr(file_extension[-1]))