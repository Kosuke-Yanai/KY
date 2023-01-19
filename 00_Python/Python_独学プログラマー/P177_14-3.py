# -*- coding: utf-8 -*-
class Param:
    def __init__(self):
        self.param = "DEX"

def comp(x, y):
    print(x is y)

dex = Param()
same_dex = dex
comp(dex, same_dex)

another_dex = Param()
comp(dex, another_dex)