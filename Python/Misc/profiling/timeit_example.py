#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

# URL: https://pymotw.com/2/timeit/index.html

# usage: python timeit_example.py

import timeit

# using setitem
t = timeit.Timer("print 'main statement'", "print 'setup'")

print 'TIMEIT:'
print t.timeit(2)

print 'REPEAT:'
print t.repeat(3, 2)


