#----------------------------------
#--- File handling ----------------
#----------------------------------
# "a" ===> append   open file for appending Values, create if not exist
# "r" ===> read     [Default value] open file for read and give error if file not exist
# "w" ===> write    open file for writing, create file if not exists
# "x" ===> Create   Create file, give error if file exists
#----------------------------------------------------------------------------------------------

import os
print(os.getcwd())      # get current working directory

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))          # change directory


file = open(r"E:\courses\Done\python_course\Elzero\Tut1\Ahmed.txt", "x")    # "r" before bath denote for act the path between quotation as one  string  ignore any special character


