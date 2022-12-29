class Base():
    def fn1(self):
        print("Calling Base Class function")

    def fnoverride(self):
        print("I am from Base Class")

class Derived1(Base):
    def fnoverride(self):
        print("I am from Derived - 1 Class.. I am overriding the function..")
class Derived2(Base):

    def fnoverride(self):
        print("I am from Derived - 2 Class.. I am overriding the function..")

class Derived3(Base):
    def fn2(self):
        print("Calling Derived-3 Class function")


one = Base()
two = Derived1()
three = Derived2()
four = Derived3()

one.fn1()
one.fnoverride()
two.fn1()
two.fnoverride()
three.fn1()
three.fnoverride()
four.fn2()
four.fnoverride()

# Output:-
# PS C:\Users\Sasikumar S\Documents\python\practice-programs\oOP's> python .\polymorphism.py
# Calling Base Class function
# I am from Base Class
# Calling Base Class function
# I am from Derived - 1 Class.. I am overriding the function..
# Calling Base Class function
# I am from Derived - 2 Class.. I am overriding the function..
# Calling Derived-3 Class function
# I am from Base Class