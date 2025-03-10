#--------------------------------------------------
#---- File handling => write and append in File ---
#--------------------------------------------------


myFile = open (r"E:\courses\Done\python_course\Elzero\Tut1\Ahmed2.txt","w")
myFile.write("Hello from python file with love\n")
#myFile.write("Second line")
myFile.write("third line")

myFile2 = open(r"E:\courses\Done\python_course\Elzero\Tut1\fun.txt", "w")
myFile2.write("Ahmed omar" * 1000)

myList = ["Osama", "Ahmed", "Omar"]

myFile3 = open(r"E:\courses\Done\python_course\Elzero\Tut1\fun2.txt", "w")
myFile3.writelines(myList)

myFile = open (r"E:\courses\Done\python_course\Elzero\Tut1\Ahmed2.txt","a")

myFile.write("Third Line\n")