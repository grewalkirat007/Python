class WiredPhone:

    def __init__(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand

    def wiredDial(self):
        print("Dialling now through wire...")

    def hangUp(self):
        print("Hanging up now....")

class ChordlessPhone(WiredPhone):

   def __init__(self, brand):
      self.brand = brand

   def wirelessDial(self):
       print("Dialling through wireless")

   def memorizeNumber(self, number):
       print("Number saved now")


class SmartPhone(ChordlessPhone):
    def __init__(self, brand):
        self.brand = brand

    def installApp(self, app):
        print("App is installed now...")

    def launchApp(self, app):
        print(app + " is lanching now...")

w = ChordlessPhone("Panasonic")

w.hangUp()
w.memorizeNumber("6572456543")


