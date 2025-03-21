#--------------------------------------
#----- Create your own module ---------
#--------------------------------------


import sys
print(sys.path)
sys.path.append(r"D:\Drivers ") # add path to import lib
print(sys.path)

import tut77_lib
import tut77_lib as tl      #alias for lib
from tut77_lib import Say_how_are_you
from tut77_lib import Say_how_are_you as SY
print(dir(tut77_lib))

tut77_lib.say_hello("Ahmed")
tut77_lib.say_hello("omar")
tl.say_hello("Lolo")


Say_how_are_you("Ahmed")
SY("Omar")