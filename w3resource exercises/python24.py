# 24. Write a Python program to test whether a passed letter is a vowel or not.
# https://www.w3resource.com/python-exercises/python-basic-exercise-24.php

letter = input("Please enter some letter and i tell you it is a vowel or is not: ")

vowels = ['a', 'e', 'i', 'o', 'u']

if letter in vowels:
    print("Your letter is vowel")
else:
    print("Your letter isn't vowel")
