# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:05:47 2022

@author: Yvonne
"""

total = 0
count = 0
maximum = None
minimum = None

while True:
    try:
        inp = input('Please enter a floating point number: \n')
        if inp == 'done':
            break
        total = total + float(inp)
        count = count + 1
        if maximum is None or maximum < float(inp):
            maximum = float(inp)
        if minimum is None or float(inp) < minimum:
            minimum = float(inp)
    except:
        print('Invalid input')
   
print('Total:', total, 'Count:', count, 'Maximum:', maximum, 'Minimum:', minimum, 'Average:', total/count)