#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q4
#
# Implement the body of the function specified in the box

def findAll(wordList, lStr):
    """ assumes: wordList is a list of words in lowercase.
            lStr is a str of lowercase letters.
            No letter occurs in lStr more than once
        returns: a list of all the words in wordList that contain
            each of the letters in lStr exactly once and no
            letters not in lStr."""
    
    lstWord = []
    for word in wordList:
        invalid = False
        for char in word:
            if (char not in lStr):
                invalid = True
                break

        if invalid == True:
            continue
        else:
            lstWord.append(word)

    return lstWord
    

    # solution code - not working due to different length
    '''
    result = []
    letters = sorted(lStr)
    for word in wordList:
        w = sorted(word)
        print w, letters
        if w == letters:
            result.append(word)

    return result
    '''

wordList = ['test', 'atm', 'list']
lStr ='estsl'

print findAll(wordList, lStr)