class rectangle:
    name = "Rectangle"

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class triangle:
    name = "Triangle"

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def area(self):
        sp = (self.s1 + self.s2 + self.s3)/2
        return (sp*(sp-self.s1)*(sp-self.s2)*(sp-self.s3))

class circle:
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * self.radius * self.radius)

r1 = rectangle(10,22)
r2 = rectangle(12, 15)

c1 = circle(5)
c2 = circle(8)

t1 = triangle(2,3,4)
t2 = triangle(5,6,7)

shapes = [r1,r2,c1,c2,t1,t2]

total_area = 0
for shape in shapes:
    total_area += shape.area()
print(total_area)

for shape in shapes:
    print(shape.name)
    print(shape.area())


