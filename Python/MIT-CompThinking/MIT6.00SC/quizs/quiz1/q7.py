#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q7
#
# 1. What does it print?
# 2. Under the assumption that logBase2 is O(n), what is the order 
#   (use big Oh notation) of f?

def logBase2(n):
    """assumes that n is a positive int
    returns a float that approximates the log base 2 of n"""
    import math
    return math.log(n, 2)

def f(n):
    """assumes n is an int"""
    if n < 1:
        return

    curDigit = int(logBase2(n))
    ans = 'n = '
    while curDigit >= 0:
        if n%(2**curDigit) < n:
            ans = ans + '1'
            n = n - 2**curDigit
        else:
            ans = ans + '0'
            curDigit -= 1
    return ans

for i in range(3):
    print f(i)
