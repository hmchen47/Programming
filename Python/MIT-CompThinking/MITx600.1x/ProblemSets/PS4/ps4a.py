# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    assert (n > 0),'hand size "n" should greater than 0'
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]

    score *= len(word)

    if len(word) == n:
        score += 50
    assert not (score < 0),'Score less than 0'
    return score

#print getWordScore('abcd', 4)
#print getWordScore('abcd', 5)
#print getWordScore('', 3)
#print getWordScore('abc', 2)
#print getWordScore('', 10) 
#   0
#print getWordScore(qi, 7)
#   22
#print getWordScore(was, 7)
#   18
#print getWordScore(outgnaw, 7)
#   127
#print getWordScore(triplet, 7)
#   113
#print getWordScore(triplet, 8)
#   63
#print getWordScore(dogs, 4)
#   74
#print getWordScore(cats, 7)
#   24
#print getWordScore(kids, 5)
#   36
#print getWordScore(onomatopoeia, 12)
#   242

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1    
        # very important to add item into dict
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for letter in word:
        newHand[letter] -= 1
    return newHand

#print updateHand({'a': 1, 'i': 1, 'm': 1, 'l': 2, 'q': 1, 'u': 1}, 'quail')
#   {'m': 1, 'l': 1}
#print updateHand({'a': 2, 'c': 2, 'l': 2, 'p': 3, 'r': 2, 't': 2}, 'claptrap')
#   {'c': 1, 'l': 1, 'p': 1, 'r': 1, 't': 1}
#print updateHand({'g': 1, 'd': 1, 'o': 1}, 'dog')
#   {'o': 0, 'd': 0, 'g': 0}
#Re-testing last test to see if you mutate the original hand
#print updateHand({'g': 1, 'd': 1, 'o': 1}, 'dog') 
#   {'o': 0, 'd': 0, 'g': 0}
#print updateHand({'q': 3, 'i': 3, 'r': 3, 'e': 3, 't': 3, 'w': 3, 'p': 3, 'y': 3, 'u': 3, 'o': 3}, typewriter)
#   {'q': 3, 'i': 2, 'r': 1, 'e': 1, 't': 1, 'w': 2, 'p': 2, 'y': 2, 'u': 3, 'o': 3}
#print updateHand({'a': 1, 'b': 1, 'e': 1, 'f': 1, 'h': 1, 'k': 1, 'o': 1, 'r': 1, 'v': 1}, boar)
#   {'e': 1, 'f': 1, 'h': 1, 'k': 1, 'v': 1}
#Re-testing last test to see if you mutate the original hand
#print updateHand({'a': 1, 'b': 1, 'e': 1, 'f': 1, 'h': 1, 'k': 1, 'o': 1, 'r': 1, 'v': 1}, boar)
#   {'a': 0, 'b': 0, 'e': 1, 'f': 1, 'h': 1, 'k': 1, 'o': 0, 'r': 0, 'v': 1}
#print updateHand({'e': 4, 'h': 1, 'k': 1, 'q': 1, 's': 1, 't': 2}, teeth)
#   {'e': 2, 'k': 1, 'q': 1, 's': 1}
#Re-testing last test to see if you mutate the original hand
#print updateHand({'e': 4, 'h': 1, 'k': 1, 'q': 1, 's': 1, 't': 2}, teeth)
#   {'q': 1, 's': 1, 'e': 2, 't': 0, 'h': 0, 'k': 1}
#print updateHand({'a': 1, 'e': 1, 'f': 1, 'i': 1, 'p': 1, 'r': 1, 't': 1, 'w': 1, 'y': 1}, pear)
#   {'f': 1, 'i': 1, 't': 1, 'w': 1, 'y': 1}
#Re-testing last test to see if you mutate the original hand
#print updateHand({'a': 1, 'e': 1, 'f': 1, 'i': 1, 'p': 1, 'r': 1, 't': 1, 'w': 1, 'y': 1}, pear)
#   {'a': 0, 'e': 0, 'f': 1, 'i': 1, 'p': 0, 'r': 0, 't': 1, 'w': 1, 'y': 1}
#print updateHand({'a': 2, 'e': 1, 'l': 1, 'n': 1, 'q': 2, 't': 1}, tea)
#   {'a': 1, 'l': 1, 'n': 1, 'q': 2}
#Re-testing last test to see if you mutate the original hand
#print updateHand({'a': 2, 'e': 1, 'l': 1, 'n': 1, 'q': 2, 't': 1}, tea)
#   {'a': 1, 'q': 2, 'e': 0, 't': 0, 'l': 1, 'n': 1}


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # check word in hand
    newHand = hand.copy()
    for letter in word:
        if (letter not in hand) or newHand[letter] == 0:
            return False
        else:
            newHand[letter] -= 1

    # check the valid word
    if word not in wordList:
        return False

    return True

