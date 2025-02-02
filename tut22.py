#--------------------------------
#----------- Lists method -------
#--------------------------------


#append()
my_friend = ["Ahmed", "omar", "EQ"]
my_friend.append("qw")
print(my_friend)


myOldFried = ["hytham", "Ali", "Mo"]
my_friend.append(myOldFried)
print(my_friend)
print(my_friend[1])
print(my_friend[2])
print(my_friend[3])
print(my_friend[4])
print(my_friend[4][2])


#Extend()

a = [1,2,3,5]
b = ["a", "b", "c"]

print(a)
a.extend(b)
print(a)


#remove

my = ["Ahmed", "omar", "EQ", "EQ"]
print(my)
my.remove("EQ")
print(my)


#sort       numbers or string one kind of them
num = [2,5,1,4,2,56,23]
print(num)
num.sort() # default
print(num)
num.sort(reverse = True)
print(num)


#reverse  reverse list numbers and string -mixed-

num = [2,5,1,4,2,56,23, "Ahmed"]
print(num)
num.reverse()
print(num)
