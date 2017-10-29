#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

# URL: https://pymotw.com/2/profile/index.html

# usage: python profile_fibonacci_raw.py

import profile

def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

print 'RAW'
print '=' * 80
profile.run('print fib_seq(20); print')
