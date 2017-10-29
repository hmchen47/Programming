#!/us/bin/python
# -*- coding: utf-8 -*-

# Exercise 11.1 
# Write a simple program to simulate the operation of the the grep
# command on Unix. Ask the user to enter a regular expression and 
# count the number of lines that matched the regular expression:
#
#	$ python grep.py
#	Enter a regular expression: ˆAuthor
#	mbox.txt had 1798 lines that matched ˆAuthor
# 
#	$ python grep.py
#	Enter a regular expression: ˆX-
#	mbox.txt had 14368 lines that matched ˆX-
#
#	$ python grep.py
#	Enter a regular expression: java$
#	mbox.txt had 4218 lines that matched java$
# 
# The code can be used by Python 3

import re

fhandle = open('mbox.txt')

#argv = raw_input("Enetr a regular expression: ")
argv = input("Enetr a regular expression: ")

cnt = 0
for line in fhandle:
	tmp = re.findall(argv, line)
	if len(tmp) > 0:
		cnt += 1

print ("mbox.txt had {} lines that matched {}".format(cnt, argv))
