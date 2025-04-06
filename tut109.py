# -----------------------------------------------------
# --------------- OOP => magic method -----------------
# -----------------------------------------------------

# Every thing in python is an object
# __init__ is call automatically when instantiating class
# self.__class__ the class to which a class instance belongs
# __str__ gives a human-readable output of the  object
# __len__ return the length of the container
#         called when we called the built-in function len() function in the object
#-------------------------------------------------------------------------------------

class skills:
    def __init__ (self):
        self.skills = ["c",  "html", "cpp"]
    def __str__ (self):
        return f"this my skills => {self.skills}"

    def __len__(self):
        return len(self.skills)

profile = skills()

print(profile)
print(len(profile))
profile.skills.append("c#")
print(len(profile))


print("#"* 50)

my_string = "Osama"

print(type(my_string))

print(my_string.__class__)
print(dir(str))