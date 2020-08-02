# -*- coding: utf-8 -*-
import math

class Circle:
    def __init__(self, r):
        self.area = r**2 * math.pi

circle = Circle(5)
print(circle.area)
