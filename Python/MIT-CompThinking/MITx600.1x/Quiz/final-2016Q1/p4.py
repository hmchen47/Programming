#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

'''
getSublists(L, n)

Input: L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 
Output:
[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Input: L = [1, 1, 1, 1, 4] and n = 2
Output:
[[1, 1], [1, 1], [1, 1], [1, 4]]



longestRun(L)
Input: L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
Output: [3, 4, 5, 7, 7]
'''
import random
import time

def getSublists(L, n):
    '''
    from a given list L and return a set of sublists with lenth n

    arguments:
        L: list
        n: integer, the length of sublist

    retunrs: a list of all sublists with length of n
    '''
    # initialize the main list
    mainLst = []
    for cnt in range(len(L) - n + 1):
        sublst = []
        for idx in range(n):
            sublst.append(L[cnt + idx])
        mainLst.append(sublst)
    return mainLst

def longestRun(L):
    '''
    from a given list to get the longest non-drecremental values

    arguments:
      L: list

    retunrs: the length of the longest 

    pseudo code:
      1. iterate range idx from longest to 1
      2. generate all sublists with the given idx
      3. check the sublists with its sorted list
      4. if any sublist is the same as the sorted sublist, return the length 
         of the sublist
    '''
    for n in range(len(L), 0, -1):
        subLsts = getSublists(L, n)
        for subLst in subLsts:
            sortedLst = sorted(subLst)
            # print(n, subLst)
            if subLst == sortedLst:
                # print('sorted list = {}, sublsts ={}'.format(subLst, subLsts))
                return len(subLst)
    return None

def boundaryCases():
    L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
    n = 4
    print(L)
    # print(getSublists(L, n))
    print(longestRun(L))
    print('')

    L = [1, 1, 1, 1, 4] 
    n = 2
    print(L)
    # print(getSublists(L, n))
    print(longestRun(L))
    print('')


    time.sleep(3)

def randomCases():
    while True:
        L = []
        for cnt in range(random.randint(5, 15)):
            L.append(random.randint(0, 10))
        n = random.randint(1, len(L))

        print(len(L), L)
        # print(n, getSublists(L, n))
        print(longestRun(L))        
        print('')

        time.sleep(0.2)


if __name__ == '__main__':
    boundaryCases()
    randomCases()