class TheVehicle:
    def __init__(self,name, maxspeed, mileage, brand):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.brand = brand

    def seatingCapacity(self, capacity):
        no = capacity
        print("Number of seats are" + str(no))


class Truck(TheVehicle):
    def __init__(self,name, maxspeed, mileage, brand):
        super(Truck, self).__init__(name, maxspeed, mileage, brand)
    def output(self):
        print (self.name, str(self.maxspeed), str(self.mileage), self.brand)


v = TheVehicle("Truck", 270, 26, "Ram")
v.seatingCapacity(4)
t = Truck("truck",220,20,"peterbelt")
t.output()

