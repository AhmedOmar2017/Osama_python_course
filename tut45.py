#########################
# not in
# in
#########################

#string

name = "Ahmed"
print("e" in name)
print("a" in name)
print("A" in name)
print("#" * 40)
List = ["Ahmed", "Omar", "hassan"]

print("Ahmed" in List)
print("Omar" in List)
print("hassan"not in List)


# use in in condition

Count1 = ["Egypt", "Ksa", "Kuwait" ]
discount1 = 80
Count2 = ["Usa", "UK"]
discount2 = 50

myCount = "Egypt"

if myCount in Count1 :
    print(f"you discount {discount1}")

elif myCount in Count2 :
    print(f"you discount {discount2}")
else:
    print("you don't have discount")