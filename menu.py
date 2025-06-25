from random import choice

from calculator import Shapes
from rectangle import Rectangle
from squar import  Square
from triangle import  Triangle
from circle import Circle
from hexagon import Hexagon
class Menu:
    def __init__(self):
        pass

    def show_menu(self):
        running = True
        while running:
            print("===== Geometric Shape Calculator =====")
            print("1. Calculate the area of a geometric shape")
            print("2. Calculate the total area of multiple geometric shapes")
            print("3. Compare the areas of two geometric shapes")
            print("0. Exit")
            choice = int(input())
            match choice:
                case 1:
                    self.print_shapes()
                case 2:
                    self.calculate_shapes()
                case 0:
                    print("by")
                case _:
                    print("Invalid choice. Please try again.")

    def print_shapes(self):
        running = True
        while (running):
            result = self.menu_shapes()
            if result:
                print(f"the area of the shape is: {result.get_area()}")
            else:
                running = False
                print("by")

    def calculate_rectangle(self):
        length = int(input("please enter the length of the rectangle:\n"))
        width = int(input("please enter the width of the rectangle:\n"))
        new_rectangle = Rectangle(length, width)
        return new_rectangle

    def calculate_squar(self):
        side = int(input("please enter one side of the squar:\n"))
        new_squar = Square(side)
        return new_squar


    def calculate_triangle(self):
        length = int(input("please enter the length of the rectangle:\n"))
        width = int(input("please enter the width of the rectangle:\n"))
        new_triangle = Triangle(length, width)
        return new_triangle


    def calculate_circle(self):
        radius = int(input("please enter the radius of the rectangle:\n"))
        new_circle = Circle(radius)
        return new_circle

    def calculate_hexagon(self):
        side = int(input("please enter one side of the squar:\n"))
        new_hexagon = Hexagon(side)
        return new_hexagon

    def menu_shapes(self):
        print("===== Choose a Geometric Shape =====")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Hexagon")
        print("6. exit")
        choice = int(input())
        match choice:
            case 1:
                return self.calculate_rectangle()
            case 2:
                return self.calculate_squar()
            case 3:
                return self.calculate_triangle()
            case 4:
                return self.calculate_circle()
            case 5:
                return self.calculate_hexagon()
            case 6:
                return 0
            case _:
                print("Invalid choice. Please try again.")

    def calculate_shapes(self):
        shapes = []
        running = True
        while running:
            print("===== Add Shape Menu =====")
            print("1. Add another shape to calculate")
            print("2. Get result")
            print("3. Exit")
            choice = int(input())
            match choice:
                case 1:
                    result = self.menu_shapes()
                    if result:
                        shapes.append(result)
                        print("added")
                    else:
                        continue
                case 2:
                    sum = 0
                    for i in shapes:
                        sum += i.get_area()
                    print(f"The result is: {sum}")
                    running = False
                case 3:
                    running = False
                case _:
                    print("Invalid choice. Please try again.")
m = Menu()
m.show_menu()













