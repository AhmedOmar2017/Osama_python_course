#----------------------------------
#----- For loop -------------------
#----------------------------------

numbers = [1,2,3,4,5,6,7,8,9]


for n in numbers :
    if n % 2 == 0 :
        print(f"number {n} is even")
    else:
        print(f"number {n} is odd")

else:
    print(" loop is finished")



print("#"* 40)

name = "Ahmed"

for l in name:
    print(f"[{l.capitalize()}]")