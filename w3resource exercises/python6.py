# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# https://www.w3resource.com/python-exercises/python-basic-exer

from optparse import Values


Values = input("Input some comma seprated numbers : ")
list = Values.split(",")
tuple = tuple(list)
print('List: ', list)
print('Tuple: ', tuple)