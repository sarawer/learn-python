# Define a circle class to create a circle with radius r using the constructor.
# Define an area() methode of the class which calculate the area of the circle.
# define a perimeter() methode of the class which allows you to calculate the perimeter of the circle
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.1418*self.r*self.r
    def perimeter(self):
        return 2*3.1416*self.r

c1=circle(10)
print("area of the circle:",c1.area())
print("perimeter of the circle:",c1.perimeter())
