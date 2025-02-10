#-----------------------------
#--------- set --------------
#-----------------------------



# [1] set in curly bracket
# [2] set item not order not index
# [3] can't slice or indexing the set
# [4] Set has immutable Data type (number, string, tuple), list and Dic are not included
# [5] Set items are unique
#----------------------------------------------------------------------------------------




mySet = {"Ahmed", "Omar", "100"}
print(mySet)

#not slicing

mySet2 = {1,2,4,6,7,8,9,9}
#   print(mySet2[0:3])      #error

#Set has immutable Data type (number, string, tuple)

#mySet3 = {"Ahmed", 100, 100.6, True, [1,2,3]} #TypeError: unhashable type: 'list'
mySet3 = {"Ahmed", 100, 100.6, True, (1,2,3)}
print(mySet3)


# Set items are unique

mySet4 = {1,2,3,4,54, 1, "ahmed", "omar", "ahmed"} #remove repeated items
print(mySet4)