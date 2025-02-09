#------------------------------
#-----------tuple
#----------------------------------------------


# tuple with one element
my_tuple1 = ("Ahmed") #string not tuple
my_tuple = "Ahmed" #string not tuple

print(type(my_tuple1))
print(type(my_tuple))

print(len(my_tuple1))
print(len(my_tuple))


# to  make it tuple add comma

my_tuple1 = ("Ahmed",) # tuple
my_tuple = "Ahmed",    # tuple

print(type(my_tuple1))
print(type(my_tuple))

print(len(my_tuple1))
print(len(my_tuple))



#tuple concate

a = (1, 2, 3, 4,5)
b = (7,8)

c = a + b
d = a+ ("a","d", "r") + b
print(a)
print(b)
print(c)
print(d)


# tuple, list, string repeat (*)

myStping = "String"
myList = [1,2]
myTuple = ("A", "B")

print(myStping * 6)
print(myList*6)
print(myTuple * 6)




# method ===> count

z =(1, 2, 3, 1,4,5,1, 3,1)
print(z.count(1))

# method ===> index
print("The index of index: {:d}  "   .format(z.index(4)))
print(f"The index of index: {z.index(4)}  ")


# method ===> distruct
a = ("a", "b", "w",  "c")

x,v,_, n = a # under score to skip value
print(x)
print(v)
print(n)