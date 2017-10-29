#!/usr/bin/python
# _*_ coding = UTF-8 _*_

from ps4a import *
import time

def _isValidWord(word, hand):
    """
    Returns True if word is entirely composed of 
    letters in the hand. Otherwise, returns False.
    Does not mutate hand.
   
    word: string
    hand: dictionary (string -> int)
    """
    valid = True
    hand_copy = hand.copy()

    for letter in word:
        hand_copy[letter] = hand_copy.get(letter, 0) - 1                            
        if hand_copy[letter] < 0:
            valid = False
            break           
    return valid          

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.
    This word should be calculated by considering all the words
    in the wordList.
    If no words in the wordList can be made from the hand, return None.
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: string or None
    """
  
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if _isValidWord(word,hand):
            # Find out how much making that word is worth
            score = getWordScore(word,n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0    
    hand_copy = hand.copy()
    
    while (calculateHandlen(hand_copy) > 0):
        print 'Current Hand: ', 
        displayHand(hand_copy)
        c_word = compChooseWord(hand_copy, wordList, n)       
        if c_word == None:
            break
        total_score += getWordScore(c_word, n)
        hand_copy = updateHand(hand_copy, c_word)
        print '"' + c_word + '" earned ' + str(getWordScore(c_word, n)) + ' points. Total: ' + str(total_score) + ' points.'
        print
    print 'Total score: ' + str(total_score) + ' points.'    
#
# Problem #8: Playing a game
#
#
def _playHand(user_hand, wordList, HAND_SIZE):
    comp_input = ''
    while True:                
        comp_input = raw_input('Enter u to have yourself play, c to have the computer play: ')
        if str(comp_input) == 'u':
            playHand(user_hand, wordList, HAND_SIZE)
            break
        elif str(comp_input) == 'c':
            compPlayHand(user_hand, wordList, HAND_SIZE)
            break
        else:
            print 'Invalid command.'  

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.
    4) After the computer or user has played the hand, repeat from step 1
    wordList: list (string)
    """
    user_hand = {}     
    
    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')        
        if str(user_input) == 'n':
            user_hand = dealHand(HAND_SIZE)
            _playHand(user_hand, wordList, HAND_SIZE) 
        elif str(user_input) == 'r':
            if user_hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
                print
            else:
                 _playHand(user_hand, wordList, HAND_SIZE)                          
        elif str(user_input) == 'e':
            return
        else:
           print 'Invalid command.'         
   
  
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
