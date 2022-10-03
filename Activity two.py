class MiniComputer:

    def __init__(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand

    def minicomputer(self):
        print("Size is small.")

    def screencolored(self):
        print("Colorful screen")

class MainframeComputer(MiniComputer):

   def __init__(self, brand):
      self.brand = brand

   def mainframecomputer(self):
       print("Processes faster...")

   def installsoftware(self, software):
       print("New updated features")




w = MainframeComputer("Asus")

w.screencolored()
w.installsoftware("Antivirus")


