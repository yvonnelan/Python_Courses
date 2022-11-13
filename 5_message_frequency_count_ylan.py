# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:26:29 2022

@author: Yvonne Lan
"""
#Yvonne Lan
#Assignment 5

import string

senders = {};
txt = open('mbox.txt')

for line in txt:
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.lower().split()
    try:
        if line[0] == 'From ':
            senders[line[1]] = senders.get(line[1],0) + 1
    except:
        pass
    
message_count = [];
for key, val in senders.items():
    message_count.append((val, key))
    
message_count.sort(reverse=True)

print("The person with the highest number of sent messages is", message_count[0][1], 'with', message_count[0][0], 'messages')

    
