#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q6
#
# 1. What does it print?
# 2. Does it terminate normally? Why or why not?


def f(s, d):
    for k in d.keys():
        d[k] = 0
    for c in s:
        if c in d:
            d[c] += 1
        else: d[c] = 0
    return d

def addUp(d):
    result = 0
    for k in d:
        result += d[k]
    return result

d1 = {}
d2 = d1
d1 = f('abbc', d1)
print addUp(d1)

d2 = f('bbcaa', d2)
print addUp(d2)
print f('', {})
# print result