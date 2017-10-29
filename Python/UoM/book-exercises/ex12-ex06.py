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
    print tag.get('href', None)


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex06.py
Enter - http://www.py4inf.com/book.htm
http://www.amazon.com/gp/product/1492339245/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1492339245&li
nkCode=as2&tag=drchu02-20
http://www.amazon.com/gp/product/1492339245/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1492339245&li
nkCode=as2&tag=drchu02-20
https://www.createspace.com/4430203
http://www.amazon.com/dp/B00K0O8HFQ
html-270/
http://do1.dr-chuck.com/py4inf/EN-us/book.pdf
http://do1.dr-chuck.com/py4inf/KO-ko/book.pdf
https://github.com/statkclee/py4inf-kor
http://fanwscu.gitbooks.io/py4inf-zh-cn/
http://do1.dr-chuck.com/py4inf/ES-es/book.pdf
https://github.com/ftardio
book_270.epub
html_270.zip
http://itunes.apple.com/us/book/python-for-informatics/id554638579?mt=13
http://www-personal.umich.edu/~csev/books/py4inf/ibooks//python_for_informatics.ibooks
http://www.py4inf.com/code
http://www.greenteapress.com/thinkpython/thinkCSpy/
http://allendowney.com/
'''