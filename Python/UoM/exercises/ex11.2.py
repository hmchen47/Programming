#!/us/bin/python
# -*- coding: utf-8 -*-

# Exercise 11.2 
# Write a program to look for lines of the form
#
#	New Revision: 39772
# 
# And extract the number from each of the lines using a regular 
# expression and the findall() method. Compute the average of the 
# numbers and print out the average.
#
#	Enter file:mbox.txt
#	38549.7949721
#
#	Enter file:mbox-short.txt
#	39756.9259259

import re

#fname = raw_input("Enter file: ")
fname = input("Enter file: ")

try:
	fhandle = open(fname)
except IOError as e:
	print ("IO Error ({}): {}".format(e.errno, e.strerror))
	exit()

rcd = list()
sum = 0.0
cnt = 0
for line in fhandle:
	tmp = re.findall('^New Revision:', line)
	if len(tmp) > 0:
		words = line.split()
		rcd.append(float(words[2]))
		sum += float(words[2])
		cnt += 1

print ("{}".format(sum/cnt))

