#--------------------------------
#------ built-in function -------
#--------------------------------

# all()
# any()
# bin()
# id()

#--------------------------------

print("all function")
x = [1,2,3,4,5, []]

if all(x):
    print("All ellemrnts are true")
else:
    print("at least one element is false")

print("any function")

if any(x):
    print("at least one element is true")
else:
    print("All ellemrnts are false")

print("bin function")

print(bin(100))

a = 1
b = 2

print("id function")
print(id(a))
print(id(b))