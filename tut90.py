#---------------------------------------------------
# --- Error And Expectations Raising ---------------
#---------------------------------------------------

# [1] Exceptions is a runtime Error reporting mechanism
# [2] Exceptions give you a message to understand the problem
# [3] Tracback gives you the  line to look for the in this line
# [4] Exceptions have types (Syntax error, Index error, Key error,Etc...)
# [5] Exceptions List https://docs.python.org/3/tutorial/errors.html
# [6] raise keyword used to raise your own Exceptions
#--------------------------------------------------------------------------

x = 10

if x < 0:
    raise Exception(f"The number {x} is less than Zero")
else:
    print("every things OK")

y = "Ahmed"

if type(y) != int:
    raise ValueError("only nuber allowed")
