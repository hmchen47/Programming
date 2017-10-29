# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    #print '\no =', s
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.
    # enpty dictionary for coder
    dict_coder = {}

    # this function use ord() to convert ascii into interger
    # however, space should be handled as an exception due to discontinuity
    # ord('A') = 65, ord('B') = 66, ..., ord('Z') = 90
    # ord('a') = 97, ord('b') = 98, ..., ord('Z') = 122
    # using 65 as the base_shift for upper cases to make these letters align to A 
    # using 97 as the base_shift for lower cases to make these letters align to a
    # i.e. ' ' = 0, 'a' = 1, 'b' = 2, ..., 'z' = 26
    baseC = 64
    baseL = 96
    letter_size = 27

    # dealing with lower cases
    # create mapping with given shift with cyclic buffer
    # dealing with space and letters
    for idx in range(letter_size):
        if idx == 0:
            key = ' '
        else:
            key = chr(idx+baseL)

        if (idx+shift) % letter_size == 0:
            value = ' '
        else:
            value =  chr(((idx+shift) % letter_size) + baseL)
        dict_coder[key] = value

    # dealing with upper cases
    for idx in range(letter_size):
        if idx != 0: 
            key = chr(idx+baseC)
            if (((idx+shift) % (letter_size)) == 0):
                value = ' '
            else:
                value = chr(((idx+shift) % (letter_size)) + baseC)
            dict_coder[key] = value

    return dict_coder

# print build_coder(3)

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    # make sure value of shift between 0 and 26
    if shift < 0 or shift > 27:
        print 'Please enter Shift with 0 <= shift < 27'
        return None

    # use build_coder fucntion t0 generate the crypto word
    return build_coder(shift)

# print build_encoder(3)


def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    # make sure that the value of shift between 0 and 26
    if shift < 0 or shift > 27:
        print 'Please enter Shift with 0 <= shift < 27'
        return None

    # apply build_coder with given negative shift as decorder
    return build_coder(-1*shift)

# print build_decoder(3)


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.
    '''
    create a temporary list to store the encode/decode text, then 
    join them together and return the joined string
    '''
    coded_text = ''
    for idx in range(len(text)):
        if coder.get(text[idx], 0) == 0:
            coded_text += text[idx]
        else: 
            coded_text += coder[text[idx]]

    return coded_text

# apply_coder("Hello, world!", build_encoder(3))
# Ans: 'Khoor,czruog!'

# apply_coder("Khoor,czruog!", build_decoder(3))
# Ans: 'Hello, world!'
  
def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.
    # call the encoder with shift to get encrypted word
    return apply_coder(text, build_encoder(shift))

# print apply_shift('This is a test.', 8)
# ans: 'Apq hq hiham a.'
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO
    # tmp_str: temporary string to store the decrypted string
    # max_valid: count of the maximum valid words
    # shift2Max: applied shift to get max_valid
    tmp_str = ''
    max_valid = 0
    shift2Max = -1

    # work through all shift by finding the best fit
    # 1. decode the encrypted string with the iterative shift
    # 2. split the decrypted string with spaces
    # 3. count how many valide words in the decrypted string
    # 4. record the shift with the maximum valid words
    for shift in range(27):
        cnt_valid = 0
        tmp_str = apply_coder(text, build_decoder(shift))
        words = tmp_str.split()
        for word in words:
            if is_word(wordlist, word):
                cnt_valid += 1
        if (cnt_valid > max_valid):
            shift2Max = shift

    return shift2Max

'''
s = apply_coder('Hello, world!', build_encoder(8))
print s
d = find_best_shift(wordlist, s)
print apply_coder(s, build_decoder(d))
'''
   
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    # read position and shift pairs from given list
    # apply the given shift from the given position to the end of string
    #print '\napply   =', shifts
    for pos, shift in shifts:
        coded_text = text
        coded_text = apply_coder(text[pos:], build_encoder(shift))
        newtext = text[:pos] + coded_text
        text = newtext

    return text
 
#print apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])



def apply_rshifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    # read position and shift pairs from given list
    # apply the given shift from the given position to the end of string
    #print "reverse =", shifts
    for pos, shift in shifts:
        coded_text = text
        coded_text = apply_coder(text[pos:], build_decoder(shift))
        newtext = text[:pos] + coded_text
        text = newtext

    return text

#
# Problem 4: Multi-level decryption.
#

def find_best_shifts_rec(wordlist, text, start):
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


s = random_scrambled(wordlist, 10)
#print 's =', s
shifts = find_best_shifts(wordlist, s)
print 'shifts=', shifts
#print 'd =',
print apply_rshifts(s, shifts)
print '\n'
#s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
#shifts = find_best_shifts(wordlist, s)
#print apply_rshifts(s, shifts)
#print '\n\n'


def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.
    fable = get_fable_string()

    shifts = find_best_shifts(wordlist, fable)

    print apply_rshifts(fable, shifts)

#if __name__ == '__main__':

#    decrypt_fable()
    
#What is the moral of the story?
#
#
#
#
#

'''
An Ingenious Man who had built a flying machine invited a great concourse of people to see it go up. at the appointed moment, everything being ready, he boarded the car and turned a a he power. the machine immediately broke through the massive substructure upon which it was builded, and sank out of sight into the earth, the aeronaut springing out barely in time to save himself. "well," said he, "i have done enough to demonstrate the correctness of my details. the defects," he added, with a add hat the ruined brick work, "are merely basic and fundamental." upon this assurance the people came ox ward with subscriptions to build a second machine
'''