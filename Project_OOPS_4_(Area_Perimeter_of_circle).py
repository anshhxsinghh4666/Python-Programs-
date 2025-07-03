# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of he class which calculates the area of the circle.
# Define a circumference() method if the class which allows you to claculate the perimeter of the circle.

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2

    def circumference(self):
        return 2 * (22/7) * self.radius

radius = float(input("Enter the radius of the circle: "))

c1 = circle(radius)
print("Area of circle = " , c1.area())
print("circumference of circle = " ,c1.circumference())
