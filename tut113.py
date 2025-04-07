#--------------------------------------
#----- OOP ==> Encapsulation ----------
#--------------------------------------
# Encapsulation
# Restrict access to the data stored in attributes and methods
# Public
# every attribute and method that we used far is public
# Attribute and methods can be modified and run from everywhere
# Inside our outside the class
# Protected
# Attributes and methods can be accessed from within the class and subclasses
# Attributes and methods prefixed with one underscore _
# Private
# Attributes and methods can be accessed from within the class or object only
# Attributes and methods can't be modified from outside the class
# Attributes and methods prefixed with one underscore __
#-----------------------------------------------------------------------------
# Attributes = Variables = Properties
#-------------------------------------

# protected

# class Member:
#     def __init__(self, name):
#         self._name = name

# one  = Member("Ahmed")

# print(one._name)


# one._name = "Osama"
# print(one._name)

#====================================================

# Private
class Member:
    def __init__(self, name):
        self.__name = name
    def say_hallo(self):
        return f"hello {self.__name}"

one  = Member("Ahmed")

print(one.say_hallo())
print(one._Member__name)
#print(one.__name)