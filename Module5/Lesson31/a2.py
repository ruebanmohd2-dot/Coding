# 1) Import `ABC` and `abstractmethod` from the `abc` module.
#    (These are used to create abstract base classes.)
from abc import ABC, abstractmethod
# 2) Create an abstract base class named `Animal` that inherits from `ABC`


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("i can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class dog(Animal):
    def move(self):
        print("i can bark")


class lion(Animal):
    def move(self):
        print("I can roar")


R = Human()
R.move()
K = Snake()
K.move()
R = dog()
R.move()
K = lion()
K.move()

# 7) Create a subclass `Lion` that inherits from `Animal`:
#    a) Implement the `move()` method to print "I can roar".

# 8) Create objects of each subclass and call their `move()` methods:
#    a) Create `R = Human()` and call `R.move()`.
#    b) Create `K = Snake()` and call `K.move()`.
#    c) Create `R = Dog()` and call `R.move()`.
#    d) Create `K = Lion()` and call `K.move()`.
#    (Each object prints its own movement behavior due to method overriding.)
