#!/usr/bin/python
# _*_ coding = UTF-8 _*_

# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
    else:
        return aStr[-1] + reverseString(aStr[0:len(aStr)-1])
    

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) > len(word):
        return False
    
    if not x or x == word:
        return True
        
    if x[0]==word[0]:
        return True and x_ian(x[1:], word[1:])
        
    return x_ian(x, word[1:])    

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.
 
    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength:
        return text
    elif text[lineLength - 1] == ' ':
        return text[:lineLength] + "\n" + insertNewlines(text[lineLength:], lineLength)
    else:
        spaceAt = text[lineLength:].find(' ')
        return text[:spaceAt+lineLength] + "\n" + insertNewlines(text[lineLength+spaceAt+1:], lineLength)