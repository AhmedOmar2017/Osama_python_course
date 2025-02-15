#----------------------------------
#-------- Dictionary method -------
#----------------------------------


# clear()

user = {
    "name" : "Ahmed"

}
print(user)
user.clear()
print(user)

print("#"*50)
# update()

member = {
    "name" : "osama"
}

print(member)
member["age"] = 31
member.update({"address":"cairo"})
print(member)

print("#"*50)


# copy()
main = {
    "name" : "Ahmed"
}
b = main.copy()
main.update({"skill": "play"})
print(main)
print(b)
print("#"*50)