#print isValidWord(kwijibo, {'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 1}, wordList)
#   False
#print isValidWord(chayote, {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}, wordList)
#   False
#print isValidWord(hammer, {'a': 1, 'h': 1, 'r': 1, 'm': 2, 'e': 1}, wordList)
#   True
# Re-testing last test to see if you mutate the original hand
#   True
#print isValidWord(rapture, {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}, wordList)
#   False
#print isValidWord(milk, {'e': 1, 'i': 1, 'h': 1, 'k': 1, 'm': 1, 'l': 1, 'q': 1, 'y': 1}, wordList)
#   True
#Re-testing last test to see if you mutate the original hand
#   False
#print isValidWord(carrot, {'a': 1, 'b': 2, 'e': 1, 'l': 2, 'o': 1, 'q': 1, 's': 3, 'z': 1},  wordList)
#   False
#print isValidWord(hair, {'f': 1, 'i': 3, 'l': 1, 'o': 1, 'n': 2, 't': 1, 'w': 1, 'v': 1, 'y': 1},  wordList)
#   False
#print  isValidWord(duck, {'c': 1, 'e': 1, 'd': 2, 'i': 2, 'j': 1, 'm': 1, 'n': 1, 'r': 1, 't': 1, 'v': 1}, worldList)
#   False
#print isValidWord(milk, {'c': 1, 'f': 1, 'i': 1, 'k': 1, 'm': 1, 'l': 1, 'r': 1, 'z': 1}, wordList)
#   True
#Re-testing last test to see if you mutate the original hand
#   False
#isValidWord(coffee, {'a': 3, 'c': 1, 'd': 2, 'g': 1, 'k': 1, 'j': 1, 'l': 1, 'p': 1, 'w': 1}, wordList)
#   False
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for value in hand.values():
        handLen += value

    return handLen

#print calculateHandlen({'a': 1, 'b': 1})
#print calculateHandlen({'a': 1, 'c': 0, 'b': 1})
#print calculateHandlen({})
#print calculateHandlen({'y': 0, 'x': 0, 'z': 0})
#print calculateHandlen({'i': 1, 's': 1, 'z': 1, 't': 2, 'j': 2})
#print calculateHandlen({'a': 1, 'c': 1, 'b': 1, 'e': 1, 'm': 1, 'p': 3, 't': 1})
##   9
#print calculateHandlen({'b': 2, 'k': 1, 'j': 1, 'o': 1, 'r': 1, 'w': 1})
##   7
#print calculateHandlen({'e': 2, 'g': 1, 'f': 2, 'l': 1, 'q': 2, 'r': 1, 'u': 1, 't': 2, 'w': 2, 'z': 1})
##   15
#print calculateHandlen({'a': 2, 'b': 2, 'd': 1, 'g': 1, 'i': 1, 'k': 1, 'o': 2, 'n': 1, 's': 1, 't': 2, 'v': 1, 'x': 1})
##   16
#print calculateHandlen({'c': 1, 'd': 2, 'f': 1, 'i': 2, 'h': 1, 'k': 2, 'l': 1, 's': 1, 'w': 2, 'v': 1, 'x': 1})
##  15


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total = 0

    # As long as there are still letters left in the hand:
    
    while True:
        # Display the hand
        print 'Current Hand: ',
        for letter in hand.keys():
            for cnt in range(hand[letter]):
                print letter,
        print 
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print
                continue
            else:
            # Otherwise (the word is valid):
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total += getWordScore(word, n)

                print '"' + word + '" earned', getWordScore(word, n), \
                    'points. Total:', total, 'points. \n'
                
                # Update the hand 
                hand = updateHand(hand, word)

                if calculateHandlen(hand) == 0:
                    break
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print 'Run out of letters. Total score:', total, 'points.'
    else:
        print 'Goodbye! Total score:', total, 'points.'

