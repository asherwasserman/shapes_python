class Shapes:
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def __add__(self, other):
        """ returnes the area of object1 and object2 """
        area = other.get_area() + self.get_area()
        return area
    def __str__(self):
        """ Returns a string representation of the shape's class name. """
        return f"class {self.__class__.__name__}"

    def __eq__(self, other):
        """ returns true if the left object is equal to the right object, if not, returns false """
        if other.get_area == self.get_area():
            return True
        else:
            return False


    def __ge__(self, other):
        """" returns true if the left object is equal or smaller than the right object, if not, returns false """
        if other.get_area >= self.get_area():
            return True
        else:
            return  False

    def __le__(self, other):
        """ returns true if the left object is equal or smaller than the right object, if not, returns false """
        if other.get_area <= self.get_area():
            return True
        else:
            return False

    def __lt__(self, other):
        """ returns true if the left object is smaller than the right object, if not, returns false """
        if other.get_area < self.get_area():
            return True
        else:
            return False

    def __gt__(self, other):
        """" returns true if the left object is equal greater than the right object, if not, returns false """

        if other.get_area > self.get_area():
            return True
        else:
            return False

