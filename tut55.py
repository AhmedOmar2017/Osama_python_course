#----------------------------------
#----- advanced Dictionary loop ---
# ---------------------------------


mySkill = {
    "C" : "80%",
    "cpp" : "90%",
    "c#" : "50%"
}

print(mySkill.items())

for skill in mySkill :
    print(f"{skill} => {mySkill[skill]}")

for myskill_key, myskill_val in mySkill.items():
    print(f"{myskill_key} => {myskill_val}")

print("#" * 40)


myUltimateSkills = {
    "HTML" : {
        "main" : "80%",
        "Pugjs" : "70%"
    },
    "CSS" : {
        "main" : "70%",
        "Sass" : "40%"
    }
}

for main_key, main_val in myUltimateSkills.items():
    print(f"{main_key} progress is:")

    for child_key, child_val in main_val.items():
        print(f"{child_key} => {child_val}")