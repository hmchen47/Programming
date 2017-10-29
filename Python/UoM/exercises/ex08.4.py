#!/usr/bin/python
#
# Exercise 8.4 
# Download a copy of the file from www.py4inf.com/code/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split 
# function. For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list.
#
# When the program completes, sort and print the resulting words in 
# alphabetical order.
#
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already','and', 'breaks', 
# 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 
# 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']
#

fname = raw_input("Enter file: ")

try:
    fhandle = open(fname)
except IOError as e:
    print "IOError({0}): {1}".format(e.errno, e.strerror)
    exit()

words = list()
for line in fhandle:
    lwords = line.split()
    for wrd in lwords:
        if (len(words) == 0):
            words.append(wrd)
        elif (wrd not in words):
            words.append(wrd)
           
words.sort()
print words
