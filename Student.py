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
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

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