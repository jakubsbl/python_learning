# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
# https://www.w3resource.com/python-exercises/python-basic-exercise-23.php



str = input("Please input a string: ")
copies = input("Please input how many copies of the first 2 characters of given string you need: ")
first_2_ch = str[0:2]

try:
    print(first_2_ch * (int)(copies))
except ValueError:
    print("PLEASE ENTER INTEGER AS SECOND ARGUMENT")