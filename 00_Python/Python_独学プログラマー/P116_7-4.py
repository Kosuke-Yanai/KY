# -*- coding: utf-8 -*-
list = ["3", "24", "76", "99", "223", "1354", "4440"]
max = 10
num = 0
t = 0

while num != "q":
    num = input("input the number:")
    t += 1

    if str.isdigit(num):
        if num in list:
            print("CORRECT!")
            print("cost {} times to find!".format(t))
            break
        else:
            print("FALSE!")
    else:
        print("Input number or type \"q\" to finish")


