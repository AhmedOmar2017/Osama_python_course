# ---------String index  & slicing -------------
# [1] All data in python are objects
# [2] Object contains element
# [3] Every Element contains own index\
# [4] Python uses zero based indexing (index start from zero)
# [5] Uses square brackets to access element
# [6] Enable Access part of string, tuples, lists
# ------------------------------------------------------------

# Indexing (access single element)
myString = "I love python"
print(myString)
print(myString[0])   #Index [0] ==> 1st element ==> I
print(myString[9])   #Index [9] ==> 9th element ==> t
print(myString[-1])  #Index [1] ==> 1st element, but you count from right to left ==> n
print(myString[-6])  #Index [6] ==> 6th element, but you count from right to left ==> p

#------------------------------------------------------------------------------------------

# Slicing (Access multiple sequence items)
# [Start : End] notice end doesn't count
# [Start : End : Steps]

print(myString[8:11]) # print from y element to H element (yth)
print(myString[:10])  # If you doesn't write the start element that means you start from beginning print from I element to T element (I love pyt)
print(myString[5:])   # If you doesn't write the end element that means you complete to  the end of string print from I element to T element (e python)
print(myString[:])    # print full string (I love python)


# Slicing with steps
print(myString[0::1])    # print full string (I love python) default value of steps is one
print(myString[::1])     # print full string (I love python) default value of steps is one

print(myString[0::2])    # print element and skip one to the end string (Ilv yhn)
print(myString[0::3])    # skip two to the end string (Io tn)