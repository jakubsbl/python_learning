# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

n = input("Please enter any number: ")

def difference(n):
    if (int(n)) <=17:
        return 17 - (int(n))
    else:
        return ((int(n))-17) * 2
print(difference(n))
