class Shapes:
    def get_area(self):
        pass
    def __add__(self, other):
        area = other.get_area() + self.get_area()
        return area
    def __str__(self):
        return f"class {self.__class__.__name__}"