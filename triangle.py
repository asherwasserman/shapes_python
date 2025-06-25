from rectangle import Rectangle
class Triangle(Rectangle):
    def __init__(self, side1, side2):
        super().__init__(side1,side2)
    def get_area(self):
        area = super().get_area() / 2
        return area
    def get_perimeter(self):
        perimeter = (self.length + self.width +
                     (self.length ** 2 + self.width ** 2) ** 0.5)
        return perimeter
r = Rectangle(5, 4)
t = Triangle(5,4)
