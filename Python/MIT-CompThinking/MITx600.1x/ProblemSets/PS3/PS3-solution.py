##RADIATION EXPOSURE
## code
def radiationExposure(start, stop, step):
    ans,i = 0,0
    while (start+(i*step))<stop:
        ans += f(start+(i*step))*step
        i += 1
    return ans  

##HANGMAN PART 1: IS THE WORD GUESSED
##I have used set module in my code. Please read about it here, if you are not familiar with it.
## code 
def isWordGuessed(secretWord, lettersGuessed):
    return set(list(secretWord)).issubset(set(lettersGuessed))  

##PRINTING OUT THE USER'S GUESS
## code     
def getGuessedWord(secretWord, lettersGuessed):
    word = ""
    for i in secretWord:
        word += i if i in lettersGuessed else "_"
    return word          

##PRINTING OUT ALL AVAILABLE LETTERS
## code     
def getAvailableLetters(lettersGuessed):
    rem = set(list(string.ascii_lowercase)) - set(lettersGuessed)
    return "".join(str(i) for i in sorted(rem))        

##HANGMAN PART 2: THE GAME/COMPLEX TESTS
## code    
def hangman(secretWord):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    breaker = "-----------"
    print breaker
    guesses = 8
    lettersGuessed = []

    while (isWordGuessed(secretWord,lettersGuessed)==False and guesses!=0):
        print "You have " + str(guesses) + " guesses left."
        print "Available Letters: " + str(getAvailableLetters(lettersGuessed))
        usrInp = raw_input("Please guess a letter: ").lower()
        if usrInp in lettersGuessed:
            print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed))
        elif usrInp in secretWord:
            lettersGuessed.append(usrInp)
            print "Good guess: "+str(getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(usrInp)
            guesses -= 1
            print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed))
        print breaker

    if guesses == 0:
        print "Sorry, you ran out of guesses. The word was "+str(secretWord)
    else:
        print "Congratulations, you won!"

