# -*- coding: utf-8 -*-
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
answer = []

for i in list1:
    for j in list2:
        new = i * j
        answer.append(new)

print(answer)