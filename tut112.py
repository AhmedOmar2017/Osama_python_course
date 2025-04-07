# ------------------------------------------------
# --------- OOP =>> polymorphism  ----------------
# ------------------------------------------------


class A:
    def do_something(self):
        print("from class A")

        raise NotImplementedError("derived class must implement this method")


class B(A):
    def do_something(self):
        print("from class B")


class C(A):


 def do_something(self):
   print("from class c")


My_Instance = B()
My_Instance.do_something()

My_Instance = C()
My_Instance.do_something()