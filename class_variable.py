class Student:

    college_name = "Cestar College"

    def __init__(self, name):
        self.id = 123
        self.name = name

    def printName(self):
        print(f"Student enrolled with name = {self.name}")

    @classmethod
    def printCollegeName(cls):
        print(f"College name : {cls.college_name}")

# Using ClassName.ClassVariable without creating an object
# 
print(Student.college_name)

Student.college_name = "Lambton in Toronto"

std1 = Student("Raj")
std2 = Student("Kevin")
std3 = Student("Roger")

std1.printName()
std1.printCollegeName()
print(Student.college_name)

std2.printName()
std2.printCollegeName()
print(Student.college_name)

std3.printName()
std3.printCollegeName()
print(Student.college_name)
