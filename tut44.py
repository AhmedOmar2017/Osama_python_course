

print("#" *80)
print(" you can write the full name or the first letter ".center(80, "#"))
print("#" *80)

age = int(input("your age?").strip())
unit = input("choose you unit , months, weeks, or days ").strip().lower()




months = age * 12
weeks  = months * 4
days   = age * 365
hours  = days * 24
minutes = hours * 60
second = minutes * 60

if unit == "months" or unit == "m":
    print(f" you lived {months:,} months.")
elif unit == "weeks" or unit == "w":
    print(f" you lived {weeks:,} weeks.")
else:
    print(f" you lived {days:,} days.")
