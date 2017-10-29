#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        print iteration, lst
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
    return lst


sort2([4, 3 ,1, 6, 2, 8])