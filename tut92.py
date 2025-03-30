#-------------------------------------
#----- practice for  error handling --
#-------------------------------------

the_file = None
the_Tries = 5
while the_Tries > 0:
    try:

        print("Enter the file name with absolute path ")
        print(f"{the_Tries} left")
        print("Example: D:\python\file.extension")
        file_name_and_bath =  input("filename => ").strip()
        the_file = open(file_name_and_bath, 'r')
        print(the_file.read())
        break

    except FileNotFoundError:
        print("file not found")
        the_Tries -= 1
    except:
        print("error happend")

    finally:
        if the_file is not None :
            the_file.close()
            print("mission is done")
else:
    print("all tries is done")

