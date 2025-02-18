#-----------------------------------------
#----- Practical your age Full detailed---
#-----------------------------------------



age = int(input("your age?").strip())

months = age * 12
weeks  = months * 4
days   = age * 365
hours  = days * 24
minutes = hours * 60
second = minutes * 60

print('You Lived for: ')
print(f"{months} months.")
print(f"{weeks:,} weeks.")
print(f"{days:,}days.")
print(f"{hours:,} hours.")
print(f"{minutes:,} minutes.")
print(f"{second:,} seconds.")