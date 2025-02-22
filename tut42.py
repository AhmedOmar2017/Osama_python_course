#--------------------------------------
#---------- make decision -------------
# --------- If and elseif -------------
#--------------------------------------
from platform import uname

uName = input("hello there please input your name==>").strip().capitalize()
uCountry = input("hello there please input your country==>").strip().capitalize()
isStudent = input("are you student ==>").strip().capitalize()
cName = "Python Course"
cPrice = 100


if uCountry == "Egypt" or uCountry == "Ksa":
    print(f"Hello {uName} because You are from {uCountry}")
    if isStudent == "Yes":
        print(f"The course \"{cName}\" price is : ${cPrice-90}")
    else:
        print(f"The course \"{cName}\" price is : ${cPrice-80}")

else:
    print(f"Hello {uName} because You are from {uCountry}")
    print(f"The course \"{cName}\" price is : ${cPrice - 30}")