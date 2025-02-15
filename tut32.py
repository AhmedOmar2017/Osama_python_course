#------------------------------
#--- Dictionary method two-----
#------------------------------
from xml.sax.handler import property_interning_dict

from Tut1.tut31 import member

# setdefault()

usr = {
    "name" : "Ahmed"

}

print(usr)
print(usr.setdefault("name" ,  "Mohamed"))


print("#" * 40)


# popitem()
member = {
    "name": "Ahmed",
    "skill" : "chess"
}

print(member)
member.update({"age": 31})
print(member.popitem())

print("#" * 40)

# items()
view = {
    "name" : "osama",
    "skill": "Xbox"
}

allitems = view.items()
print(allitems)
view["age"] = 31
print(allitems)
print("#" * 40)

# from keys()

a = ("keyOne", "KeyTwo", "KeyThree")
b = "X"

print(dict.fromkeys(a, b))
print("#" * 40)