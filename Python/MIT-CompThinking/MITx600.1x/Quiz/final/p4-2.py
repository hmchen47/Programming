#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def getSublists(L, n):
    '''
    get all sublists of L with n in length
    the sublist must in successive index order of L
    Input: 
        L: list 
        n: length of sublist
    Output:
        list of sublists
    '''
    lst_sublsts = []
    for idx in range(len(L)+1 - n):
        sublst = []
        for cnt in range(n):
            sublst.append(L[idx+cnt])
        lst_sublsts.append(sublst)

    return lst_sublsts


def longestRun(L):
    '''
    get the longest monotonically length of a given integer list
    Output:
        int - legth of the longest monotonical sublist
    '''
    for n in range(len(L), 1, -1):
        lst_sublsts = getSublists(L, n)
        #print n, lst_sublsts
        for idx in range(len(lst_sublsts)):
            cnt = 1
            for inIdx in range(n-1):
                if lst_sublsts[idx][inIdx] <= lst_sublsts[idx][inIdx+1]:
                    cnt += 1
                else:
                    break
            if cnt == n:
                return n
    return 1

#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
#   5
#print longestRun([1, 1, 1, 1, 4])
#   5
#print longestRun([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50])
#   0
#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
#   5
#print longestRun([0])
#   1
#print longestRun([1, 1, 1, 1, 1])
#   5
#print longestRun([-10, -5, 0, 5, 10])
#   5
#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
#   5
#print longestRun([1, 2, 3, -1, -2, -3, -4, -5, -6])
#   3
#print longestRun([-1, -2, -3, -4, -5, -6, -7, 2, 3])
#   3
#print longestRun([1, 3, 5, -1, -3, -5, -7, 1, 3, 5])
#   4
#print longestRun([10, 8, 9, 5, 6, 7, 1, 2, 3, 4])
#   4
#print longestRun([14, 16, 18, 20, 8, 10, 12, 4, 6, 2])
#   4
#print longestRun([7, 4, 1, -7, -11])
#   1
#print longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9])
#   6
#pritn longestRun([1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0])
#   5