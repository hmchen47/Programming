#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data

mysock.close()


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex01.py
HTTP/1.1 200 OK
Date: Tue, 25 Aug 2015 04:46:13 GMT
Server: Apache
Last-Modified: Fri, 07 Aug 2015 16:39:14 GMT
ETag: "20a1817f-a7-51cbb46b621a7"
Accept-Ranges: bytes
Content-Length: 167
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''