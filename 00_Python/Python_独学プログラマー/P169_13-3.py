# -*- coding: utf-8 -*-
class Shape:
    def what_am_i(self):
        print("I am a shape")
         
class Rectangle(Shape):
    def __init__(self, l1, l2, l3):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
    def calculate_perimeter(self):
        return self.length1 + self.length2 + self.length3

class Square(Shape):
    def __init__(self, l1, l2, l3, l4):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.length4 = l4
    def calculate_perimeter(self):
        return self.length1 + self.length2 + self.length3 + self.length4

a_rectangle = Rectangle(2, 3, 4)
a_square = Square(1, 3, 5, 7)

a_rectangle.what_am_i()
a_square.what_am_i()