#-------------------------------------
#------- Modules => Build in ---------
#-------------------------------------

# [1] Module is A File contain A set of functions
# [2] You can import module in your App to help you
# [3] you can import modules multiple times
# [4] You Can create your own modules
# [5] Modules saves your time
#----------------------------------------


import  random

print(f"print random float value {random.random()}")

#show all function inrandom
print(dir(random))

from random import randint, randrange, random

print(f"print random intger value {randint(100, 900)}")
print(f"print random float value {random()}")