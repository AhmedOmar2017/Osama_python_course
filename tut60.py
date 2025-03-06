#----------------------------------------------------
#- Function packing and unpacking, arg, **KWArgs ----
#----------------------------------------------------

def Show_mySkills(*mySkills):
    print(type(mySkills))
    for skills in mySkills:
        print(f"{skills}")

Show_mySkills("c", "cpp")


mySkills = {
    "HTML" : "90%",
    "C"    : "40%",
    "Cpp"  : "60%",
    "C#"   : "70%"
}

def Show_mySkills(**mySkills):
    print(type(mySkills))
    for skills, values in mySkills.items():
        print(f"{skills}==>>{values}")

Show_mySkills(c = "80%", cpp = "40%")

print("#"* 40)

print(mySkills)
Show_mySkills(**mySkills)   #unpacking dict