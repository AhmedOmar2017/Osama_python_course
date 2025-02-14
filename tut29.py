#--------------------------------
#------------ set method --------
#--------------------------------



# issuperset()

print("is super set function")
a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}
print(a.issuperset(b)) #True
print(a.issuperset(c)) #false

print("#" * 50)

# issubset()

print("is sub set function")
print(a.issubset(b)) #false
print(a.issubset(c)) #true

print("#" * 50)

# isdisjoint()

g = {7,8,9,0}
print("is disjoint function")
print(a.isdisjoint(b)) #false
print(a.isdisjoint(g)) #true

print("#" * 50)


