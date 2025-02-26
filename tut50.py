#------------------------------
#--- Check the password--------
#-------------------------------


Tries = 4

Correct_password = "Ahmed"

password = input("enter you password please: ")

while password != Correct_password :

    Tries -= 1
    print(f"wrong password, {"last" if Tries == 0 else Tries} reminds")

    password = input("enter you password please: ")

    if Tries ==0 :
        print("all tries is finished")
        break

else:
    print("Correct password")