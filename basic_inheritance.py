class Person:
    status = "Employed"
    education = "Masters"

    def __init__(self):
        print("I am contructor from Person Class!")

    def perInfo(self):
        print("This Person lives in Toronto")

    def job_title(self):
        print("This person is working as a Financial Analyst")

class Doctor(Person):
    status = "Volunteer"
    
    def __init__(self):
        print("I am contructor from Doctor Class!")

    def drInfo(self):
        print("This Doctor living in Milton")

    def job_title(self):
        print("This Person is working as a Doctor")

per = Person()

dr = Doctor()

dr.perInfo()

print(dr.status)

print(dr.education)

dr.job_title()

per.job_title()
