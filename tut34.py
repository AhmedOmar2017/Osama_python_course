#-----------------------------------
#------- operation in boolean -----
#----------------------------------
# and &
# or
# not

#------------------------------------


age = 31
country = "Egypt"
rank = 10
print(age > 16)
print(country == "Egypt")


print(age > 16 and country == "Egypt")
print(age > 16 and country == "Egypt" and rank > 20)
print(age > 16 and country == "Egypt" and rank < 20)
print("#" *40 )

print(age > 16 or country == "Egy")
print(age > 16 or country == "Egypt" or rank > 20)
print(age > 16 or country == "Egypt" or rank < 20)
print("#" *40 )

print(age > 16)
print(not  age > 16)
print("#" *40 )




