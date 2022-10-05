class Book:
    # class variable "count"
    count = 0
    def __init__(self, p_id, p_name, p_author, p_published):
        self.id = p_id
        self.name = p_name
        self.author = p_author
        self.published = p_published
        self.status = "Available"
        Book.count += 1
    
    def borrow_book(self):
        self.status = "Borrowed"
        print(self.name + " is borrowed")

    def return_book(self):
        self.status = "Available"
        print(self.name + " is returned")

    @classmethod
    def book_from_string(cls, s):
        id, name, author, published = s.split(",")
        return cls(int(id), name, author, int(published))
    
    @classmethod
    def my_class_method(cls, s):
        print("hello from class method", s)

    @staticmethod
    def this_static_method(x,y):
        return x+y

print(Book.this_static_method(10,20))

Book.my_class_method("Grewal")

b5 = Book.book_from_string("1010,Hobby,KHJR,1992")
print(b5.id, b5.name)

b1 = Book(1, "Book1", "Author1", 2001)
if b1.status == "Available":
    b1.borrow_book()

b2 = Book(2, "Book2", "Author2", 2000)
b2.borrow_book()
b1.return_book()

print(Book.count)