# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# https://www.w3resource.com/python-exercises/python-basic-exercise-10.php

#a = int(input("Input an integer : ") )
#n1 = int ( "%s" % a )
#n2 = int ( "%s%s" % (a,a) )
#n3 = int ( "%s%s%s" % (a,a,a) )
#print ("The sum of the addition of your integer(n) in format n + nn + nnn is: ")
#print (n1+n2+n3)
###################################### EDIT ->

a = input("Input an integer : ")
n1 = (a)
n2 = (a*2)
n3 = (a*3)


print ("The sum of the addition of your integer(n) in format n + nn + nnn is: ")
print (int(n1)+int(n2)+int(n3)) 
