#!/usr/bin/python
# _*_ coding = UTF-8 _*_

s = 'azcbobobegghaklbobbobjfuboboo'

def counting_bobs(s): 
    pattern = 'bob'
    index = 0
    counter = 0
    for letter in s:
        if letter == 'b':
           if s.find(pattern, index, index + 3) != -1:
               counter += 1
        index += 1   
    return counter
  
print counting_bobs(s)