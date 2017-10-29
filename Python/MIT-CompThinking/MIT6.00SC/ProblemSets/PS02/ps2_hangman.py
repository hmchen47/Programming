# 6.00 Problem Set 3
# 
# Hangman
#

# Problem Set 2 - Hangman
# Name: Fred Chen
# Collaborators: None
# Time Spent: 3:00

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

# print welcome message
print 'Welcome to the game, Hangman!'
target_word = choose_word(wordlist)
print 'I am thinking of a word that is', len(target_word), 'letters long.'

cnt_guest = min(20, 2 * len(target_word))
lst_target = ['_'] * len(target_word)

lst_available = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while (cnt_guest > 0):
    # print current guest information
    print '\n-------------'
    print 'You have', cnt_guest, 'guesses left.'
    letters = 'Available letters: '
    for i in range(len(lst_available)):
        letters += lst_available[i]
    print letters

    # invite to have an input but limit to one character
    guest = ''
    while(len(guest) != 1):
        guest = raw_input('Please guess a letter: ')

    # print the feedback information
    reveal = ''
    if (guest in target_word):
        for idx in range(len(lst_target)):
            if (target_word[idx] == guest):
                lst_target[idx] = guest
        for idx in range(len(lst_target)):
            reveal += lst_target[idx]
        print 'Good guess:', reveal
    else: 
        for idx in range(len(lst_target)):
            reveal += lst_target[idx]
        print 'Oops! That letter is not in my word:', reveal

    # post processing for next run
    cnt_guest -= 1
    if (guest in lst_available):
        lst_available.remove(guest)

print 'The word is', target_word