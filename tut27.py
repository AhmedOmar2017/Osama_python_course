#----------------------------------------------


#clear()
a ={1,2,4}
a.clear()
print(a)


#union
d = {324,46,56,5,767,6}
b = {5,7,6,8,9,9}
q = {"Ahmed", "qw"}

print(d | b)
print(b.union(d,q))

#Add
print(b)
b.add(2)
print(b)

#copy()
e= {2,3,45,5,6}

f = e.copy()
print(f)
print(e)


e.add(76)

print(f)
print(e)


#Remove

g = {12,243,43,46,56,7,6}
print(g)
g.remove(12)
print(g)

#discard
# differance is, it doesn't give error with unavailable number

print(g)
g.discard(1000)
print(g)

#pop
# random value from list
print(g.pop())


#update()
#like union
j = {23, 434,545,6575,7,87}
k = {12,34,6,676,8,798,9}
j.update(["as","asd"])
j.update(k)
print(j)
