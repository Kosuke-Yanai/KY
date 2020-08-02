# -*- coding: utf-8 -*-

def division(x):
    """
    Returns x / 2.
    :param x: int.
    :return int x divided by 2.
    """
    return x / 2

def multiple_4(x):
    """
    Returns x * 4.
    :param x: int.
    :return int x multipled by 4.
    """
    return x * 4 


a = input("type a number:")
a = int(a)

div_x = division(a)
print(multiple_4(div_x))
