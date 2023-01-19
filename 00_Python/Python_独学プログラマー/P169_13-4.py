# -*- coding: utf-8 -*-
class Horse:
    def  __init__(self, name, breed, owner):
        self.namme = name
        self.breed = breed
        self.owner = owner
    
class Rider:
    def __init__(self, name):
        self.name = name

yutaka = Rider("Take Yutaka")
deep = Horse("Deep Inpact", "black", yutaka)
print(deep.owner.name)
    