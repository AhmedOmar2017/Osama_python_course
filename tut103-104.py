#--------------------------------------------------------------
#------------ Object oriented programming ---------------------
#--------------------------------------------------------------

# [01] Class is the blueprint or constructor of the object
# [02] Class instantiate means create instance of A class
# [03] Instance ==> Object created from class and their methods and attributes
# [04] Class Defined with keyword class
# [05] class name written with PascalCase [upperCamelCase] style
# [06] Class may contain method and attributes
# [07] when  creating object python look for the built-in function  __init__ method
# [08] __init__ method called every time you create object from class
# [09] __init__ method is initialized the data for the object
# [10] any method with two underscore in the start and end called dunder or magic method
# [11] Self refer to the current instance created from class and must be first param
# [12] self can be any name.
# [13] In python you don't need to call new() keyword to create object
# ----------------------------------------------------------------------

# Syntax
# Class name:
#       Constructor => Do Instantiation [create instance from class]
#       Each instance is separate object
#       def __init__ (self, other date)
#       body function
#
class member:
    def __init__(self):
        print(" A new member has been added ")


member_one = member()
member_two = member()
member_three = member()
print(dir(member))

print("#" * 50)
print(member_one.__class__)
