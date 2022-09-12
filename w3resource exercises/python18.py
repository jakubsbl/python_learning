# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. 
# https://www.w3resource.com/python-exercises/python-basic-exercise-18.php



x = float(input("enter first num. : "))
y = float(input("enter second num. : "))
z = float(input("enter third num. : "))

sum = x + y + z

if x == y and y == z:
    print (sum * 3)
else:
    print(sum)