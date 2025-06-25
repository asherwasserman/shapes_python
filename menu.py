from calculator import Shapes
from rectangle import Rectangle
from squar import  Square
from triangle import  Triangle
from circle import Circle
from hexagon import Hexagon
class Menu:
    def show_menu(self):
        print("===== Geometric Shape Calculator =====")
        print("1. Calculate the area of a geometric shape")
        print("2. Calculate the total area of multiple geometric shapes")
        print("3. Compare the areas of two geometric shapes")
        print("0. Exit")

    def menu_shapes(self):
        running = True
        while (running):
            print("===== Choose a Geometric Shape =====")
            print("1. Rectangle")
            print("2. Square")
            print("3. Triangle")
            print("4. Circle")
            print("5. Hexagon")
            print("0. Go back to main menu")
            choice = input()
            match choice:
                case 1:
                    print(self.calculate_rectangle())
                case 2:
                    print(self.calculate_squar())
                case 3:
                    print(self.calculate_triangle())
                case 4:
                    print(self.calculate_circle())
                case 5:
                    print(self.calculate_hexagon())
                case 6:
                    running = False

    @staticmethod
    def calculate_rectangle():
        length = input("please enter the length of the rectangle")
        width = input("please enter the width of the rectangle")
        new_rectangle = Rectangle(length, width)
        return new_rectangle
    @staticmethod
    def calculate_squar():
        side = input("please enter one side of the squar")
        new_squar = Square(side)
        return new_squar

    @staticmethod
    def calculate_triangle():
        length = input("please enter the length of the rectangle")
        width = input("please enter the width of the rectangle")
        new_triangle = Triangle(length, width)
        return new_triangle

    @staticmethod
    def calculate_circle():
        radius = input("please enter the radius of the rectangle")
        new_circle = Circle(radius)
        return new_circle

    @staticmethod
    def calculate_hexagon():
        side = input("please enter one side of the squar")
        new_hexagon = Hexagon(side)
        return new_hexagon







