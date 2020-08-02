# -*- coding: utf-8 -*-
class Square:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2
    def change_size(self, n):
        if self.width + n <= 0:
            print("幅は0以下には指定できません")
        else:
            self.width += n
        
a_square = Square(5, 7)
print(a_square.calculate_perimeter())
a_square.change_size(-4)
print(a_square.calculate_perimeter())

