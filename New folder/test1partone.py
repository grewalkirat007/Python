class Person:
    def __init__(self, name, height, weight, gender):
        self.name = name
        self.height = height
        self.weight = weight
        self.gender = gender

    def calculateAge(self, year):
        theyear = 2020
        age = theyear - year
        print(f"{self.name} has the age of {age} years")

class Student(Person):
    def __init__(self, name, height, weight, gender, studentid, program):
        super(Student, self).__init__(name, height, weight, gender)
        self.studentid = studentid
        self.program = program
    
    def student_details(self):
        print(self.name, self.height, self.weight, self.gender, self.studentid, self.program)

    def calculateAge(self, year):
        theyear = 2020
        age = theyear - year
        print(f"The student named {self.name} has the age of {age} years")


P1 = Person("Kirat", 150, 75, "M")

P1.calculateAge(2001)

S1 = Student("Kiratveer", 149, 74, "M", "C0772969", "CPCT")
S1.student_details()
S1.calculateAge(2000)
