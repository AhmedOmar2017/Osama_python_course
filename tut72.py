#--------------------------
#-- built in function -----
#--------------------------


# [1] Map take a function + iteration
# [2] it called map because it map the function in every element
# [3] The function it can pre-defined function or lambda function
#-----------------------------------------------------------------

# [1] using the map in pre-define function
def formtext(text):
    return  f" - {text.strip().capitalize()}-"


my_txt = ["Ahmed", "Omar", "abou"]

myFormatData = map(formtext,my_txt)
print(myFormatData)

for name in myFormatData:
    print(name)


print("#"* 40)

for name in map(formtext,my_txt):
    print(name)


print("#"* 40)


#use map with lambda function

for name in list(map(lambda txt: f" - {txt.strip().capitalize()}-",my_txt)):
    print(name)