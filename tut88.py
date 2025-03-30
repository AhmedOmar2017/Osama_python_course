#-----------------------------------------------
#--- Doc String & Commenting vs Documenting ----
#-----------------------------------------------


# [1] Documentation String for class, Module or function
# [2] Can be access from the help and doc Attributes
# [3] made to understand the functionality of the complex code
# [4] There are two mode single line and multiple lines
#------------------------------------------------------------------------

def AhmedFunction(name):
    ''' This function to say my name is '''         # single Documentation
    print(f"My name is {name}")

AhmedFunction("Ahmed")

def AhmedFunction2(name):
    # multiple Documentation
    """
    Ahmed function2
        it gives you a hand
        pram ==> name your name
        return ==> Helping massage
    """
    print(f"Hello {name} can i help you")



print(AhmedFunction.__doc__)
help(AhmedFunction)
print("#"* 50)
print(AhmedFunction2.__doc__)
help(AhmedFunction2)
