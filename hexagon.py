from calculator import Shapes

class Hexagon(Shapes):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = self.side ** 2 * ((3 ** 0.5 * 3) / 2)
        return area

    def get_perimeter(self):
        perimeter = self.side * 6
        return perimeter

