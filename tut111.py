# ------------------------------------------------
# --------- OOP =>> multiple inheritance ---------
# ------------------------------------------------

# method overwrite

class food:  # based class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} is created from base class ")

    def eat(self):
        print("eat method main base class")


class Apple(food):  # drived class
    def __init__(self, name, price, amount):
        # food._init_(self, name, price)  # 1st method
        super().__init__(name, price)  # 2nd method
        self.amount = amount
        print(
            f"{self.name} is created from derived class and price is {self.price} $ and amount is {self.amount} pieces")

    def get_from_tree(self):
        print("get from tree deriven from class")

    def eat(self):  # overwrite
        print("eat method main drive class")


# food_one = food("pizze")
food_two = Apple("pizze", 150, 3)

food_two.eat()
food_two.get_from_tree()


class baseOne:
    def __init__(self):
        print("base one")

    def funOne(self):
        print("one")


class baseTwo:
    def __init__(self):
        print("base two")

    def funTwo(self):
        print("two")


class driven(baseOne, baseTwo):
    pass


my_var = driven()

print(driven.mro())

print(my_var.funOne)
print(my_var.funTwo)

my_var.funOne()
my_var.funTwo()


class base:
    pass


class derivedOne(base):
    pass


class derivedTwo(derivedOne):
    pass