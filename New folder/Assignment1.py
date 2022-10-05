import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)


class Person:
    theTitles = "Mr, Mrs, Miss, Dr"

    def __init__(self, title, firstname, lastname, birthYear, address, telephone, email):
        self.title = title
        self.fname = firstname
        self.lname = lastname
        self.bYear = birthYear
        self.address = address
        self.tphone = telephone
        self.mail = email

    def fullName(self):
        print(f"{self.title} {self.fname} {self.lname}")

    def personAge(self):
        age = 2020 - self.bYear
        print(f"{self.title} {self.fname} {self.lname} is {age} years old")

    @staticmethod
    def isAdult(year):
        age = 2020 - year
        if age > 18:
            print(f"an adult")
            return True
        else:
            print(f"Not an adult")
            return False

    @classmethod
    def error(cls, year):
        age = 2020 - year
        if age > 2020:
            logging.error("Error processing the data, enter correct age", exc_info=True)


P1 = Person('Mr', 'Dave', 'Blaser', 1990, 'Brampton', 9054659809, 'dave@gmail.com')
P2 = Person('Mr', 'Dave', 'Blaser', 2005, 'Brampton', 9054659809, 'dave@gmail.com')
P3 = Person('Mr', 'Dave', 'Blaser', -1, 'Brampton', 9054659809, 'dave@gmail.com')
P4 = Person('M', 'Dave', 'Blaser', 1990, 'Brampton', 9054659809, 'dave@gmail.com')


P1.personAge()
P2.isAdult(2005)
P3.error(-1)
