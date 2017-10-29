#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def getGuessedWord(secretWord, lettersGuessed):
    secretWord = list(secretWord)
    for i in range(len(secretWord)):
        if ( (secretWord[i] in lettersGuessed)==False ):
            secretWord[i] = '_'
    return "".join(secretWord)