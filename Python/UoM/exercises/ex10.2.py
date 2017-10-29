#!/usr/bin/python
# -*- coding: utf-8 -*-

#Exercise 10.2 
# This program counts the distribution of the hour of the day for each 
# of the messages. You can pull the hour from the “From” line by finding 
# the time string and then splitting that string into parts using the 
# colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.
#
# Sample Execution:
#   python timeofday.py
#   Enter a file name: mbox-short.txt
#   04 3
#   06 1
#   07 1
#   09 2
#   10 3
#   11 6
#   14 1
#   15 2
#   16 4
#   17 2
#   18 1
#   19 1

fname = raw_input("Enter a file name: ")

#if len(fname) == 0: fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except IOError as e:
    print "IO Errro {0}: {1}".format(e.errno, e.strerror)
    exit()

hrdict = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        hrstr = words[5].split(':')
        hrdict[hrstr[0]] = hrdict.get(hrstr[0], 0) + 1

hrlst = hrdict.items()

#hrlst = list()
#for (key, val) in hrdict.items():
#    hrlst.append((val, key))

hrlst.sort()

for (key, val) in hrlst:
    print key, val
