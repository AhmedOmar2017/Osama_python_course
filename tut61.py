#-------------------------------------------------------------
#- Function packing and unpacking, arg, **KWArgs training ----
#-------------------------------------------------------------



mySkills = {
    "HTML" : "90%",
    "C"    : "40%",
    "Cpp"  : "60%",
    "C#"   : "70%"
}

mytuple = ["Css", "Cpp", "C#"]

def Show_skills(name, *skills, **skillswithProgress):
    print(f"Hello{name} \n Skills without progress is:")
    for skill in skills:
        print(f"-{skill}")
    print("skills with progress is: ")
    for skill , value in skillswithProgress.items():
        print(f" Skills is {skill} and progress is {value}")

Show_skills("Ahmed", "HTML", python = "50%")

print("#" * 40)
Show_skills("Ahmed", *mytuple, **mySkills)