#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG: ', tag
    print 'URL: ', tag.get('href', None)
    print 'Content: ', tag.contents[0]
    print 'Attrs: ', tag.attrs


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex07.py
Enter - http://www.dr-chuck.com/page1.com
TAG:  <a href="/page1.htm">/page1.htm</a>
URL:  /page1.htm
Content:  /page1.htm
Attrs:  [(u'href', u'/page1.htm')]
'''