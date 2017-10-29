#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    if len(listA) == 0:
        return 0
    elif len(listA) == 1:
        return listA[0] * listB[0]
    else: 
        return listA[0] * listB[0] + dotProduct(listA[1:], listB[1:])

print(dotProduct([1, 2, 3], [4, 5, 6]))
# 32
print(dotProduct([1.0, 2.0, 3.0], [4, 5, 6]))
# 32.0
print(dotProduct([], []))
# 0
print(dotProduct([1], [2]))
# 2
'''
Missing test cases:
1. no negative values
'''


print(dotProduct([51, 21, 15, -29], [19, -43, 63, 44]))
# -256
print(dotProduct([65, 52, -78, 36, -65, 19], [-18, -33, -69, 42, 52, 35]))
# 1293
print(dotProduct([65, 47, -91, 32, -14, -57, -87, 37, -85, -41], [86, 38, -13, -3, 81, -30, 66, 46, -15, -28]))
# 7422
print(dotProduct([18, 66, -13, 48, -100, -12], [54, 4, 96, -59, -73, 50]))
# 3856
print(dotProduct([-65, -87, 72], [58, -31, -59]))
# -5321
print(dotProduct([-99], [-52]))
# 5148
print(dotProduct([-66, -51, 35, 62, 93, 11, 67], [-21, 71, -39, 84, -79, -95, -91]))
# -12881
print(dotProduct([-64, 93, 26, -69], [20, -30, 40, 89]))
# -9171
print(dotProduct([68, -44, 17, 23, -41, -20, -56, 27, -10, 60], [3, 19, -52, -30, 74, -10, -68, -7, -43, -82]))
# -5911
print(dotProduct([-47, 6, -19, -56, -50, 14], [-61, -49, -3, -86, -13, 8]))
# 8208

