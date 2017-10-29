from ps4a import *
import time


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
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word

    # return the best word you found.
    return bestWord


#wordList = loadWords()
#print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
#   apples or appels
#print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
#   acta
#print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
#   immanent
#print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
#   None

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
    # the code is revised from playHand(hand, wordList, n) in ps4a.py
    total = 0
    
    while True:
        print '\nCurrent Hand: ',
        for letter in hand.keys():
            for cnt in range(hand[letter]):
                print letter,
        print 
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        else:
            # check validation of the word and calculate its score
            if not isValidWord(word, hand, wordList):
                # should not print the message, computer goes for the next word
                #print 'Invalid word, please try again.'
                #print
                continue
            else:
                total += getWordScore(word, n)

                print '"' + word + '" earned', getWordScore(word, n), \
                    'points. Total:', total, 'points.'
                
                hand = updateHand(hand, word)

                if calculateHandlen(hand) == 0:
                    break
    print 'Total score:', total, 'points.'


#wordList = loadWords()
#compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
#compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
#compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
#compPlayHand({'a': 1, 'c': 1, 'h': 1, 'o': 1, 'x': 1, 'w': 2}, wordList, 7)

#hand = dealHand(10)
#compPlayHand(hand, wordList, 10)

#compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
'''
Current Hand:  a p p s e l
"appels" earned 110 points. Total: 110 points.
Total score: 110 points.

None
'''
#compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
'''
Current Hand:  a a c b t
"acta" earned 24 points. Total: 24 points.

Current Hand:  b
Total score: 24 points.

None
'''
#compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
'''
Current Hand:  a a e e i i m m n n t t
"imamate" earned 77 points. Total: 77 points.

Current Hand:  e t i n n
"in" earned 4 points. Total: 81 points.

Current Hand:  e t n
Total score: 81 points.

None
'''
#compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 8)
'''
Current Hand:  a p p s e l
"appels" earned 60 points. Total: 60 points.
Total score: 60 points.

None
'''
#compPlayHand({'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 2}, wordList, 8)
'''
Current Hand:  b i i k j o w w
"koji" earned 60 points. Total: 60 points.

Current Hand:  b w w i
"bi" earned 8 points. Total: 68 points.

Current Hand:  w w
Total score: 68 points.

None
'''
#compPlayHand({'a': 1, 'g': 1, 'i': 1, 'n': 2, 'q': 1, 't': 1, 'y': 1}, wordList, 8)
'''
Current Hand:  a g i n n q t y
"ayin" earned 28 points. Total: 28 points.

Current Hand:  q t g n
Total score: 28 points.

None
'''
#compPlayHand({'c': 2, 'r': 2, 't': 1, 'f': 1}, wordList, 8)
'''
Current Hand:  c c r r t f
Total score: 0 points.

None
'''
#compPlayHand({'a': 1, 'd': 1, 'i': 1, 'j': 1, 'o': 3, 'n': 2, 'p': 1, 'r': 1, 'w': 1}, wordList, 12)
'''
Current Hand:  a d i j o o o n n p r w
"jow" earned 39 points. Total: 39 points.

Current Hand:  a d i o o n n p r
"danio" earned 30 points. Total: 69 points.

Current Hand:  o n p r
"no" earned 4 points. Total: 73 points.

Current Hand:  p r
Total score: 73 points.

None
'''


#
# Problem #8: Playing a game
#
#
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
    hand = None
    while True:
        print
        game = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if game == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                player = raw_input('\nEnter u to have yourself play, c to have the computer play: ')
                if player == 'u':
                    print
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif player == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif game == 'r':
            if hand == None:
                print 'You have not played a hand yet. Please play a new hand first!'            
            else: 
                player = raw_input('\nEnter u to have yourself play, c to have the computer play: ')
                while True:
                    if player == 'u':
                        print
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif player == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print 'Invalid command.'
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


'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  a c b
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  y x z
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  a z
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  q i
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  d o
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  a a m
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  c r
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  e l l
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  a b t o
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  a b t o
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  a a r m t
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  a a r m t
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  b e e f l o t t z
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  b e e f l o t t z
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  b e e f l o t t z
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: u

Hand passed to playHand:  b e e f l o t t z
<playHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: y
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: z
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: k
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: s
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: w
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''

'''
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: x
Invalid command.

Enter u to have yourself play, c to have the computer play: y
Invalid command.

Enter u to have yourself play, c to have the computer play: z
Invalid command.

Enter u to have yourself play, c to have the computer play: k
Invalid command.

Enter u to have yourself play, c to have the computer play: s
Invalid command.

Enter u to have yourself play, c to have the computer play: w
Invalid command.

Enter u to have yourself play, c to have the computer play: c
Hand passed to compPlayHand:  a a a i i j q s t v
<compPlayHand execution not shown for grading brevity>

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
'''