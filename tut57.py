#-------------------------------------------
#----- function pramaters and return -------
#-------------------------------------------




a,b,c = "Ahmed", "omar", "Abouelhassan"

print(f"hello {a}")
print(f"hello {b}")
print(f"hello {c}")

print("#"*40)


# def                    =>>> function keyword [define]
# say_hello()            =>>> function name
# name                   =>>> parameter
# print(f"hello {name}") =>>> Task
# say_hello(a)           =>>> a is the argument


def say_hello(name):
    print(f"hello {name}")

say_hello(a)
say_hello(b)
say_hello(c)


print("#"*40)



def addition(n1,n2):
    if type(n1) != int or type(n2) != int:
        print("intger only")
    else:
        print(int(n1) + int(n2))


addition(100,200)
addition(234, 456)
addition(-30, 50)
addition(-30, "Osama")


def full_name(first, middle, last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()} ")


full_name("Ahmed", "Omar", "Abouelhassan")