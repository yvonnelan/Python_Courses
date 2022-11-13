# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:09:20 2022

@author: Yvonne
"""

avg_str = 'Average value read: 0.72903' 
colpos = avg_str.find(':')
sliced_str = avg_str[colpos+1:]
float_str = float(sliced_str)
print(float_str)
