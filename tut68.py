#--------------------------------------------
#------- File Handling import info ----------
#--------------------------------------------


myFile = open (r"E:\courses\Done\python_course\Elzero\Tut1\fun2.txt","a")
myFile.truncate(5) #number of bytes


print(myFile.tell())

myFile = open (r"E:\courses\Done\python_course\Elzero\Tut1\fun.txt","r")

myFile.seek(6)
print(myFile.seek(6))


import os

os.remove(r"E:\courses\Done\python_course\Elzero\Tut1\fun.txt")