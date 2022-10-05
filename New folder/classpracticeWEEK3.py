"""
Create a class Name Rectangle 

the class will have a class variaible which value will be 'Recatangle'

you need attribute Length and breadth 

funtion area 

def perimeter

area = length*breadth

perimiter = 2*(length+bredth)

you need a static method which will return any static text about rectagnle

you need a class method that will return the value of class variable you declatred earluer 
"""

class Rectangle:
    main_length = 10
    main_breadth = 100
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        rectangle_area = self.l * self.b
        print(f"The area of the rectangle is {rectangle_area}")

    def perimeter(self):
        rectangle_perimeter = 2 * (self.l * self.b)
        print(f"The perimeter of the rectangle is {rectangle_perimeter}")

    @staticmethod
    def rectangle_static_method():
        print("A rectangle is a 2D shape in geometry.")

    @classmethod
    def rectangle_class_method(cls):
        print(f"this is length : {cls.main_length} and breadth is : {cls.main_breadth}")

rectangle = Rectangle(20, 15)
rectangle.area()
rectangle.perimeter()
Rectangle.rectangle_static_method()
Rectangle.rectangle_class_method()
