# ------------------------------------------------------
# ---- Function Packing, unpacking Argument *arg -------
# ------------------------------------------------------


print(1, 2, 3, 4)
myList = [1, 2, 3, 4]

print(myList)
print(*myList)  # unpacking


def say_hallo(n1, n2, n3, n4):
    people = [n1, n2, n3, n4]
    for name in people:
        print(f"hello {name}")


say_hallo("Ahmed", "Omar", "abo", "hassan")


def say_hallo2(*people):  # unpacking
    for name in people:
        print(f"hello {name}")


say_hallo2("Ahmed", "Omar", "abo", "hassan")


def show_details(skill1, skill2, skill3):
    print(f"Hello Ahmed your skills is: {skill1}")
    print(f"Hello Ahmed your skills is: {skill2}")
    print(f"Hello Ahmed your skills is: {skill3}")


show_details("c", "cpp", "c#")


def show_details2(*skill):
    print(f"Hello Ahmed your skills is: {skill}")


show_details2("c", "cpp", "c#")