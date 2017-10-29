#!/usr/bin/python
# _*_ coding = UTF-8 _*_

# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "/home/xala/workarea/Introduction-to-Computer-Science-and-Programming-with-python/week6/Problems/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.
    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.
    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.
    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList
    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.
    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words
    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/home/xala/workarea/Introduction-to-Computer-Science-and-Programming-with-python/week6/Problems/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
    shift: 0 <= int < 26
    returns: dict
    """
    upper_dict = {}
    lower_dict = {}
    offset = shift
    for letter in string.ascii_uppercase:
        upper_dict[letter] = string.ascii_uppercase[offset%26]
        offset += 1
         
    offset = shift
    for letter in string.ascii_lowercase:
        lower_dict[letter] = string.ascii_lowercase[offset%26]
        offset += 1 
            
    return  dict(upper_dict.items() + lower_dict.items())   

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    text_coded = ''
    for index in range(0, len(text)):
        text_coded += str(coder.get(text[index], text[index]))
    return text_coded
        
        

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    max_real_words = 0
    best_shift = 0
    
    for i in range(0, 26):
        coded_text = applyShift(text, i)
        list_coded_words = coded_text.split(' ')
        n_valid_words = 0
        for word in list_coded_words:
            if isWord(wordList, word):
                n_valid_words += 1
        if n_valid_words > max_real_words:
            max_real_words = n_valid_words
            best_shift = i
    return best_shift    
        

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.
    returns: string - story in plain text
    """
    
    wordList = loadWords()
    story = getStoryString()
    bestShift = findBestShift(wordList, story)
    return applyShift(story, bestShift)
    

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()