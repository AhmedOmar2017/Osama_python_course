#-----------------------------------
#-- built in function -filter- -----
#-----------------------------------


# [1] filter takes a function + Iterator
# [2] run a function in every  element
# [3] the function can be pre-defined or lambda
# [4] it  return all element for which the function return true
# [5] it need to return boolean value
#--------------------------------------------------------------------

def check_num (num):
    if num > 10:
        return num


my_num = [1,122,33,45,57,6,97,8,9]

myResult = filter(check_num, my_num)

for n in myResult:
    print(n)

print("#" * 50)


def check_name (name):
    return   name.startswith("O")

txt = ["Ahmed", "Omar", "mohmed"]

return_data = filter(check_name,txt)

for nam in return_data:
    print(nam)

print("#" * 50)


txt2 = ["Ahmed", "Omar", "mohmed"]

return_data2 = filter(lambda name : name.startswith("A"), txt2)

for nam in return_data2:
    print(nam)

print("#" * 50)
