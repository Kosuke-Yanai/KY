# -*- coding: utf-8 -*-
list = [x + 25 for x in range(26)]

for i, new in enumerate(list):
    new = list[i]
    print(new)