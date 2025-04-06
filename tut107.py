# ----------------------------------------
# -- Object Oriented Programming --------
# ----------------------------------------

# Class Attribute: Attributes define outside the constructor
# ------------------------------------------------------------

class member:
    # Attributes instance: ==>  [Outside the constructor]
    not_allowed_name = ["hell", "shit"]
    users_num = 0

    def __init__(self, firstName, lastName, gender):
        # Attributes instance:==> [inside the constructor]
        self.fName = firstName
        self.lName = lastName
        self.gender = gender
        member.users_num += 1

    def full_name(self):
        if self.fName in member.not_allowed_name:
            raise ValueError("not allowed name")
        else:
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

    def delete_user(self):
        member.users_num -= 1
        return f"user {self.fName} deleted"


print(member.users_num)

member_one = member("Mero", "Omar", "female")
member_Two = member("ahmed", "Omar", "male")
member_Three = member("amr", "Omar", "male")

print(member.users_num)

print(member_Three.delete_user())
print(member.users_num)
print(member_Two.get_all_info())