#!/usr/bin/python
# _*_ coding = UTF-8 _*_

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def timesFive(a):
    return a * 5

def addOne(a):
    return a + 1

def power(a):
    return a**2

#applyToEach(testList, timesFive)
#print testList

#applyToEach(testList, abs) 
#print testList

#applyToEach(testList, addOne) 
#print testList

applyToEach(testList, power) 
print testList