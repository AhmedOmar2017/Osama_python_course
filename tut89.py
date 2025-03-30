#------------------------------------------------------
#-------- Installing and use pylint for better code ---
#------------------------------------------------------

# [1] command line: pylint.exe E:\courses\Done\python_course\Elzero\Tut1\tut89.py
# [2] it ask for general documentation
# [3] specific Doc for each function
# [4] snake case for the name of function


"""
This function to say Hello
pram name  your name
"""
def say_hallo(name):
    ''' it's only say hallo'''
    msg =  "Hello"

    return f"{msg} , {name}"


print(say_hallo("Ahmed"))
