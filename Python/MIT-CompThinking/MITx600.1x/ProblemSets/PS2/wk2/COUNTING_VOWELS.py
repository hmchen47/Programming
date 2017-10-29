#!/usr/bin/python
# _*_ coding = UTF-8 _*_

s = 'azcbobobegghakla8ufghtre'

def count_vowels(s): 
    vowels = 'aeiou'
    counter = 0
    for vowel in s:
        if vowel in vowels:
            counter += 1
    return counter
 
print count_vowels(s)      