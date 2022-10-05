class Phone:
    category = "Electronics"

    def __init__(self):
        print("Phone is used for talking from a home or within a building")

    def price(self):
        print("Price of a normal phone is $200!")

    def function(self):
        print("Phone is a good source for communication")

class CellPhone(Phone):
    category = "Wireless Device"

    def __init__(self):
        super().__init__()
        print("Cellphone is used for talking anywhere while moving")

    def price(self):
        print(super().category)
        super().price
        print("Price of cell phone is $500!")

    def feature(self):
        super().function()
        print("Wireless talking and mobility is greater feature of cell phone!")

class SmartPhone(CellPhone):
    category = "Wireless MultiFunctional Device"

    def __init__(self):
        print(super().category)
        print("SmartPhone is used for talking and video call anywhere while moving")

    def price(self):
        print("Price of cell phone is $1000!")

    def specialFeature(self):
        print("Video Call and Video Conference is a special feature of Smart Phone")

p = Phone()

cp = CellPhone()

sp = SmartPhone()

# sp.feature()
sp.specialFeature()
