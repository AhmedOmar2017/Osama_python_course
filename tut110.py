# -----------------------------------------------------
# --------------- OOP => Inheritance ------------------
# -----------------------------------------------------

class food:  # based class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} is created from base class ")

    def eat(self):
        print("eat method main base class")


class Apple(food):  # driven class
    def __init__(self, name, price, amount):
        # food._init_(self, name, price)  # 1st method
        super().__init__(name, price)  # 2nd method
        self.amount = amount
        print(
            f"{self.name} is created from derived class and price is {self.price} $ and amount is {self.amount} pieces")

    def get_from_tree(self):
        print("get from tree driven from class")


# food_one = food("pizze")
food_two = Apple("pizza", 150, 3)

food_two.eat()
food_two.get_from_tree()