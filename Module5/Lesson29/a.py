class FamilyMember:
    def __init__(self, eyecolor, height):
        self.eyecolor = eyecolor
        self.height = height

    def show_traits(self):
        print(self.eyecolor)
        print(self.height)


class Kid(FamilyMember):
    def __init__(self, name, age, eyecolor, height):
        self.name = name
        self.age = age
        super().__init__(eyecolor, height)

    def show_traits(self):
        print(self.name)
        print(self.age)
        super().show_traits()

    def favorite_hobby(self):
        Hobby = input("Enter A hobby")
        print(Hobby)


child = Kid("XYZ", 13, "Blue", 180)
child.show_traits()
child.favorite_hobby()

print(issubclass(Kid, FamilyMember))


"""
5) Override the parent method.
   a) Create another `show_traits()` method inside `Kid`.
   b) Print the kid's name and age.
   c) Use `super().show_traits()` to also show inherited traits.

6) Add a new child class method.
   a) Create `favorite_hobby()`.
   b) Take a hobby as input.
   c) Print the kid's favourite hobby.

7) Create an object.
   a) Create a `Kid` object named `child`.
   b) Add values for name, age, eye colour, and height.

8) Call the methods.
   a) Use `child.show_traits()` to display all details.
   b) Use `child.favorite_hobby()` to display the hobby.

9) Check inheritance.
   a) Use `issubclass()` to check if `Kid` is a subclass of `FamilyMember`.
   b) Print the result.
"""
