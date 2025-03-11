#-------------------------------------------
#------ built in function part two ---------
#-------------------------------------------

# sum()
# round()
# range()
# print()

#--------------------------------------------


print("sum function")

a = [1,2,3,5,6,7,8]

print(sum(a))
print(sum(a,40))
print("#" * 40)


print("round function")
# round(number, number of digit)
print(round(150,459))
print(round(150.459, 2))
print("#" * 40)

print("range function")
#range(start,end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0,20, 2)))
print("#" * 40)

print("print function")
#print(string, separator)

print("Hello" "ahmed" "welcome" "in" "python" "course")
print("Hello", "ahmed", "welcome", "in", "python", "course", sep = "@")

print("first line", end  = " ")
print("second line", )
print("#" * 40)