# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:05:32 2022

@author: ylan
"""
fname = input('Enter the File Name: ')
search_str = input('Enter a substring: ')
fhand = open(fname)
script_list = []

for line in fhand:
    file_word_list = line.split()
    for element in file_word_list:
        if element in script_list:
            continue
        else:
            script_list.append(element)
            script_list.sort()

def freq_count(search_str, script_list):
    for word in script_list:
        count = 0
        pos = word.find(search_str)
        while pos >= 0:
            count += 1
            pos += len(search_str)
            pos = word.find(search_str,pos)
        print(word+ ' ' + str(count))

freq_count(search_str, script_list)
