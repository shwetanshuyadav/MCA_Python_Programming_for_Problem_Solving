# circle.py

from .point import Point   # relative import inside package

class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise TypeError("center must be a Point object")
        
        self.center = center
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def __str__(self):
        return f"Circle(Center={self.center}, Radius={self.radius})"