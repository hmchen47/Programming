# 6.00 Problem Set 2
# 
# Hangman
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>

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
def hangman():
    """Runs the hangman game"""
    hidden_word = choose_word(wordlist).lower()
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is %d letters long" %(len(hidden_word))
    incorrect_guesses = 8
    used_letters = {}
    while(True):
        print "-----------"
        print "You have %d guesses left" %(incorrect_guesses)
        print "Available Letters: " + get_available_letters(used_letters)
        new_letter = request_letter(hidden_word, used_letters)
        if new_letter in hidden_word:
            print "Good guess: " + get_hidden_word(hidden_word, used_letters)
        else:
            print "Oops! That letter is not in my word " \
                  + get_hidden_word(hidden_word, used_letters)
            incorrect_guesses -= 1
            if incorrect_guesses == 0:
                print "Sorry, you ran out of guesses. The word was " \
                + hidden_word + ". Play again!"
                break
        print
        if found_hidden_word(hidden_word, used_letters):
            print "Congratulations, you won!"
            break

def get_hidden_word(hidden_word, used_letters):
    """Returns a string of the form __ad___ by filling in correct guesses"""
    visible_word = ""
    for letter in hidden_word:
        if letter in used_letters:
            visible_word += letter
        else:
            if len(visible_word) > 0 and visible_word[-1] == '_':
                visible_word += " "
            visible_word += "_"
    return visible_word

def found_hidden_word(hidden_word, used_letters):
    """Returns True if the word has been completely uncovered"""
    for letter in hidden_word:
        if letter not in used_letters:
            return False
    return True

def get_available_letters(used_letters):
    """Returns a list of lowercase letters not in used_letters"""
    available_letters = ""
    for letter in string.lowercase:
        if letter not in used_letters:
            available_letters += letter
    return available_letters


def request_letter(hidden_word, used_letters):
    """Asks for another guess and returns (gameover, victory) """
    new_letter = raw_input("Please guess a letter: ").lower()
    used_letters[new_letter] = 1
    return new_letter

hangman()
