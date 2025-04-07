# -------------------------------------------
# ----- OOP ==> Getter and setter ----------
# ------------------------------------------


class Member:
    def __init__(self, name):
        self.__name = name

    def say_hallo(self):
        return f"hello {self.__name}"

    def get_func(self):  # getter
        return self.__name

    def set_func(self, newName):  # setter
        self.__name = newName


one = Member("Ahmed")
print(one.get_func())
one.set_func("Osama")
print(one.get_func())