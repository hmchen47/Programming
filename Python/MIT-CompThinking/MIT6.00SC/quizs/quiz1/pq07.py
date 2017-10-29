#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q7
# 1.1 The value of f('3') is ['3']
# 1.2 The call f(3) would cause an error message to be displayed
# 2. What does print f([1, [[2, 'a'], ['a','b']], (3, 4)]) print?


def f(L):
    result = []
    for e in L:
        if type(e) != list:
            result.append(e)
        else:
            return f(e)     # recursive fucntion
    return result 

if __name__ == '__main__':

    print f('3')
#    print f(3)     # TypeError: 'int' object is not iterable for line 12
    print f([1, [[2, 'a'], ['a','b']], (3, 4)])
