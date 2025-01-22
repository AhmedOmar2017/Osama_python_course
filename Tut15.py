#-------------------- string method 2 ----------------
#
#
#
#------------ index function
# it take three param
# element you want index
# start
# end
from codecs import xmlcharrefreplace_errors

a = " I love python"
print(a.index("p"))
print(a.index("p", 0,10))
#print(a.index("p", 0,5)) # it gives  error


#---------------------- find function ----------
# it take three param
# element you want index
# start
# end
# main differance is, if index isn't between  start and end it not give error it gives (-1)

print(a.find("p"))
print(a.find("p", 0,10))
print(a.find("p", 0,5))



#---------------------- l,rjust function ----------
# width
# char fill default char is space

c = "Ahmed"

print(c.rjust(10))
print(c.ljust(10, "#"))
print(c.rjust(10, "#"))



#---------------------- splitlines function ----------
# return lines in list


e = """ First line
second line
third line
"""

print(e.splitlines())
print(type(e.splitlines()))


f = "newline1 \n newline2 \n newline3"
print(f.splitlines())


#------------------------------ expandtabs function
# repeat tabs according the given numbers

w = "hello \t I \t love \t python"

print(w.expandtabs(2))
print(w.expandtabs(5))


#-----------------------------istitle()--------------------------
# is scan is word title or not


one  ="I Love Python 3G"
two = "I Love Python 3g"

print(one.istitle())
print(two.istitle())


#-----------------------------ispace()--------------------------


three = " "
four = ""
print(three.isspace())
print(four.isspace())


#-----------------------------islower()--------------------------

five = "i love python"
six =  "I Love Python"

print(five)
print(five.islower())
print(six)
print(six.islower())



#-----------------------------islower()--------------------------
# it can check is element can be a variable

q = "ahmed_python"
w = "lolAhmed"
r = "ahmed--omar"

print(q)
print(q.isidentifier())
print(w)
print(w.isidentifier())
print(r)
print(r.isidentifier())


#-----------------------------isalpha()--------------------------
# check is alpha
x = "aaaqqqqw"
y = "qaaaaaaaaadsdd21"


print(x)
print(x.isalpha())
print(y)
print(y.isalpha())


#-----------------------------isalnum()--------------------------
# check is alpha and num


j = "aaaqqqqw"
i = "qaaaaaaaaadsdd21"


print(j)
print(x.isalnum())
print(i)
print(i.isalnum())