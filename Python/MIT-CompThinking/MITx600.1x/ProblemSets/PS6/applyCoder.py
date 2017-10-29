#!/usr/bin/env python
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

def applyCoder(text, coder):
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


#print applyCoder('Hello, world!', buildCoder(14))
#   'Vszzc, kcfzr!'
#print applyCoder('Hello, world!', buildCoder(6))
#   'Nkrru, cuxrj!'
#print applyCoder('Hello, world!', buildCoder(0))
#   'Hello, world!'
#print applyCoder('Hello, world!', buildCoder(11))
#   'Spwwz, hzcwo!'
#print applyCoder('The quiz is... hard!', buildCoder(14))
#   'Hvs eiwn wg... vofr!'
#print applyCoder('The quiz is... hard!', buildCoder(6))
#   'Znk waof oy... ngxj!'
#print applyCoder('The quiz is... hard!', buildCoder(0))
#   'The quiz is... hard!'
#print applyCoder('The quiz is... hard!', buildCoder(11))
#   'Esp bftk td... slco!'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(14))
#   '12 xoqyrokg eiwnnsr am gdvwbl!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(6))
#   '12 pgiqjgcy waoffkj se yvnotd!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(0))
#   '12 jackdaws quizzed my sphinx!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(11))
#   '12 ulnvolhd bftkkpo xj dastyi!?'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(14))
#   '?DXz4;M8K73UkEpnreOuwZvWg.ILlA'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(6))
#   '?VPr4;E8C73McWhfjwGmoRnOy.ADdS'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(0))
#   '?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(11))
#   '?AUw4;J8H73RhBmkobLrtWsTd.FIiX'


#print applyCoder("Hello, world!", buildCoder(3))
#print
#print applyCoder("Khoor, zruog!", buildCoder(23))