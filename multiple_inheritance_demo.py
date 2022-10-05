class Employee:
    company = "Amazon"

    def __init__(self):
        print("I am from Employee class Constructor")

    def empInfo(self):
        print("This employee is highly skilled in IT")

    def jobInfo(self):
        print("This emplyee works in Amazon")

class Consultant:
    company = "KK Developer.INC"

    def __init__(self):
        print("I am from Consultant Class Constructor")

    def empInfo(self):
        print("This person works as a Self Employed Consultant")

    def consultInfo(self):
        print("This guy provides IT Consultancy")

    def salaryInfo(self):
        print("This guy charges $200 per hour for profesional services")

    def jobInfo(self):
        print("This emplyee works as Python Developer in Web Applications")

class Programmer(Employee, Consultant):
    # company = "Free Lancer & Facebook"
    
    def __init__(self):
        print("I am from Programmer Class Constructor")

    def progrInfo(self):
        print("This guy is a Full Stack Developer")

    def salaryInfo(self):
        print("This guy charges $200 per hour for profesional services and 100k yearly")

    def jobInfo(self):
        print("This emplyee works as Python Developer and React Developer")

prog = Programmer()

prog.jobInfo()

prog.empInfo()

prog.consultInfo()

print(prog.company)