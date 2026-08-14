# 1) Create a class named `myClass`.
class myclass:
    __x = 27

    def __y(self):
        print("I'm inside the class")

    def hello(self):
        print(self.__x)


foo = myclass()
foo.hello()
foo.__y()
print(foo.__x)

# 2) Inside the class, create a private class variable `__privateVar = 27`.
#    (The double underscore makes it name-mangled, so it cannot be accessed directly outside the class.)

# 3) Define a private method `__privMeth(self)`:
#    a) This method prints "I'm inside class myClass".
#    (It is also name-mangled because of the double underscore.)

# 4) Define a public method `hello(self)`:
#    a) Print the value of the private variable using `myClass.__privateVar`.

# 5) Create an object `foo` of the class `myClass`.

# 6) Call the public method `foo.hello()` to display the private variable value.

# 7) Attempt to access the private method using `foo.__privMeth`.
#    (This will not work directly because `__privMeth` is private/name-mangled.)
