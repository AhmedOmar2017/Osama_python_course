#-----------------------------------------------------
#--------  Decorators - Function With Parameters -----
#-----------------------------------------------------

def myDecorator (func):     #decorator function
    def nestedfunction (num1, num2):  #any name
        if num1 < 0 or num2 < 0 :

            print("worng at lest one number less than zero ")
        func(num1, num2)             # excute function
        print("after decoration")

    return nestedfunction

def myDecorator2 (func):     #decorator function
    def nestedfunction (num1, num2):  #any name

        print("decrotator 2 ")
        func(num1, num2)             # excute function


    return nestedfunction

@myDecorator
@myDecorator2
def calac (a1, a2):
    print(a1 + a2)

calac(3,4)

calac(-3,4)