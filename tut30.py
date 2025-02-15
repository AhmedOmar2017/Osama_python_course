#-------------------------------
#------------- Dictionary ------
#-------------------------------
from Tut1.tut15 import three

# [1] Dict item are enclosed in curly braces
# [2] Dict Contain  key and value
# [3] Dict Key have to be Immutable =>> (number, string, tuple) not list
# [4] Dict value can have any type of data
# [5] Dict key have to be unique
# [6] Dict is not ordered you can access only by key
#-------------------------------------------------------------------------


user = {
    "name"    : "Ahmed",
    "age"     : "31",
    "country" : "Egypt",
    "skills"  : ["html", "embedded", "PCB"],
    "Rating"  : 10.5

}

print(user)
print(user["country"])
print(user.get("country"))

print(user.keys())
print(user.values())


# Dictionary in two dimension

language = {
    "one": {
        "name" : "c",
        "progress" : "%80"
    },
    "two" : {
        "name" : "python",
        "progress" : "90%"
    },
    "three" : {
        "name" : "Cpp",
        "progress" : "90%"
    },
}

print(language)
print(language["one"])
print(language["three"]["progress"])


#Dictionary length
print(len(language))
print(len(language["two"]))


#create Dict from variables
framWorkOne = {
    "name" : "Vuejs",
    "progresss": "80%"
}

framWorktwo = {
    "name" : "reactjs",
    "progresss": "80%"
}

framWorkthree = {
    "name" : "anguler",
    "progresss": "80%"
}

allFram = {
    "one" : framWorkOne,
    "two" : framWorktwo,
    "three" : framWorkthree
}

print(allFram)