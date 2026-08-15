# 1) Import `ABC` and `abstractmethod` from the `abc` module.
#    (These are used to create abstract base classes in Python.)
from abc import ABC, abstractmethod
# 2) Create an abstract base class named `Absclass` that inherits from `ABC`.


class Absclass(ABC):
    def XYZ(self, x):
        print(x)

    @abstractmethod
    def task(self):
        print("Inside Base Class")


class test_class(Absclass):
    def task(self):
        print("Inside test class")


# test_obj = Absclass()
test_obj = test_class()
test_obj.XYZ(10000)
test_obj.task()
# 3) Inside `Absclass`, define a normal method `print(self, x)`:
#    a) It takes a value `x` as input.
#    b) It prints the value passed to the method.

# 4) Define an abstract method `task(self)` using the `@abstractmethod` decorator:
#    a) This method must be implemented (overridden) in any child class.
#    b) The print statement inside shows what the base version contains.

# 5) Create a subclass named `test_class` that inherits from `Absclass`.

# 6) Implement the abstract method `task(self)` inside `test_class`:
#    a) Print "We are inside test_class task".
#    (This satisfies the abstract method requirement.)

# 7) Create an object `test_obj` of the class `test_class`.
#    (We can create this object because `task()` is implemented.)

# 8) Call `test_obj.task()` to run the overridden method in `test_class`.

# 9) Call `test_obj.print(100)` to print the value 100 using the parent class method.
