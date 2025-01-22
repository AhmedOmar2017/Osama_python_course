#-----------------------------replace()--------------------------
# replace (old value, new, count)



a = "Hello one Two  one three one"
print(a)
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))

#-----------------------------join()--------------------------
# iterable
# takes list and return one string
#"separator"join(variable)


my_list = ["ahmed", " ", "Omar"]

print(my_list)
print("-".join(my_list))