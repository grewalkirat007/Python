class Car:
    size = "small"

    def __init__(self):
        print("I am contructor from Car Class!")

    def Info(self):
        print("Car has 4 seats")

    def carFeatures(self):
        print("Car is available in fully-automatic model only")


class SUV(Car):
    status = "big"

    def __init__(self):
        print("I am contructor from SUV Class!")

    def Info(self):
        print("SUV has 6 seats")

    def suvFeatures(self):
        print("SUV is available in fully-automatic and manual models ")


c1 = Car()

s1 = SUV()

s1.Info()

print(s1.status)

s1.suvFeatures()

c1.carFeatures()
