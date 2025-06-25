from calculator import Shapes
import math
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (5 ** 2) * math.pi
        return area

    def get_perimeter(self):
        perimeter = 2  * math.pi * self.radius
        return perimeter
