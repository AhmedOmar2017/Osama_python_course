#-----------------------------
#--- File handling part2------
#-----------------------------

myFile = open ("E:\courses\Done\python_course\Elzero\Tut1\Ahmed.txt","r")

print(myFile)
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)


print(myFile.read())
print(myFile.read(5))

print(myFile.readline(10)) #start from line 10

print(myFile.readline())


print(myFile.readlines())

for ine in myFile:
    print(line)
    if line.startwith("07"):
        break