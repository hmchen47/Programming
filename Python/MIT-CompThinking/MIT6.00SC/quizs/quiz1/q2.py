#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q2
#
# What does the following code print?

T = (0.1, 0.1)
x = 0.0

for i in range(len(T)):
    for j in T:
        x += i + j
        print x
print i

