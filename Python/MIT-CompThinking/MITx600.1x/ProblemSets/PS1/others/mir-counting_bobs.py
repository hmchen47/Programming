#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

s = "azcbobobegghakl"
count = 0

for i in range(0, len(s) - 2):
    if s[i:i+3] == "bob":
        count += 1

print "Number of times bob occurs is: " + str(count)
