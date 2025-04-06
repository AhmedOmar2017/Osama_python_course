# -----------------------------------------------------
# ----- OOP => Class methods & static method ----------
# -----------------------------------------------------

# class methods:
# marked with @classmethod decorator to flag it as class
# it take Cls- parameter not  self to the class not the instance
# It doesn't require to create of a class instance
# Used when you want to do something with the class itself
# Static methods:
#   It takes no parameters
#   its bound to the class not instance
#   Used when doing something doesn't have access to object or class but related to class
# -----------------------------------------------------------------------------------------------

class member:
    # Attributes instance: ==>  [Outside the constructor]
    not_allowed_name = ["hell", "shit"]
    users_num = 0

    @classmethod
    def show_user_count(cls):
        print(f"we have {cls.users_num} users in our system")

    @staticmethod
    def say_hallo():
        print("hello from static method")
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

print("#" * 50)

member.show_user_count()
print("#" * 50)
member.say_hallo()