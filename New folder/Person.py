class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        class_name = self.__class__.__name__
        print(f"{class_name} is destroyed")

    def person_output(self):
        return f"{self.name} {self.age}"

class Student(Person):
    def __init__(self, name, age, regyear):
        super(Student, self).__init__(name, age)
        self.regyear = regyear

    def person_output(self):
        return (f"{self.name} {self.age} {self.regyear}")

    def student_details(self):
        print(self.person_output(), self.regyear)

class Teacher(Person):
    pass

class course:
    pass

P1 = Person("name1", 20)
P1.person_output()

S1 = Student("name2", 21, 2020)
S1.person_output()

T1 = Teacher("name3", 23)
T1.person_output()

# del P1
# del S1
# del T1
