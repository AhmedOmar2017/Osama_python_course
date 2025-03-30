#---------------------------------------
#---------- Exceptions Handling --------
#--------Try | Except | Else | Finally -
#---------------------------------------
# Try => test the code for errors
# Except => Handle the errors
#----------------------------------------
# Else => If not errors
# Finally => Run the code
#----------------------------------------


try:    #test the code for errors
    num = int(input("Writeyourage: "))
except: # handle the error if it found
    print("This is not integer")
else: #if there are no errors
    print("everything's OK")
finally:
    print("print finally whatever happens")


try:
   # print(10/0)
    print(X)

except ZeroDivisionError:
    print("Can not divide")
except NameError:
    print("identifier not found")
except:
    print("error happened")
