#!/usr/bin/python
# _*_ coding = UTF-8 _*_

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    menor = min(a,b)
    
    while menor > 0:
        if a % menor == 0 and b % menor == 0:
            return menor
        menor -= 1    