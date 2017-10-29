#!/usr/bin/python
# _*_ coding = UTF-8 _*_

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
    
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1