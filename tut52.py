
#range
myRange = range(1,100)

for n in myRange:
    print(n)


#Dectionary

mySkills ={
    "c"      : "90%",
    "cpp"    : "80%",
    "c#"     : "70%",
    "css"    : "50%",
    "python" : "70%"
}

print(mySkills["css"])
print(mySkills.get("css"))

for skill in mySkills:
    print(f"My progress in {skill} is {mySkills[skill]} ")