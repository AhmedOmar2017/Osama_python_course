#---------------------------------------------
#----- OOP ==>  @Property Decorator ----------
#---------------------------------------------

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hallo(self):
        return f"hello {self.name}"
    @property
    def age_in_days(self):      # only return values
        return self.age *360

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hallo())
#print(one.age_in_days())

print(one.age_in_days)