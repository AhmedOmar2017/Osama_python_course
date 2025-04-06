#------------------------------------------------------------------
# --------- OOP ==> Instance Attributes and methods ---------------
#------------------------------------------------------------------
# self: point to instance created from class
# Instance attributes:   Instance attributes defined inside the constractor
# --------------------------------------------------------------------------
# Instance method :take self parameter which point to instance created from class
# Instance method can have more than one parameter like any function
# Instance method can freely access attribute and method on the same object
# Instance method can access the class itself
# ----------------------------------------------------------------------------------

class member:
    def __init__ (self, firstName, lastName, gender):
        self.fName = firstName
        self.lName = lastName
        self.gender = gender

    def full_name(self):
        return f"{self.fName}, {self.lName}"
    def nameWithTitle(self):
        if self.gender == "male":
            return f"Hello Mr {self.fName}"
        elif self.gender == "female":
            return f"Hello Miss {self.fName}"
        else:
            return f"hello {self.fName}"
    def get_all_info(self):
        return f"{self.nameWithTitle()}, your Full Name is: {self.full_name()}"


member_one = member("Ahmed", "omar","male")
member_Two = member("Mero", "Omar","female")

print(member_one.full_name())
print(member_one.nameWithTitle())
print(member_Two.nameWithTitle())
print("#" *40)
print(member_Two.get_all_info())