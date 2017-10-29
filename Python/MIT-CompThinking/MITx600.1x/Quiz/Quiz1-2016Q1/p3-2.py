#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

# print(Square(2))
# print(Square(-2))
print(Square(997))