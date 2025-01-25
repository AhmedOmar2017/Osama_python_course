#-------------------------- string formatting new method



name = " Ahmed"
age  = 31
rank  = 10

print("my name is {}:" .format(name))
#print("my name is :" +name + "and my  age is:" +age ) #Error can't concat string with number
print("my name is : {}  and my  age is: {}" .format(name  , age))
print("my name is : {:s}  and my  age is: {:d} and my rank: {:.2f}" .format(name  , age, rank))

# {:s} ==> string
# {:d} ==> degit number
# {:f} ==> floating
#


# truncate string

n = "Hello there my  name is ahmed Omar and  i love programming so much"
print("welcome massage: {:s}" .format(n))
print("welcome massage: {:.5s}" .format(n))



# format money
MyMoney = 875674563422423
print("my balance is : {:d}".format(MyMoney))
print("my balance is : {:,d}".format(MyMoney))


# Rearrange item

a,b,c = 1,2,3

print("First:{}, second: {}, Third: {}".format(a,b,c))
print("First:{2}, second: {0}, Third: {1}".format(a,b,c))
print("First:{2}, second: {1}, Third: {0}".format(a,b,c))



x,y,z = 10,20, 30

print("First:{}, second: {}, Third: {}".format(x,y,z))
print("First:{2:d}, second: {0:d}, Third: {1:.2f}".format(x,y,z))
print("First:{2:f}, second: {1:d}, Third: {0:.3f}".format(x,y,z))

#format version 3.6 or above

# add f before  quote
name = " Ahmed"
age  = 31
rank  = 10
print(f"my name is : {name}  and my  age is: {age} and my rank: {rank}")