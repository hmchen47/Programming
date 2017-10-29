#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.
    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    ans = ''
    if s1 == '':
        ans = s2
    elif s2 == '':
        ans = s1
    elif s1 == '' and s2 == '':
        ans =  ''
    else:
        if len(s1) > len(s2):
            itera = s2
            rest = s1
        else:
            itera = s1
            rest = s2
        for i in range(len(itera)):
            ans += s1[i] + s2[i]  
        if (len(s1) != len(s2)):
            ans += rest[len(itera):]            
    return ans
        