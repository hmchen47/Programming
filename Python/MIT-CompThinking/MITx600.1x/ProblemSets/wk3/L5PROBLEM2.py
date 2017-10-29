#!/usr/bin/python
# _*_ coding = UTF-8 _*_


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)