#!usr/bin/python
# _*_ coding = utf-8 _*_

s = 'azcbobobegghakl'

cnt = 0
strchk = 'bob'
for idx in range(len(s)):
    if s.find(strchk, idx, idx+len(strchk)) != -1:
        cnt += 1

print 'Number of times bob occurs is: ', cnt
