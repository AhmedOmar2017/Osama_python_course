#------------------------------------------------------
#------ - Decorators - Practical Speed Test -----------
#------------------------------------------------------

from time import time

def myDecorator (func):     #decorator function
    def nestedfunction (*num):  #any name
        for n in num :

            if n < 0 :

                print("worng at lest one number less than zero ")
        func(*num)             # excute function
        print("after decoration")

    return nestedfunction


def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()

        print(f" running time is {end -start} ")


    return wrapper


@speedTest
def bigLoop():
    for n in range (1, 20000):
        print(n)


bigLoop()