#wordList = loadWords()

#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
#playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)

#playHand({'i': 1, 'k': 1, 'm': 1, 'l': 1}, '<edX internal wordList>', 4)
'''
Current Hand:  i k m l
Enter word, or a "." to indicate that you are finished: milk
"milk" earned 90 points. Total: 90 points. 

Run out of letters. Total score: 90 points.
None
'''

#playHand({'a': 1, 'z': 1}, '<edX internal wordList>', 2)
'''
Current Hand:  a z
Enter word, or a "." to indicate that you are finished: zo
Invalid word, please try again.

Current Hand:  a z
Enter word, or a "." to indicate that you are finished: za
"za" earned 72 points. Total: 72 points. 

Run out of letters. Total score: 72 points.
None
'''

#playHand({'q': 1, 'i': 1, 'o': 1}, '<edX internal wordList>', 3)
'''
Current Hand:  q i o
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 22 points. 

Current Hand:  o
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 22 points.
None
'''

#playHand({'y': 1, 'x': 2, 's': 1, 'z': 2, 'b': 1}, '<edX internal wordList>', 7)
'''
Current Hand:  y x x s z z b
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 0 points.
None
'''

#playHand({'a': 2, 'p': 1, 'r': 1, 'e': 2, 't': 1}, '<edX internal wordList>', 7)
'''
Current Hand:  a a p r e e t
Enter word, or a "." to indicate that you are finished: pear
"pear" earned 24 points. Total: 24 points. 

Current Hand:  a e t
Enter word, or a "." to indicate that you are finished: tea
"tea" earned 9 points. Total: 33 points. 

Run out of letters. Total score: 33 points.
None
'''

#playHand({'a': 2, 'p': 2, 'r': 1, 'z': 1, 'e': 1}, '<edX internal wordList>', 7)
'''
Current Hand:  a a p p r z e
Enter word, or a "." to indicate that you are finished: pear
"pear" earned 24 points. Total: 24 points. 

Current Hand:  a p z
Enter word, or a "." to indicate that you are finished: za
"za" earned 22 points. Total: 46 points. 

Current Hand:  p
Enter word, or a "." to indicate that you are finished: p
Invalid word, please try again.

Current Hand:  p
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.
None
'''

#playHand({'e': 1, 'k': 1, 'm': 1, 'l': 2, 'p': 1, 'u': 1, 'w': 1, 'x': 1, 'z': 1}, '<edX internal wordList>', 10)
'''
Current Hand:  e k m l l p u w x z
Enter word, or a "." to indicate that you are finished: l
Invalid word, please try again.

Current Hand:  e k m l l p u w x z
Enter word, or a "." to indicate that you are finished: chayote
Invalid word, please try again.

Current Hand:  e k m l l p u w x z
Enter word, or a "." to indicate that you are finished: kwijibo
Invalid word, please try again.

Current Hand:  e k m l l p u w x z
Enter word, or a "." to indicate that you are finished: plum
"plum" earned 32 points. Total: 32 points. 

Current Hand:  e k l w x z
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 32 points.
None
'''


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    hand = None
    while True:
        print
        game = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if game == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif game == 'r':
            if hand == None:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif game == 'e':
            break
        else: 
            print 'Invalid command.'


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
