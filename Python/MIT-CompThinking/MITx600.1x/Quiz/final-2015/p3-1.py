#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        print iteration, L
        iteration += 1
    return lst

sort1([4, 3 ,1, 6, 2, 8])