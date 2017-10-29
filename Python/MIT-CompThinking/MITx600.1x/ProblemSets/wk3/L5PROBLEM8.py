#!/usr/bin/python
# _*_ coding = UTF-8 _*_

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    middle = len(aStr) / 2
    
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
            return aStr == char
    elif aStr[middle] == char:
        return True
    else:
        if aStr[middle] > char:
            return isIn(char, aStr[:middle])
        else:
            return isIn(char, aStr[middle+1:])