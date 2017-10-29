#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import urllib
import re

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="http://(.*?)"', html)
for link in links:
    print link



''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex05.py
Enter - http://www.dr-chuck.com/page1.htm
www.dr-chuck.com/page2.htm

python ex12-ex05.py
Enter - http://www.py4inf.com/book.htm
www.amazon.com/gp/product/1492339245/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1492339245&linkCode=
as2&tag=drchu02-20
www.amazon.com/gp/product/1492339245/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1492339245&linkCode=
as2&tag=drchu02-20
www.amazon.com/dp/B00K0O8HFQ
do1.dr-chuck.com/py4inf/EN-us/book.pdf
do1.dr-chuck.com/py4inf/KO-ko/book.pdf
fanwscu.gitbooks.io/py4inf-zh-cn/
do1.dr-chuck.com/py4inf/ES-es/book.pdf
itunes.apple.com/us/book/python-for-informatics/id554638579?mt=13
www-personal.umich.edu/~csev/books/py4inf/ibooks//python_for_informatics.ibooks
www.py4inf.com/code
www.greenteapress.com/thinkpython/thinkCSpy/
allendowney.com/
'''