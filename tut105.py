# ------------------------------------------------------------------
# --------- OOP ==> Instance Attributes and methods ---------------
# ------------------------------------------------------------------
# self: point to instance created from class
# Instance attributes:   Instance attributes defined inside the constractor
# --------------------------------------------------------------------------
# Instance method :take self parameter which point to instance created from class
# Instance method can have more than one parameter like any function
# Instance method can freely access attribute and method on the same object
# Instance method can access the class itself
# ----------------------------------------------------------------------------------

class member:
    def __init__(self, firstName, lastName):
        self.fName = firstName
        self.lName = lastName


member_one = member("Ahmed", "omar")
member_Two = member("Ali", "Omar")

print(member_one.fName, member_one.lName)
print(member_Two.fName, member_Two.lName)