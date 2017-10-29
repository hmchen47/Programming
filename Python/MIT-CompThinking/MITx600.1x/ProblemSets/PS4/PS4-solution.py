WORD SCORES
## code
def getWordScore(word, n):
    score = sum(SCRABBLE_LETTER_VALUES[i] for i in word.lower()) * len(word)
    return score if len(word) != n else score+50            
DEALING WITH HANDS
## code 
def updateHand(hand, word):
    hand1 = hand.copy()
    for i in word:
        hand1[i] -= 1 if i in hand1 else None
    return hand1       
VALID WORDS
## code 
def isValidWord(word, hand, wordList):
    if word=="" or word not in wordList:
        return False
    hand1 = hand.copy()
    for i in word:
        if hand1.get(i,0) == 0:
            return False
            break
        else:
            hand1[i] -= 1
    else:
        return True
HAND LENGTH
## code
def calculateHandlen(hand):
    return sum(hand[i] for i in hand)         
PLAYING A HAND
## code
def playHand(hand, wordList, n):
    score = 0
    while calculateHandlen(hand)!=0:
        print "Current Hand: ", displayHand(hand)
        word = raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        if word == ".":
            print "Goodbye! Total score: " + str(score) + " points."
            break
        elif isValidWord(word, hand, wordList) is False:
            print "Invalid word, please try again.\n"
        else:
            tmp = getWordScore(word, n)
            score += tmp
            hand = updateHand(hand, word)
            print "\"" + str(word) + "\" earned " + str(tmp) + " points. Total: " + str(score) + " points\n"
    else:
        print "Run out of letters. Total score: " + str(score) + " points."
PLAYING A GAME
## code    
def playGame(wordList):
    flag = 0
    inp = ""

    while inp!="e":
        inp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if inp == "r":
            if flag == 0:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif inp == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            flag = 1
        elif inp != "e":
            print "Invalid command."       
COMPUTER CHOOSES A WORD
## code 
def compChooseWord(hand, wordList, n):
    maxSc = 0
    reqWord = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            tmp = getWordScore(word, n)
            if tmp > maxSc:
                maxSc = tmp
                reqWord = word
    return reqWord     
COMPUTER PLAYS A HAND
## code 
def compChooseWord(hand, wordList, n):
    maxSc = 0
    reqWord = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            tmp = getWordScore(word, n)
            if tmp > maxSc:
                maxSc = tmp
                reqWord = word
    return reqWord

def compPlayHand(hand, wordList, n):
    word = ""
    score = 0
    while word != None and calculateHandlen(hand) != 0:
        print "Current Hand:", 
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word != None:
            tmp = getWordScore(word, n)
            score += tmp
            hand = updateHand(hand, word)
            print "\"" + str(word) + "\" earned " + str(tmp) + " points. Total: " + str(score) + " points\n"
    else:
        print "Total score: " + str(score) + " points."
YOU AND YOUR COMPUTER
## code   
def usrComp(hand, wordList):
    inp = None
    while inp != "u" and inp != "c":
        inp = raw_input("\nEnter u to have yourself play, c to have the computer play: ")
        if inp == "u":
            playHand(hand, wordList, HAND_SIZE)
        elif inp == "c":
            compPlayHand(hand, wordList, HAND_SIZE)
        else:
            print "Invalid command.\n"

def playGame(wordList):
    inp = None
    flag = 0
    while inp != "e":
        inp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if inp == "n":
            flag = 1
            hand = dealHand(HAND_SIZE)
            usrComp(hand, wordList)
        elif inp == "r":
            if flag == 0:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                usrComp(hand, wordList)
        elif inp != "e":
            print "Invalid command.\n"