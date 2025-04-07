#-----------------------------------------------------------
#-------Regular Expressions  Group Training's & Flags ------
# ------ https://pythex.org/ --------------------------------
#-----------------------------------------------------------


import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)",my_web)

print(search.group())
print(search.groups())

for group in search.groups():
    print(group)


print("#" * 50)
print(f"Protocol: {search.group(1)}")
print(f"Subdomain: {search.group(2)}")
print(f"domain name: {search.group(3)}")
print(f"Top level domain : {search.group(4)}")
print(f"Port : {search.group(5)}")
print(f"Query string : {search.group(6)}")


