#!usr/bin/python
# _*_ coding = utf-8 _*_

cntVowels = 0

for char in s:
    if char in ['a', 'e', 'i', 'o', 'u']:
        cntVowels += 1

print 'Number of vowels: ', cntVowels
