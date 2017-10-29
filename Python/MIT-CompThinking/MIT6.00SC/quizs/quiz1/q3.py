#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q3
#
# What does the following code print?

def f(s):
    if len(s) <= 1:
        return s
    return f(f(s[1:])) + s[0] #Note double recursion

print f('mat')
print f('math')
