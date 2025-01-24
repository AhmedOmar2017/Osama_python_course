#-------------------------- string formatting old way




name = " Ahmed"
age  = 31
rank  = 10

print("my name is :" +name)
#print("my name is :" +name + "and my  age is:" +age ) #Error can't concat string with number
print("my name is : %s  and my  age is: %d" %(name  , age))
print("my name is : %s  and my  age is: %d and my rank: %.2f" %(name  , age, rank))

# s ==> string
# d ==> degit number
# f ==> floating
#


# truncate string

n = "Hello there my  name is ahmed Omar and  i love programming so much"
print("welcome massage: %.5s" % n)