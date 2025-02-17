#-----------------------------------
#----------- data conversion -------
#-----------------------------------

# str()






#str()
a = 10
print(type(a))
print(type(str(a)))

print("#" * 40)


# tuple()

c = "Osama"                     #string
d = [1,2,3,4,5]                 # List
e = {"A", "B", "C"}             # Set
f = {"A": 1, "B": 2, "C":3}     # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print("#" * 40)


# List()

c = "Ahmed"                     #string
d = (1,2,3,4,5)                 # tuple
e = {"A", "B", "C"}             # Set
f = {"A": 1, "B": 2, "C":3}     # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 40)

# set()

c = "Osama"                     #string
d = [1,2,3,4,5]                 # List
e = ("A", "B", "C")             # tuple
f = {"A": 1, "B": 2, "C":3}     # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("#" * 40)

# dict()

#c = "Osama"                     #string you can't convert string to dictionary
# all type most be  nested to convert to dictionary

d = [["A",1],["B",2]]               # List
e = (("A",1), ("B",2), ("C",3))     # tuple
#f = {{"A",1}, {"B",2}, {"C",3}}     # set error  TypeError: unhashable type: 'set'


print(dict(d))
print(dict(e))
#print(dict(f))

print("#" * 40)
