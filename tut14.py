#----------------------------------------
#------------ string part2 --------------
#
#
#
#
#--------- split function ----------------
# split()
# rsplit()
# split the sentences to word and store it in list by default space
# it take to parameter
# spliter, ==> simple of spliter
#  max split  ==> number of words



a = "I love python"

print(a.split())

b = "I-love-python"
print(b.split())
print(b.split("-"))
c = "I-love-embedded-system-and-machine-learning-and-electronics"
print(c.split())
print(c.split("-"))
print(c.split("-",2))
print(c.rsplit("-",2))


#---------------------- center function ----------------------
# width==> include the word
# fillchar ==> simple -default is space-

q = "Ahmed"

print(q.center(9,"#"))
print(q.center(15,"#"))


#----------------- count function --------------------------------------
# it counts  repeated element in string
# give element you  want count
# start
# end
# case-sensitive

print(c.count("e"))
print(c.count("and"))
print(c.count("e", 2,12))



#----------------- swapcase function --------------------------------------
# swap small to capital and versa

s = "I love PYTHOn"
print(s.swapcase())

#----------------- startwith function --------------------------------------
# check if start with
# take start and end
# Return bool value

print(s.startswith("I"))
print(s.startswith("i"))

print(s.startswith("P",7, 12))


#----------------- endwith function --------------------------------------
# check if end with
# take start and end
# Return bool value


print(s.endswith("N"))
print(s.endswith("n"))

print(s.endswith("e",2, 6))