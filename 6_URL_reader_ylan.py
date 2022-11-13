#Yvonne Lan

import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter -')

size = 0
print_count = 0
PRINT_LIMIT = 3000
CHUNK_SIZE = 512

try:
    file = urllib.request.urlopen(url)

except:
    print('Invalid Link')

while True:
        data = file.read(CHUNK_SIZE)
        if len(data) < 1: break
        size = size + len(data)    
        print_count += 1
        if size <= PRINT_LIMIT:
           print(data.decode('utf8'))
        if size > PRINT_LIMIT:
           diff = int(PRINT_LIMIT - size)
           print(data[0:diff].decode('utf8'))
print('There are a total of', size, 'characters in the file')

#link used:
#http://textfiles.com/adventure/221baker.txt