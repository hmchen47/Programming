#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

""" Fibonacci Module """

def fib(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibErr(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ creates a list of Fibonacci numbers up to the n-th generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("Test for the fib function was successful!")
    else:
        print("The fib function is returning wrong values!")
