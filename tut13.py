#----------------------------------------
#------ String methods--------------------


# -------------------- len() function -----------------------

a = "I love python"
b = "           I love python"
print(len(a))       # number of element  is sting include spaces
print(len(b))       # number of element  is sting include spaces



#-------------------------- strip function ----------------------------------
# strip()   remove  any character you pass to it from left and right -default is space-
# rstrip()  remove  any character you pass to it from right
# lstrip()  remove  any character you pass to it from left



c ="        I love python           "
print(c.strip())
print(c.lstrip())
print(c.rstrip())


c ="###########I love python###########"
print(c.strip("#"))
print(c.lstrip("#"))
print(c.rstrip("#"))

c ="@#@#@#@#@#I love python@#@#@#@#@#"
print(c.strip("@#"))
print(c.lstrip("@#"))
print(c.rstrip("@#"))


# ----------------------Title function ------------------
# it capitalize the first letter in each word

d = "i love python 2d and 3d model"

print(d.title())

# ----------------------Capitalize function ------------------
# it capitalize the first letter
print(d.capitalize())

#-----------------------zfill function --------------
#fill zero it is need numbers of zero

c,d,e, f = "1", "1", "111","1111"
print(c)
print(d)
print(e)


print(c.zfill(len(e)))
print(d.zfill(len(e)))
print(e.zfill(len(e)))
print(f.zfill(len(e)))

#------------------------ upper function ---------------
#  it capitalize all letters
w= "i love python"

print(w.upper())

#------------------------ lower function ---------------
#  it small all letters
q = "I LOVE PYTHON"
print(q.lower())