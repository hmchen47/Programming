#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def isPalindrome(aString):
    '''
    aString: a string
    '''
    if len(aString) <= 1:
        return True
    else:
        if aString[0] == aString[-1]:
            # print aString, aString[1:-1]
            return isPalindrome(aString[1:-1])
        else:
            return False


print('a', isPalindrome('a'))
# True
print('ab', isPalindrome('ab'))
# False
print('abcba', isPalindrome('abcba'))
True
print('abba', isPalindrome('abba'))
# True
print('abcdba', isPalindrome('abcdba'))
# False
print('abcdeba', isPalindrome('abcdeba'))
# False
'''
Missing test cases
1. capital
2. empty
3. comapring upper and lower cases -> should C and c the same?
'''


print(isPalindrome(''))
# True
print(isPalindrome('rdv'))
# False
print(isPalindrome('sNENs'))
# True
print(isPalindrome('GvUgTsXA'))
# False
print(isPalindrome('ziaZaiz'))
# True
print(isPalindrome('g'))
# True
print(isPalindrome('dOSzzSOd'))
# True
print(isPalindrome('mUeFiqpVFD'))
# False
print(isPalindrome('rrBBrr'))
# True
print(isPalindrome('aoLOh'))
# False