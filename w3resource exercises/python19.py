# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
# https://www.w3resource.com/python-exercises/python-basic-exercise-19.php



string = input("Please enter a string:")
if string.startswith('Is'):
    print(string)
else: 
    print("Is " + string)
