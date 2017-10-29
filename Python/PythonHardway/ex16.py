#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 16: Reading and Writing Files

"""
usage: python3 ex16.py test.txt

Mary had a little lamb
Its fleece was white as snow
It was also tasty
"""

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("? ")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")

print("Now, I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

"""
Study Drills
1. If you do not understand this, go back through and use the comment trick to get it 
    squared away in your mind. One simple English comment above each line will help you 
    understand or at least let you know what you need to research more.
2. Write a script similar to the last exercise that uses read and argv to read the file 
    you just created.
3. There's too much repetition in this file. Use strings, formats, and escapes to print 
    out line1, line2, and line3 with just one target.write() command instead of six.
4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to 
    be safe by making you explicitly say you want to write a file.
5. If you open the file with 'w' mode, then do you really need the target.truncate()? 
    Read the documentation for Python's open function and see if that's true.

NB:
The + modifier, 'w+', 'r+', and 'a+', will open the file in both read and write mode, 
    and depending on the character use position the file in different ways.
"""