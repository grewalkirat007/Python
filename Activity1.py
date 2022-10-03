class circle:
    def __init__(self, radius):
        self.radius = radius

    def setradius(self, newradius):
        self.radius = newradius

    def getarea(self):
        return 3.14 * self.radius ** 2

    def getperimeter(self):
        return 2 * 3.14 * self.radius


circle007 = circle(12)
print(circle007.getarea())
print(circle007.getperimeter())
