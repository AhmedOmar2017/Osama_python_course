#-----------------------------
#-- built in function --------
# ----------------------------
#
# abs()
# pow()
# min()
# max()
# slice()
# -----------------------------------------

 # abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#"*40)

# pow(base, exp, mod) ==> power

print(pow(2,5))  #2*2*2*2*2
print(pow(2,5,10))  # (2*2*2*2*2)%10

print("#"*40)

# min(item,item, iterate)
my = (1,10,-50,20,30)
print(min(1,10,-50,20,30))
print(min("A", "z", "Ahmed"))
print(min(my))
print("#"*40)

#max(item,item, iterate)
my2 = (1,10,-50,20,30)
print(max(1,10,-50,20,30))
print(max("A", "z", "Ahmed"))
print(max(my2))
print("#"*40)

# slice(start, end, step)
a = ["A", "B","C", "D", "E","F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
