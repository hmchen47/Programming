#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q5

'''
The following code contains two semantic errors. Correct it so that 
it reads in integers until the user enters -1, and then prints the 
sum of the integers (8 points)
'''

def getLines():
    inputs = []
    while True:
        line = raw_input('Enter a positive integer, -1 to quit: ')
    #    if line == -1:
        if line == '-1':
            break
        inputs.append(line)
    return inputs # TypeError: 'NoneType' object is not iterable

total = 0
for e in getLines():
#    total += e 
    # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    total += int(e)
print total 

