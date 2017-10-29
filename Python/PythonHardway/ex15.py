#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 15: Reading Files

"""
usage: python3 ex15.py ex15_sample.txt
"""

from sys import argv

script, filename = argv     # take the arguments

txt = open(filename)        # open the file

print("here's your life %r: " % filename)   # print information
print(txt.read())           # read all text from the given file

txt.close()

print("Type the filename again:")
file_again = input("> ")    # read file with the input

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()


"""
Study Drills
1. Above each line, write out in English what that line does.
2. If you are not sure ask someone for help or search online. Many times searching for 
    "python THING" will find answers to what that THING does in Python. Try searching 
    for "python open."
3. I used the word "commands" here, but commands are also called "functions" and 
    "methods." You will learn about functions and methods later in the book.
4. Get rid of the lines 10-15 where you use raw_input and run the script again.
5. Use only raw_input and try the script that way. Why is one way of getting the 
    filename better than another?
6. Start python to start the python shell, and use open from the prompt just like in 
    this program. Notice how you can open files and run read on them from within python?
7. Have your script also call close() on the txt and txt_again variables. It's 
    important to close files when you are done with them.
"""

