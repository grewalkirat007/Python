# class Person:
#     def display(self):
#         print("I am a person")
    
#     def greet(self):
#         print("Hello, how are you doing?")

# p1 = Person()
# p1.display()
# p1.greet()
# # print(type(p1))
# p2 = Person()
# p3 = Person()

class Movies:
    count = 0
    def __init__(self, m_Name, m_ReleaseYear, m_IsRented):
        self.id = Movies.count
        self.name = m_Name
        self.year = m_ReleaseYear
        self.rent = m_IsRented
        Movies.count += 1

    def ID(self):
        print(f"The Book ID: {self.id}")
    
    def Name(self):
        print(f"The Book Name: {self.name}")

    def ReleaseYear(self):
        print(f"The Book was released in year: {self.year}")

    def IsRented(self):
        if self.rent == True:
            print(f"The Book is rented from the library")
        else:
            print(f"The Book is available to be rented")

    @classmethod
    def movie_from_string(cls, s):
        name, year, rent = s.split(",")
        return cls(name, int(year), bool(rent))


m1 = Movies("Terminator", 2003, True)
# m1.set_details()
m1.ID()
m1.Name()
m1.ReleaseYear()
m1.IsRented()

m5 = Movies.movie_from_string("Hobby,1992,True")
print(m5.id, m5.name, m5.year)

m6 = Movies.movie_from_string("Hob,1982,True")
print(m6.id, m6.name, m6.year)
