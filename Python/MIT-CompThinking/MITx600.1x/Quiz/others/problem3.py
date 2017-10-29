#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def myLog(x, b):
    b1 = b
    i = 1
    if x < b:
        return 0
    while b1*b <= x:
        if b == 0:
            return 0
        i+=1
        b1*= b
    return i