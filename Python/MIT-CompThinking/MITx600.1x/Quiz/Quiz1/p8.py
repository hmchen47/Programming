#!/usr/bin/env python2
# _*_ encoding: utf-8 _*_

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    fS = []
    newL = []
    for element in L:
        fS.append(f(element))

    for idx in range(len(fS)):
        if not fS[idx]:
           L[idx] = '!@#'

    for idx in range(len(L)):
        try:
            L.remove('!@#')
        except:
            break;

    return len(L)

run_satisfiesF(L, satisfiesF)

#L = ['a', 'b', 'a', 'c', 'e', 'a', 'a']
#L = ['b', 'c', 'e']
L = ['a', 'b', 'a']
print satisfiesF(L)
print L