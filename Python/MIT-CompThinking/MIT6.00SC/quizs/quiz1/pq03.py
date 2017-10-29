#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q3
# 1. What does it print?
# 2. Characterize the complexity of decode using big Oh notation.

def buildCodeBook():
    letters ='.abcdefghijklnopqrstuvwxyz'
    codeBook = {}
    key = 0
    for c in letters:
        codeBook[key] = c
        key += 1
    return codeBook

def decode(cypherText, codeBook):
    plainText = ''
    for e in cypherText:
        if e in codeBook:
            plainText += codeBook[e]
        else:
            plainText += ' '
    return plainText

codeBook = buildCodeBook()
msg = (3,2,41,1,0)
print decode(msg, codeBook)