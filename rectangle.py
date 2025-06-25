from calculator import Shapes

class Rectangle(Shapes):

    def __init__(self, length, width):
        self.length= length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimeter(self):
        perimeter = self.length * 2 +self.width * 2
        return perimeter
