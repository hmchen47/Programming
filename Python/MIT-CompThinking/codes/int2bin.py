#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def int2bin(n):
    '''
    convert an integer into binary as string

    argument: integer, value to convert

    returns: string, a string to represent binary of the given number
    '''
    # check the negative or not
    if n < 0:
        isNeg = True
        num = abs(n)
    else:
        isNeg = False
        num = n

    # convert
    result = ''
    if num == 0:
        result = '0'
    
    while num > 0:
        result = str(num % 2) + result
        num /= 2

    if isNeg:
        result = '-' + result

    return result


num = 32
print('integer: {} -> binary: {}'.format(num, int2bin(num)))
print('')

