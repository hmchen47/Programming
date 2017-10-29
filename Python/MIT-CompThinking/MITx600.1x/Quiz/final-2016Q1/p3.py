#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

'''
Test cases

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns 
    {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns 
    {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns 
    {True: [0, 2, 4]}
'''
import random
import time

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invertDict = {}
    for key, value in d.items():
        if value in invertDict:
            invertDict[value].append(key)
            invertDict[value] = sorted(invertDict[value])
        else:
            invertDict[value] = [key]

    return invertDict

def boundaryCases():
    d = {1:10, 2:20, 3:30}
    print(dict_invert(d))

    d = {1:10, 2:20, 3:30, 4:30}
    print(dict_invert(d))

    d = {4:True, 2:True, 0:True}    
    print(dict_invert(d))

    time.sleep(3)

def randomCases():
    while True:
        d = {}
        n = random.randint(3, 20) # number of items in dictionay

        # generate dictionary
        for cnt in range(n):
            d[cnt] = d.get(cnt, random.randint(50, 60))

        print('')
        print(d)
        print(dict_invert(d))

        time.sleep(0.3)


if __name__ == "__main__":
    boundaryCases()
    randomCases()

