#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import urllib
from BeautifulSoup import *

img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'w')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size += len(info)
    fhand.write(info)

print size, 'characters copied.'
fhand.close()


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex08.py
70057 characters copied.
'''