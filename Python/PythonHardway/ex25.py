#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 25: Even More Practice

def break_words(stuff):
    """This fucntion will break up wpords for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sortes the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


if __name__ == "__main__":
    sentence = "All good things come to those who wait."
    words = break_words(sentence)

    print(words)

    sorted_words = sort_words(words)
    print(sort_words)

    print_first_word(words)
    print_last_word(words)

    # sorted_words = sort_sentence(sentence)
    # print(sorted_words)


    # print_first_and_last(sentence)
    # print_first_and_last_sorted(sentence)



# Study Drills
# 1. Take the remaining lines of the What You Should See output and figure out what 
#       they are doing. Make sure you understand how you are running your functions in 
#       the ex25 module.
# 2. Try doing this: help(ex25) and also help(ex25.break_words). Notice how you get
#       help for your module, and how the help is those odd """ strings you put after 
#       each function in ex25? Those special strings are called documentation comments 
#       and we'll be seeing more of them.
# 3. Typing ex25. is annoying. A shortcut is to do your import like this: from ex25 
#       import * which is like saying, "Import everything from ex25." Programmers like 
#       saying things backward. Start a new session and see how all your functions are 
#       right there.
# 4. Try breaking your file and see what it looks like in python when you use it. You 
#       will have to quit python with quit() to be able to reload it.

"""
Python 2.7.11 (default, May 11 2016, 07:52:17) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
"""