#---------------------------------------------------
#-------- OOP ==> ABCs ------ abstract base class---
#---------------------------------------------------

# class called abstract class if it has one or more abstract methods
# abc module in python provides infrastructure for defining custom abstract base classes
# by adding @abstractmethod decorator on the methods
# ABCMeta class is a mataclass used for defining abstract base class
#-----------------------------------------------------------------------------------------

from abc import ABCMeta,abstractmethod

class programming(metaclass = ABCMeta):
    @abstractmethod
    def has_oop (self):
        pass
    @abstractmethod
    def has_name(self):
        pass

class python (programming):
    def has_oop(self):
        return "Yes"

    def has_name(self):
        return "python"


class pascal (programming):
    def has_oop(self):
        return "no"

    def has_name(self):
        return "python"

one =python()
print(one.has_oop())
print(one.has_name())