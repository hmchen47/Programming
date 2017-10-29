#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 18: Names, Variables, Code, Functions

"""
Usage: python ex18.py
"""

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless , we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this is just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


"""
Study Drills
1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no 
    less.
8. Did you "end" your function by going back to writing with no indent (dedenting we 
    call it)?

NB: 
The * in *args tells Python to take all the arguments to the function and then put them 
    in args as a list. It's like argv that you've been using, but for functions. It's 
    not normally used too often unless specifically needed.
"""