#--------------------------------
#------- Break, continue, pass --
#--------------------------------


myNumber = [1,2,3,4,5,6,18,7,8,9,10, 13, 14, 15]

# continue
for n in myNumber:
    if n == 13 :
        continue
    print(n)

print("#" * 40)
#Break
for n in myNumber:
    if n == 13 :
        break
    print(n)

print("#" * 40)
# pass

for n in myNumber:
    if n == 13 :
        pass
    print(n)

print("#" * 40)