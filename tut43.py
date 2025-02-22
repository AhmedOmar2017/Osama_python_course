#----------------------------------------
#----- Ternary Conditional operator------
#----------------------------------------

# Write the condition in the same line


Country = "A"

if Country == "A" : print("is egypt")
else: print("is not egypt")

movieRate = 18
age = 16

if age < movieRate :
    print("movie is n't good for you ")
else:
    print("movie is suit you happy watch")

print("movie is n't good for you " if age < movieRate else "movie is suit you happy watch")