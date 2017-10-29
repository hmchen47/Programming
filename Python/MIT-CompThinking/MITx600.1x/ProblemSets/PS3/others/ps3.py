#!/usr/bin/python
# _*_ coding = UTF-8 _*_


# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/xala/workarea/Introduction-to-Computer-Science-and-Programming-with-python/week4/Problems/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True        
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += '_ '
    return ans

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            ans += letter
    return ans

def isLetterGuessed(secretWord, userLetter):
    '''
    secretWord: string, the word the user is guessing
    userGuessed: char, letter from user
    returns: boolean, True if the letter is in secretWord;
      False otherwise
    '''    
    if userLetter.lower() in secretWord:
            return True
    return False        
        
def user_letter_list(letter, lettersList):
    if letter not in lettersList:
        lettersList.append(letter)
    return lettersList    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''  
    guesses = 8
    letterList = []
    lettersGuessed = []
    guess = True
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-----------'
    
    while guess:                
        if guesses == 0:
            guess = False
            print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
            break 
            
        print 'You have ' + str(guesses) + ' guesses left'
        print 'Available letters: ' + str(getAvailableLetters(letterList))                   
        letter = raw_input('Please guess a letter: ')                                
                                
        if letter.lower() not in secretWord and letter.lower() not in letterList:
            letterList = user_letter_list(letter.lower(), letterList)
            guesses -= 1
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        elif letter.lower() in letterList:          
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        elif letter.lower() in secretWord:                        
            letterList = user_letter_list(letter.lower(), letterList)
            if letter.lower() not in lettersGuessed:
                lettersGuessed.append(letter.lower())
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                print '-----------'
                if isWordGuessed(secretWord, lettersGuessed):
                    guess = False
                    print 'Congratulations, you won!'                    
            else:
                print "Oops! You've already guessed that letter:  " +  getGuessedWord(secretWord, lettersGuessed)
                print '-----------'          
                    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = chooseWord(loadWords())
#hangman(secretWord)
