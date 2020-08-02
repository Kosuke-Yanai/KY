# -*- coding: utf-8 -*-
q = input("好きな色は？:")

with open("q.txt", "w", encoding="utf-8") as f:
    f.write(q)