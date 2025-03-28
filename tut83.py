#-----------------------------------------
#------ Decorator ==> Intro --------------
#-----------------------------------------


# [1] Somtime called Meta programming
# [2] Everything in python are object even function
# [3] Decorator take function and add some functionality and return it
# [4] Decorator warp other functions and enhance their behaviour
# [5] Decorator highly order function (function accept function as parameter)
#--------------------------------------------------------------------------------


def myDecorator (func):     #decorator function
    def nestedfunction ():  #any name
        print("before decoration")
        func()              # excute function
        print("after decoration")

    return nestedfunction



def sayHallo():
    print("hello Ahmed")


sayHallo()
print("#" * 50)

# first method
afterDecoration = myDecorator(sayHallo)

afterDecoration()

print("#" * 50)
#another method
@myDecorator
def sayHallo2():
    print("hello Ahmed2")


sayHallo2()