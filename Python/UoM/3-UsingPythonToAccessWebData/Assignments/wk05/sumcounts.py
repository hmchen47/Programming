#!/usr/bin/env python2
# _*_ coding: utf-8 _*_
'''
    The program is for the assignment to extract XML data and parse the 
    counts and then sums the counts.
'''
import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET

# ask for URL input
url = raw_input('Enter location: ')
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
print 'Retrieving', url

# open url and parsing the data
try: 
    data = urllib.urlopen(url).read()
except IOError as e:
    print "IOError({0}): {1}".format(e.errno, e.strerror)
    exit()

# retrieve data from the provide URL
print 'Retrieved', len(data), 'characters'

# paring XML data to tree structure fromat
root = ET.fromstring(data)

print 'Count:', len(root.find('comments').findall('comment'))

# retrieve count text and convert to integer to sum them
cnt = 0
for comment in root.find('comments').findall('comment'):
    # print comment.find('count').text
    cnt += int (comment.find('count').text)

print 'Sum:', cnt
