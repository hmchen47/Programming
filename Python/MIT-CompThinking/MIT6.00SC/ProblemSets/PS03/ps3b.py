from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    for idx in range(HAND_SIZE):
        words = get_perms(hand, HAND_SIZE - idx)
        for word in words:
            if word in word_list:
                return word

    return None

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    # display the hand
    word = None
    global total_score
    total_score = 0

    print '\n'
    invalid = True
    handsize = 1
    while (invalid):
        print '\nCurrent Hand:', 
        for key in hand:
            for cnt in range(hand[key]):
                print key,
        print 

        word = comp_choose_word(hand, word_list)
        if word == None:
            break

        if is_valid_word(word, hand, word_list):
            total_score += get_word_score(word, handsize)
            print 'Computer:', word, 'earned', get_word_score(word, handsize), 'points. Total:', total_score, 'points'

            # use these characters
            update_hand(hand, word)

    handsize += 1
    print '\nTotal score:', total_score, 'points.'

    print '\n'


#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    play = True
    while(play):
        game_instruct = raw_input('Please enter - n (new hand); r (replay); e (exit game): ')
        if game_instruct in ['n', 'r']:
            who_play = raw_input('Who plays - c (computer); u (user): ')
        if game_instruct == 'n':
            hand = deal_hand(HAND_SIZE)
            old_hand = dict(hand)
            if who_play == 'u':
                play_hand(hand, word_list)
            elif who_play == 'c':
                comp_play_hand(hand, word_list)
            else:
                print 'Invalid input - only "u" and "c" allowed'
        elif game_instruct == 'r':
            hand = dict(old_hand)
            if who_play == 'u':
                play_hand(hand, word_list)
            elif who_play == 'c':
                comp_play_hand(hand, word_list)
            else:
                print 'Invalid input - only "u" and "c" allowed'
        elif game_instruct == 'e':
            play = False
        else:
            print "\nInvalid input, please try again.\n"

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
