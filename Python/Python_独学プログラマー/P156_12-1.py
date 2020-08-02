# -*- coding: utf-8 -*-
class Apple:
    def __init__(self, k, w, c, s):
        self.kind = k
        self.weight = w
        self.color = c
        self.sugar = s
        print("registered")

apple = Apple("王林", 150, "黄緑", 5)
print(apple)
print(apple.kind)
