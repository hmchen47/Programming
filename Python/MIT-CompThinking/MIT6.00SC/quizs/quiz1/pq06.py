#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q6
# 1. What is the value of the expression f('abbc')
# 2. Is the value of the expression f('bbcaa') predictable from the 
#   semantics of Python?  Explain why or why not
# 3. Is f total, i.e., defined for all values of s of type str? 
#   Explain why or why not.


def f(s):
    """Assumes type(s) == str"""
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else: 
            d[c] = 1
    
    x = None
    for k in d.keys():
        if x == None:
            x = d[k]
            y = k
        elif d[k] > x:
            x = d[k]
            y = k
    return y


if __name__ == '__main__':
    print f('abbc')

    print f('bbcaa')



    