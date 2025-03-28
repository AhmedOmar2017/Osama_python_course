#--------------------------------------
#------------ Generators --------------
# -------------------------------------
#
# [1] Generator is a function with "Yield" Keyword Instead of "return"
# [2] It support Iteration and return Generator Iterator By CAlling "Yield"
# [3] Generator Function can have one or more "Yeild"
# [4] By using Next() It Resume From Where it called Yeild Not from Beginging
# [5] when called, It's not start Automatically, Its Only Give You The Control
#------------------------------------------------------------------------------

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8

def myGenerator2():
    return 1


print(myGenerator())
print(myGenerator2())

print("#" * 40)

myGen = myGenerator()

print(next(myGen))

print("Hello Ahmed")
print(next(myGen))
print("Hello Ahmed")
print(next(myGen))
print("Hello Ahmed")
print(next(myGen))

print("#" * 40)

for n in myGen:
    print(n)
