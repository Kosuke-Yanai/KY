# -*- coding: utf-8 -*-
class Hexagon:
    def __init__(self, l1, l2, l3, l4, l5, l6):     
        self.calculate_perimeter = l1 + l2 + l3 + l4 + l5 + l6
        
hexagon = Hexagon(2, 4, 6, 8, 10 , 12)
print(hexagon.calculate_perimeter)
