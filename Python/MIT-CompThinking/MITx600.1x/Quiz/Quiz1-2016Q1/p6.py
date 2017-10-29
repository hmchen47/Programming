#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # declar a new list to storage
    new = []

    if type(aList) != list:
        # input is not a list, return a list contain the element
        return new.append(aList)
    else:
        # iterate through all elements of the list
        for idx in range(len(aList)):
            if type(aList[idx]) == list:
                # if the ith element a list call flatten and 
                # concatnate the return list with storage list new
                new = new + flatten(aList[idx])
            else: 
                # the ith element is not a list, append the element
                # into the storage list new
                new.append(aList[idx])

    return new

print(flatten{'abc'})
# ['abc']
print(flatten(['abc', 2, [[3], 4], 5]))
# ['abc', 3, 4, 5]
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
# [1,'a','cat',2,3,'dog',4,5]
print(flatten([[], [1, 2, [3, [4, 5], 6], [7, 8, [9]], 10, 11], [[[[12]]]]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten([]))
'''
missing test cases:
1. dealing with more than one empty list
2. should test from simply cases 
'''

print(flatten([]))
# []
print(flatten([[], []]))
# []
print(flatten([1]))
# [1]
print(flatten([[1]]))
# [1]
print(flatten([[1], [1]]))
# [1, 1]
print(flatten([[1], [2, 3]]))
# [1, 2, 3]
print(flatten([[3], [2, 1, 0], [4, 5, 6, 7]]))
# [3, 2, 1, 0, 4, 5, 6, 7]
print(flatten([[[1]], [[[5]]]]))
# [1, 5]
print(flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1, 2, 1, 1, 0]

