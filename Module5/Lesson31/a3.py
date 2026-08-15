# 1) Create a class `India` with three methods:
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.
class India:
    def capital(self):
        print("Delhi")

    def language(self):
        print("Hindi")

    def type(self):
        print("Semi Developed")

# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.


class USA:
    def capital(self):
        print("washington DC")

    def language(self):
        print("Engling")

    def type(self):
        print("Developed")


# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`
obj_ind = India()
obj_USA = USA()

# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)\

for i in (obj_ind, obj_USA):
    i.capital()
    i.language()
    i.type()
