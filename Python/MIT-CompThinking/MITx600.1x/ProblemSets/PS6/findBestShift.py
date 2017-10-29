def findBestShiftsRec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    ### TODO.
    # iterate the shift from 0 to 27
    #   decrypted the given text with the iterated shift
    #   using split function to get words 
    #   iterate through the words
    #       evaluate the words with is_word() function
    #       if the words are valid append to a tuple and call self
    #           with start of the invalid word
    #       if first word is not valid, use the next shift

    tmpstr = text[start:]
    decryptStr = ''
    
    #print '\n'
    for shift in range(27):
        cnt_valid = 0
        decryptStr = apply_coder(tmpstr, build_decoder(shift))
        words = decryptStr.split()

        for word in words:
            # check each word with validation and 
            # count how many valid words
            if is_word(wordlist, word):
                cnt_valid += 1
            else:
                break

        #print 'sh=', shift, ' decStr:', decryptStr, 'words=', words

        # judge going deeper? if still un-decrypted word go deeper
        curText = ''
        if cnt_valid >= 1:
            # valid words exists
            if cnt_valid == len(words):
                #print 'final words =', words
                # all words decrypted
                return [(start, shift)]
            else:
                ''' the encryption algorithm apply to each word than a 
                    couple of words, therefore, the decryption algorithm
                    should of that '''
                wordsLen = len(words[0]) + 1

                '''
                #still words left, call self
                # counting the length of words and spaces first
                wordsLen = 0
                for idx in range(cnt_valid):
                    #print 'valid word =', words[idx]
                    wordsLen += (len(words[idx]) + 1)
                '''
                #print '\nfor next =', text[:start]+decryptStr
                next_valid = \
                    find_best_shifts_rec(wordlist, text[:start]+decryptStr, start+wordsLen)
                #print 'next =', next_valid
                if (next_valid == None):
                    # not a correct one due to next level undecrypted
                    # if the last shift than return None otherwise
                    # go for next shift
                    #print '\nrevert with shift =', shift
                    if shift == 26:
                        return None
                else:
                    # next level is valid
                    #print 'tuple', [(start, shift)] + next_valid
                    return [(start, shift)] + next_valid


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    # basically pass the work to find_best_shift_rec fucntion 
    # with the start at 0

    shiftPos = find_best_shifts_rec(wordlist, text, 0)
    #print '\nshifts =', shiftPos
    return shiftPos


#s = applyShift('Hello, world!', 8)
#s
#findBestShift(wordList, s)
#applyShift(s, 18)