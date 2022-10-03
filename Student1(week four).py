#Name
#Number
#balance
#limit

#functions:
#----------------
#swipe(amount)
#payBalance(amount)
#setLlimit(newLimit)

#getBalance()
#getName()
#getNumber()
#getLimit()






class  CreditCard:

        def __init__(self, name, number, balance, limit):
            self.name = name
            self.number = number
            self.balance = balance
            self.limit = limit

        def swipe(self, amount):
            self.balance = self.balance + amount

        def payBalance(self, amount):
            self.balance = self.balance - amount

        def setLimit(self, newLimit):
            self.limit = newLimit

        def getBalance(self):
            return self.balance

        def getName(self):
            return self.name

        def getNumber(self):
            return self.number

        def getLimit(self):
            return self.limit




class Student:

    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id

    def getFirstName(self):
        return self._first_name

    def setFirstName(self, name):
        if len(name) > 0:
            self._first_name = name
        else:
            print("First name can NOT be null")

    def getLastName(self):
        return self._last_name

    def setLastName(self, name):
        if len(name) > 0:
            self._last_name = name
        else:
            print("Last name can NOT be null")

    def getID(self):
        return self._student_id

    def setID(self, id):
        if id > 0:
            self._student_id = id
        else:
            print("ID can not be a negatve value")

    def getBalance(self):
        return 200

    def getFullName(self):
        return self.first_name + " " + self.last_name


class CeStarCollege:

    def __init__(self, address, manager):
        self.address = address
        self.manager = manager

student1 = Student("Adam", "Jane", "1234")
student2 = Student("Alex", "Johnson", "3344")


print(student1.first_name)
print (student2.student_id)

print(student1.getFullName())
print(student2.getBalance())

card1 = CreditCard("Alex John", "1111", 0, 10000)

print(card1.getLimit())

card1.swipe(2000)
print("New balance: " + str(card1.getBalance()))

card1.payBalance(100)
print("New balance: " + str(card1.getBalance()))



class Circle:

    def __init__(self, radius):
        self._radius = radius   #Radius is an attribute of this class. So, defined as protected

    def getRadius(self):            #Accessor (getter) for raius
        return self._radius

    def setRadius(self, radius):    #Muatator (setter) for radius
        if radius >= 0:
            self._radius = radius
        else:
            print("Negative values for radius is NOT acceptable")

    def getArea(self):
        return self._radius * self._radius * 3.141

    def getPerimeer(self):
        return 2 * self._radius * 3.141


circle1 = Circle(12)
print(circle1.getArea())
print(circle1.getPerimeer())

circle1.setRadius(1)
print(circle1.getArea())
print(circle1.getPerimeer())


circle1.setRadius(-15)
print(circle1.getArea())
print(circle1.getPerimeer())

