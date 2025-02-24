#-------------------------------------
#----------Loop while ----------------
#------ Practice bookmarks------------
#-------------------------------------

# an empty list to fill later
myFavoriteItweb = []

# Maximum Allowed websites

maximumAllowedWebsite = 5

while maximumAllowedWebsite > 0 :

    #Add the new website to the list
    web = input("website name without http://")
    myFavoriteItweb.append(f" http://{web.strip().lower()}.com  ")

    #decount
    maximumAllowedWebsite -= 1

    print(f"Your website were added, remind is {maximumAllowedWebsite}")


    print(myFavoriteItweb)


else:
    print("yourbookmark is full")


# check if the list is empty

if  len(myFavoriteItweb) > 0:
    # sort the list
    myFavoriteItweb.sort()
    print("waiting i will print the sorted list")
    index = 0
    while index < len(myFavoriteItweb) :
        print(myFavoriteItweb[index].center(40, "#"))
        print("#" * 40)
        index += 1

