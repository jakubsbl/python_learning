# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# https://www.w3resource.com/python-exercises/python-basic-exercise-9.php


exam_st_date = (11, 12, 2014)
# print("The examination will start from : %i/%i/%i"%exam_st_date) - example from w3resource

print("The examination will start from :" + str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/" + str(exam_st_date[2]))