#------------------------------
#------- Method two -----------
#------------------------------


# Differance()

a = {1,3,45,565,65,7}
b = {1,3, "Ahmed", "Omar"}

print(a)
print(a.difference(b))  # a-b
print("#"  * 40)


#Differance_update()


d = {1,3,45,565,65,7}
w = {1,3, "Ahmed", "Omar"}

print(d)
d.difference_update(w)
print(d)
print("#"  * 40)

#intersection


q = {1,3,45,565,65,7}
e = {1,3, "Ahmed", "Omar"}
print(q)
print(q.intersection(e))    # q & e
print("#"  * 40)


# Intersection_update()

t = {1,3,45,565,65,7}
r = {1,3, "Ahmed", "Omar"}

print(t)
t.intersection_update(r)
print(t)
print("#"  * 40)


# Symmetric_differance()
q = {1,3,45,565,65,7}
e = {1,3, "Ahmed", "Omar"}
print(q)
print(q.symmetric_difference(e))  # q ^ e
print("#"  * 40)



# Symmetric_differance_update()
t = {1,3,45,565,65,7}
r = {1,3, "Ahmed", "Omar"}

print(t)
t.symmetric_difference_update(r)
print(t)
print("#"  * 40)





