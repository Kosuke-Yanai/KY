# -*- coding: utf-8 -*-

def square(x):
    """
    Returns x ^ x.
    :param x: int.
    :return int square of x.
    """
    return x ** 2

a = input("type a number:")
a = int(a)

print(square(a))
