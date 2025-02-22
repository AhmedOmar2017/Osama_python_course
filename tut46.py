#----------------------------------
#--- Practice membership ----------
#----------------------------------



# list contain admins

Admins = ["Ahmed", "Omar", "Osama", "Ali"]

#Login

UserName = input("Please input you user name").strip().capitalize()


# check if user is admin

if UserName in Admins:
    print(f"Hello {UserName} welcome back")
    option = input("Delete or edit your name?").strip().capitalize()
    print(option)
    if option == "Delete" or option == "D":
        Admins.remove(UserName)
        print("you name was deleted")
        print(Admins)
    elif option == "Edit" or option == "E":
        thNewName = input("your new  name").strip().capitalize()
        print(thNewName)
        Admins[Admins.index(UserName)] = thNewName
        print("you name is updated")
        print(Admins)
    else:
        print("you choose wrong option")
else:
    status = input("you are not admin would you join us ? y/n").strip().capitalize()
    if status == "Y" or status == "Yes":
        print("you have been add")
        Admins.append(UserName)
        print(Admins)
    else:
        print("Thanks for your time")


