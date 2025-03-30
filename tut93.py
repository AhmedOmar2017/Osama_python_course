#----------------------------------------------------
#----------------------- Debugging ------------------
#----------------------------------------------------


my_list = [1,2,3,4,5,6]
my_dictionary = {"name": "Ahmed", "Age": 31, "Country": "Egypt"}

for num in my_list:
    print(num)

for key, value in my_dictionary.items():
    print(f"{key} ==> {value}")


def function_one():
    print("hello from function one")



function_one()