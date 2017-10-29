#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex03.py
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''