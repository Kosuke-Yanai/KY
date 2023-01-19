# -*- coding: utf-8 -*-
class Square:
    square_list = []
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.square_list.append((self.width, self.height))
        
s1 = Square(10, 5)
s2 = Square(3, 10)
s3 = Square(40, 25)

print(Square.square_list)