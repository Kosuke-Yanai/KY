# -*- coding: utf-8 -*-
class Triangle:
    def __init__(self, l, h):
        self.area = l * h / 2

triangle = Triangle(5, 4)
print(triangle.area)
