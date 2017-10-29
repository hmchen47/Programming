#!/usr/bin/python
# _*_ coding = UTF-8 _*_

def isVowel2(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False

