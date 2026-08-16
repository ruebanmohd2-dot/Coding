class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        is_borrowed = False

    def borrowed(self):
        self.is_borrowed = True
        print("It is borrowed")

    def return_book(self):
        self.is_borrowed = False
        print("It is in stock")


obj = Book("Harry Potter", "JK Rowling", "Borrowed")
obj2 = Book("XYZ", "Xyz", "Xyz")
obj3 = Book("ABC", "ABC", "Abc")

obj.borrowed()
obj.return_book()
