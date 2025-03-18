# ---------------------------------
# -- Built in Functions -----------
# ---------------------------------

# enumerate()
# help()
# reserved()

# -------------------------------------


# enumerate(iterable, start = 0 )

mySkill = ["c", "cpp", "c#", "python", "java"]
mySkillWithCounter = enumerate(mySkill)
for skill in mySkillWithCounter:
    print(skill)

print("#" * 40)
mySkillWithCounter2 = enumerate(mySkill, 20)
for skill in mySkillWithCounter2:
    print(skill)
print("#" * 40)

for c, s in mySkillWithCounter2:
    print(f"{c} - {s}")
print("#" * 40)

# help()

print(help(print))

print("#" * 40)

# reserved(iterable)

myString = "elzero"

for l in reversed(myString):
    print(l)