#-------------------------------------------------
#------ Data and time => format ------------------
#------------ "https://strftime.org/" ------------
#-------------------------------------------------

import datetime



my_Birthday = datetime.datetime(1993, 12,15)

print(my_Birthday)

print(my_Birthday.strftime("%A"))
print(my_Birthday.strftime("%a"))
print(my_Birthday.strftime("%b"))
print(my_Birthday.strftime("%B"))

print(my_Birthday.strftime("%d %B %Y"))
print(my_Birthday.strftime("%d-%B-%y"))
print(my_Birthday.strftime("%d/%b/%y"))