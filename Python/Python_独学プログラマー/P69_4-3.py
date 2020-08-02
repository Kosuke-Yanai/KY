# -*- coding: utf-8 -*-

def self_introduction(first_name, family_name, age, height=173, weight=58):
    """
    Returns print .first_name, family_name, age, height=173, weight=58
    :param first_name: str.
    :param family_name: str.
    :param age: .
    :param height: .
    :param weight: .
    :return str print of first_name, family _name, and
    int print of age, height, weight.
    """
    print("My name is", first_name, family_name, ".")
    print(age, "years old.")
    print(height, "cm.")
    print(weight, "kg.")

a = input("type your first name:")
b = input("type your family name:")
c = input("type your age:")
a = str(a)
b = str(b)
c = str(c)

self_introduction(a, b, c)
