#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 49: Making Sentences

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

