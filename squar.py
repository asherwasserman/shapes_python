from rectangle import  Rectangle


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
s = Square(5)
print(s.get_area())