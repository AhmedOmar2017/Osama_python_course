#--------------------------------------------------------------
#---------------------- List ----------------------------------

#--------------------------------------------------------------



# [1] list items are closure in square bracket
# [2] list are ordered to use index to access
# [3] list are mutable ==>> add edit remove
# [4] list item aren't uniq
# [5] list can have different data type

##   index output type is depend on  [string, bool, int ...]
## slice  output is always string

myOsameList = ["one", "two", "one", 1, 2, 100.1, True]

print(myOsameList)

# Index
print(myOsameList[1])       # print string
print(type(myOsameList[1]))


#index from left
print(myOsameList[-1])
print(type(myOsameList[-1]))


#slice
print(myOsameList[1:4]) #print index [2,3,4]
print(type(myOsameList[1:4]))

print(myOsameList[1:2])
print(type(myOsameList[1:2]))



print(myOsameList[:4])
print(myOsameList[1:])


## steps

print(myOsameList[::1])
print(myOsameList[::2])


# Editing

print(myOsameList)
myOsameList[2] = "Ahmed"
print(myOsameList)
myOsameList[-1] = False
print(myOsameList)
myOsameList[0:2] = []
print(myOsameList)
myOsameList[0:3] = ["A", "w", "c"]
print(myOsameList)
myOsameList[0:3] = ["A"]
print(myOsameList)
