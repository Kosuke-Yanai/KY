# -*- coding: utf-8 -*-

def change_float(string):
    """
    Returns float(string).
    :param x: str.
    :return float string.
    """
    try:
        return float(string)
    except ValueError:
        print("strings could not be converted to float.")
    
string = input("type a strings:")
string = str(string)

print(change_float(string))

