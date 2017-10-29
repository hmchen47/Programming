#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
   print tag.contents[0]
   sum += tag.contents[0]

print 'Sum = ', sum