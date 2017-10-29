#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q2

x = 10.0
for i in range(10):
    x += 0.1
print x == 11.0

print repr(x)
# float poin tissue

for i in range(10):
    x -= 0.1
print x == 10.0