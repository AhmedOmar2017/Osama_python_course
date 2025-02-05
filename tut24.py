#-----------------------------------
#------------ Tuple ----------------
#-----------------------------------


# [1] Tuple are enclosed in parentheses
# [2] You Can remove the parentheses if you want
# [3] Tuple is order, element to use index to access item
# [4] Tuple are immutable => you can't add or remove
# [5] Tuple item isn't unique
# [6] Tuple can have different date type
# [7] Operators can use in strings and list and available in tuple
#--------------------------------------

# tuple syntax
myAwesameTuple = ("Ahmed", "omar")
print(type(myAwesameTuple))

myAwesamTuple = "Ahmed", "omar"
print(type(myAwesamTuple))

# tuple index

print(myAwesameTuple[0])


#tuple assigned

# myAwesamTuple[0] = "Lile"     # Error


#different type
awsome = "ahmed", "omer", 1, 2, 4.4, True
print(awsome[1])
print(awsome[2])
print(awsome[-1])
print(awsome[-3])


