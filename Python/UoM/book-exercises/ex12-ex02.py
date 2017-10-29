#!/usr/bin/python
# _*_ coding=UTF-8 _*_

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
picture = ""
while True:
    data = mysock.recv(5120)
    if (len(data) < 1):
        break
    time.sleep(0.25)
    count += len(data)
    print len(data), count
    picture += data

mysock.close()

# look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n")
print 'Header length', pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()


''' results:
PS D:\Users\hmchen\Documents\CurrentProjects\GitHub\Python\prj\UoM> python ex12-ex02.py
5120 5120
3640 8760
5120 13880
720 14600
5120 19720
720 20440
5120 25560
720 26280
1460 27740
5120 32860
2180 35040
1460 36500
5120 41620
5100 46720
5120 51840
5120 56960
5120 62080
2160 64240
5120 69360
720 70080
223 70303
Header length 242
HTTP/1.1 200 OK
Date: Tue, 25 Aug 2015 04:56:24 GMT
Server: Apache
Last-Modified: Sat, 18 Apr 2015 15:05:20 GMT
ETag: "91d6403f-111a9-51401068ab651"
Accept-Ranges: bytes
Content-Length: 70057
Connection: close
Content-Type: image/jpeg
'''