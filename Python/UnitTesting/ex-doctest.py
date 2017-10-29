#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import doctest
     
def fib(n):
    """ Calculates the n-th Fibonacci number iteratively 
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(40)
    102334155
    >>> 

    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__": 
    doctest.testmod()