#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 49: Making Sentences

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, excepting):
    if word_list:
        word = word_list.pop(0)
    
        if word[0] == expecting:
            return word 
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) = 'verb':
        return match(word_list, 'verb')
    else:
        riase ParseError("Expectd a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')

    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise PareseError("Expected a noun or a direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb:
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        riase ParseError("Must start with subject, object, or verb not: %s" % start)


"""
Study Drills
1. Change the parse_ methods and try to put them into a class rather than be just 
    methods. Which design do you like better?
2. Make the parser more error-resistant so that you can avoid annoying your users if 
    they type words your lexicon doesn't understand.
3. Improve the grammar by handling more things like numbers.
4. Think about how you might use this Sentence class in your game to do more fun things 
    with a user's input.
"""


