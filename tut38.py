#------------------------
#----- input function----
#------------------------


fName = input("Your first name?")
mName = input("Your middel name?")
lName = input("Your last name?")


fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()
print(f"Hello {fName} {mName :.1s} {lName}")     #.strip() to remove spaces


