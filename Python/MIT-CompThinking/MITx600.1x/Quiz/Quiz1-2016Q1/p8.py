#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # declar a copy of L
    tmpLst = L[:]
    for idx in range(len(tmpLst)):
        # print tmpLst, tmpLst[idx]

        if not f(tmpLst[idx]):
            L.remove(tmpLst[idx])
            # print 'L =', L

    return len(L)

run_satisfiesF(L, satisfiesF)

def run_satisfiesF(L, satisfiesF):
    return satisfiesF(L)

def f(s):
    return 'a' in s

L = ['abc', 'bcs', 'dsa']
print(run_satisfiesF(L, satisfiesF))
print L