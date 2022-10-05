class Vehicle:

     def __init__(self, number, model, company, color, name, price):
        self.number = number
        self.model = model
        self.company = company
        self.color = color
        self.name = name
        self.price = price
    
     def VehicleInfo(self):
        print(f"Vehicle number :{self.number} \n Model :{self.model} \n Company :{self.company} \n Color :{self.color} \n Name :{self.name} \n Price :{self.price} ")
   
     def VehicleAvg(self, average):
         print(f"{self.name} average is {average}.") 

     def VehicleSpeedMax(self,speed):
         print(f"{self.name} maximun speed is {speed}.")

     def VehicleColor(self):
         print(f"{self.name} color is {self.color}")  

V1 = Vehicle(1,"2010","Honda","Black","Accord","9000");
V1.VehicleInfo()
V1.VehicleAvg(20)
V1.VehicleSpeedMax(220)
V1.VehicleColor()

print()

V2 = Vehicle(6,"2001","Toyota","Grey","Camry","2000");
V2.VehicleInfo()
V2.VehicleAvg(19)
V2.VehicleSpeedMax(240)
V2.VehicleColor()

print()

V3 = Vehicle(4,"2016","Jaguar","Black","XF","29000");
V3.VehicleInfo()
V3.VehicleAvg(26)
V3.VehicleSpeedMax(270)
V3.VehicleColor()

