#---------------------------------------------
#---- Lambda function ------------------------
#---------------------------------------------
from types import LambdaType


# [1] It has no name
# [2] You can call it inline without definition
# [3] You can use it in return another function
# [4] Lambda used for Simple Functions and def Handle The large Tasks
# [5] Lambda is a single line not a block of code
# [6] Lambda Type is function

#-----------------------------------------------

def say_hello(name, age) : return f"Hello {name} you age {age}"

hello = lambda name, age : f"Hello {name} you age {age}"

print(say_hello("Ahmed", 31))
print(hello("Ahmed", 31))

print(type(hello))

print(say_hello.__name__)
print(hello.__name__)