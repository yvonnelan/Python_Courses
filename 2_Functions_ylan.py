# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def to_number(num_str):
    num_int = int(num_str)
    return(num_int)

def add_two(num_int1, num_int2):
    added = num_int1 + num_int2
    return added

def cube(numeric):
    import math
    cubed = math.pow(numeric,3)
    return cubed

print(cube(add_two(to_number('2'),to_number('3'))))

