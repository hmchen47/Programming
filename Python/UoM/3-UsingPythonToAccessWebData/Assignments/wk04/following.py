# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count =  int(raw_input('Enter count: '))
pos =  int(raw_input('Enter position: '))

#count = int countStr
#os = int posStr

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
for cnt in range(count):
    tags = soup('a')
    newUrl = tags[pos-1].get('href', None)

    newHtml = urllib.urlopen(newUrl).read()
    soup = BeautifulSoup(newHtml)
    #print 'Retrieving: ', newUrl

print 'Last retrieving: ', newUrl
lname = re.findall(u'known_by_(.*)\.html', newUrl)

print 'Last name =', lname[0]