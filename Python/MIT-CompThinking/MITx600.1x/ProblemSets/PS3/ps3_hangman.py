# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import sys
import random
import string


WORDLIST_FILENAME = "words.txt"

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
    # FILL IN YOUR CODE HERE...
    # create a temporary secret word for checking and removing
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed = ['e', 'i', 'k', 'p', 'a', 'l']
#print isWordGuessed(secretWord, lettersGuessed)

#Testcases:
#print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
#print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
#print isWordGuessed('pineapple', ['s', 'd', 'r', 'v', 'w', 'z', 'm', 'g', 'q', 'k'])
#print isWordGuessed('coconut', ['l', 'v', 'z', 'b', 'p', 'c', 'u', 'q', 'a', 'j'])
#print isWordGuessed('mangosteen', [])
#print isWordGuessed('carrot', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't'])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ['_ '] * len(secretWord)
    #print result
    for letter in lettersGuessed:
        if letter in secretWord:
            for idx in range(len(secretWord)):
                if letter == secretWord[idx]:
                    result[idx] = letter
    return ''.join(result)

#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getGuessedWord(secretWord, lettersGuessed)

#print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
#print getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
#print getGuessedWord('carrot', ['s', 'z', 'i', 'g', 'c', 'e', 'o', 'y', 'a', 'k'])
#print getGuessedWord('mangosteen', ['d', 'p', 'c', 'k', 'u', 'y', 'm', 'b', 'a', 'q'])
#print getGuessedWord('pineapple', [])
#print getGuessedWord('grapefruit', ['e', 'i', 'x', 'b', 'f', 'm', 'r', 'g', 'q', 'a'])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in lettersGuessed:
        alphas.remove(letter)

    return ''.join(alphas)

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getAvailableLetters(lettersGuessed)
#    abcdfghjlmnoqtuvwxyz

#print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
#print getAvailableLetters([])
#print getAvailableLetters(['h', 'q', 'z'])
#print getAvailableLetters(['l', 'r', 'c', 'e', 'j'])
#print getAvailableLetters(['s', 'x', 'w', 'm', 'v', 'z', 'i', 'h', 'u', 'n'])
#print getAvailableLetters(['n', 'r', 'o', 's', 'h', 'l', 'q', 'm', 'c', 'y'])


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
    # FILL IN YOUR CODE HERE...
    
    # get secret word first
#    wordlist = loadWords()

    # printing begining of the game
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'

    # loop through the guest
    guesses = 8
    lettersGuessed = []
#    print secretWord

    while guesses > 0:
        # printing header and available letters
        print '-------------'
        print 'You have', guesses, 'guesses left.'
        print 'Available letters:', getAvailableLetters(lettersGuessed)

        # get input from user
        try:
            guessLetter = raw_input('Please guess a letter: ')
        except IOError as e:
            print 'IOError ({0}): {1}'.format(e.errorno, e.strerror)
            sys.exit(0)

        # convert input letter to lower case
        guessLetter = guessLetter.lower()

        # insert input letter into the list lettersGuessed or ask for input
        if guessLetter in lettersGuessed:
            print "Oops! You've already guessed that letter:", \
                getGuessedWord(secretWord, lettersGuessed)
            continue
        else:
            lettersGuessed += guessLetter
            if guessLetter in secretWord:
                print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
            else: 
                print 'Oops! That letter is not in my word:', \
                    getGuessedWord(secretWord, lettersGuessed)

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print '------------'
            print 'Congratulations, you won!'
            return None
        elif guessLetter not in secretWord:
            guesses -= 1

    if guesses == 0:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was', secretWord, '.'
        return None
    else:
        print 'Something wrong!! Should not be here with guesses=', guesses

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)


# Simple word check

#hangman(c)
'''
Welcome to the game, Hangman!
I am thinking of a word that is 1 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: c
Good guess: c
------------
Congratulations, you won!
None
'''

#hangman(zzz)
'''Welcome to the game, Hangman!
I am thinking of a word that is 3 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: z
Good guess: zzz
------------
Congratulations, you won!
None
'''

#hangman(c)
'''
Welcome to the game, Hangman!
I am thinking of a word that is 1 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ 
-------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ 
-------------
You have 6 guesses left.
Available letters: cdefghijklmnopqrstuvwxyz
Please guess a letter: d
Oops! That letter is not in my word: _ 
-------------
You have 5 guesses left.
Available letters: cefghijklmnopqrstuvwxyz
Please guess a letter: e
Oops! That letter is not in my word: _ 
-------------
You have 4 guesses left.
Available letters: cfghijklmnopqrstuvwxyz
Please guess a letter: f
Oops! That letter is not in my word: _ 
-------------
You have 3 guesses left.
Available letters: cghijklmnopqrstuvwxyz
Please guess a letter: g
Oops! That letter is not in my word: _ 
-------------
You have 2 guesses left.
Available letters: chijklmnopqrstuvwxyz
Please guess a letter: h
Oops! That letter is not in my word: _ 
-------------
You have 1 guesses left.
Available letters: cijklmnopqrstuvwxyz
Please guess a letter: i
Oops! That letter is not in my word: _ 
-----------
Sorry, you ran out of guesses. The word was c .
None
'''

