#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    dict_coder = {}

    # this function use ord() to convert ascii into interger
    # however, space should be handled as an exception due to discontinuity
    # ord('A') = 65, ord('B') = 66, ..., ord('Z') = 90
    # ord('a') = 97, ord('b') = 98, ..., ord('Z') = 122
    # using 65 as the base_shift for upper cases to make these letters align to A 
    # using 97 as the base_shift for lower cases to make these letters align to a
    # i.e. ' ' = 0, 'a' = 1, 'b' = 2, ..., 'z' = 26
    baseC = 65
    baseL = 97
    letter_size = 26

    # dealing with lower cases
    # create mapping with given shift with cyclic buffer
    # dealing with space and letters
    for idx in range(letter_size):
        key = chr(idx+baseL)

        #if (idx+shift) % letter_size == 0:
        #    value = 'z'
        #else:
        #print chr(idx+baseL), chr(((idx+shift) % letter_size) + baseL)
        value =  chr(((idx+shift) % letter_size) + baseL)    
        dict_coder[key] = value

    # dealing with upper cases
    for idx in range(letter_size):
        key = chr(idx+baseC)
        #if (idx+shift) % letter_size == 0:
        #    value = 'Z'
        #else:
            
        #print chr(idx+baseC), chr(((idx+shift) % letter_size) + baseC)
        value = chr(((idx+shift) % (letter_size)) + baseC)
        dict_coder[key] = value

    return dict_coder

#print buildCoder(0)
#print buildCoder(5)
print buildCoder(24)
#print buildCoder(13)
#print buildCoder(9)

#print buildCoder(3)
#print
#print buildCoder(9)