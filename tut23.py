#----------------------------------
#---------- Method three ----------
#----------------------------------



#clear()

a =[1,2,3,4]
print(a)
a.clear()
print(a)

#-------------------------------

#copy()
b =[1,2,3,4,5,6,]
print(b)
c = b.copy()
print(b)    # main list
print(c)    # copy list shadow copy

b.append(5)

print(b)    # main list
print(c)    # copy list

#------------------------------------

# count() count repeated number

d =[1,2,3,4,5,6,5,5,5,6,676,76,767,5]
print(d.count(5))

# index() find the index of element

e = ["Ahmed", "Omar", "new", "as"]
print(e.index("Omar"))

#--------------------------------------

# insert()

qd =[1,2,3,4,5,6,5,5,5,6,676,76,767,5]
print(qd)
qd.insert(0,23)
print(qd)
qd.insert(-1,23)
print(qd)

#------------------------------------------


# pop() element in this index

g =[1,2,3,4,5,6,5,5,5,6,676,76,767,5]
print(g.pop(6))
print(g.pop(-2))

#-------------------------------------