#hangman(sea)
'''
Welcome to the game, Hangman!
I am thinking of a word that is 3 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ _ a
-------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: _ ea
-------------
You have 8 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! You've already guessed that letter: _ ea
-------------
You have 8 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: e
Oops! You've already guessed that letter: _ ea
-------------
You have 8 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: s
Good guess: sea
------------
Congratulations, you won!
None
'''

#hangman(y)
'''
Welcome to the game, Hangman!
I am thinking of a word that is 1 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: x
Oops! That letter is not in my word: _ 
-------------
You have 7 guesses left.
Available letters: abcdefghijklmnopqrstuvwyz
Please guess a letter: z
Oops! That letter is not in my word: _ 
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwy
Please guess a letter: x
Oops! You've already guessed that letter: _ 
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwy
Please guess a letter: z
Oops! You've already guessed that letter: _ 
-------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwy
Please guess a letter: y
Good guess: y
------------
Congratulations, you won!
None
'''


# Complex Test

#hangman('zzz')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 3 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: Z
Good guess: zzz
------------
Congratulations, you won!
None
'''

#hangman('y')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 1 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: z
Oops! That letter is not in my word: _ 
-------------
You have 7 guesses left.
Available letters: abcdefghijklmnopqrstuvwxy
Please guess a letter: z
Oops! You've already guessed that letter: _ 
-------------
You have 7 guesses left.
Available letters: abcdefghijklmnopqrstuvwxy
Please guess a letter: z
Oops! You've already guessed that letter: _ 
-------------
You have 7 guesses left.
Available letters: abcdefghijklmnopqrstuvwxy
Please guess a letter: z
Oops! You've already guessed that letter: _ 
-------------
You have 7 guesses left.
Available letters: abcdefghijklmnopqrstuvwxy
Please guess a letter: y
Good guess: y
------------
Congratulations, you won!
None
'''

#hangman('camel')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 5 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _ _ 
-------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: _ a_ e_ 
-------------
You have 8 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: i
Oops! That letter is not in my word: _ a_ e_ 
-------------
You have 7 guesses left.
Available letters: bcdfghjklmnopqrstuvwxyz
Please guess a letter: m
Good guess: _ ame_ 
-------------
You have 7 guesses left.
Available letters: bcdfghjklnopqrstuvwxyz
Please guess a letter: n
Oops! That letter is not in my word: _ ame_ 
-------------
You have 6 guesses left.
Available letters: bcdfghjklopqrstuvwxyz
Please guess a letter: l
Good guess: _ amel
-------------
You have 6 guesses left.
Available letters: bcdfghjkopqrstuvwxyz
Please guess a letter: k
Oops! That letter is not in my word: _ amel
-------------
You have 5 guesses left.
Available letters: bcdfghjopqrstuvwxyz
Please guess a letter: c
Good guess: camel
------------
Congratulations, you won!
None
'''

#hangman('guanabana')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 9 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: E
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 7 guesses left.
Available letters: abcdfghijklmnopqrstuvwxyz
Please guess a letter: O
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 6 guesses left.
Available letters: abcdfghijklmnpqrstuvwxyz
Please guess a letter: M
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 5 guesses left.
Available letters: abcdfghijklnpqrstuvwxyz
Please guess a letter: L
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 4 guesses left.
Available letters: abcdfghijknpqrstuvwxyz
Please guess a letter: R
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 3 guesses left.
Available letters: abcdfghijknpqstuvwxyz
Please guess a letter: S
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 2 guesses left.
Available letters: abcdfghijknpqtuvwxyz
Please guess a letter: T
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-------------
You have 1 guesses left.
Available letters: abcdfghijknpquvwxyz
Please guess a letter: Z
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
-----------
Sorry, you ran out of guesses. The word was guanabana .
None
'''

#hangman('senselessness')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 13 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ _ _ _ _ 
-------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: _ e_ _ e_ e_ _ _ e_ _ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: s
Good guess: se_ se_ ess_ ess
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrtuvwxyz
Please guess a letter: n
Good guess: sense_ essness
-------------
You have 7 guesses left.
Available letters: bcdfghijklmopqrtuvwxyz
Please guess a letter: l
Good guess: senselessness
------------
Congratulations, you won!
None
'''

#hangman('cheetah')
'''
Welcome to the game, Hangman!
I am thinking of a word that is 7 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: A
Good guess: _ _ _ _ _ a_ 
-------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: _ _ ee_ a_ 
-------------
You have 8 guesses left.
Available letters: bcdfghijklmnopqrstuvwxyz
Please guess a letter: z
Oops! That letter is not in my word: _ _ ee_ a_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrstuvwxy
Please guess a letter: t
Good guess: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: a
Oops! You've already guessed that letter: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: E
Oops! You've already guessed that letter: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: a
Oops! You've already guessed that letter: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: a
Oops! You've already guessed that letter: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: t
Oops! You've already guessed that letter: _ _ eeta_ 
-------------
You have 7 guesses left.
Available letters: bcdfghijklmnopqrsuvwxy
Please guess a letter: h
Good guess: _ heetah
-------------
You have 7 guesses left.
Available letters: bcdfgijklmnopqrsuvwxy
Please guess a letter: c
Good guess: cheetah
------------
Congratulations, you won!
None
'''