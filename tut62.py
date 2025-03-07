#-------------------------------------------
#---------------- function scope -----------
#-------------------------------------------


x = 1    # Global scope



def one():
    global x
    x =4
    print(f"print globle variable from function {x}")

def Two():
    x = 2   # Local scope
    print(f"print globle variable from function {x}")



print(f"globle scope {x}")
one()
Two()
print(f"globle scope after globla X {x}")