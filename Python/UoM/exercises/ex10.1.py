#!/usr/bin/python
# -*- coding: utf-8 -*-

# Exercise 10.1 
# Revise a previous program as follows: Read and parse the “From” lines and 
# pull out the addresses from the line. Count the number of messages from 
# each person using a dictionary.
# After all the data has been read print the person with the most commits 
# by creating a list of (count, email) tuples from the dictionary and then 
# sorting the list in reverse order and print out the person who has the 
# most commits.
#
# Sample Line:
#   From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
#   Enter a file name: mbox-short.txt
#   cwen@iupui.edu 5
#   Enter a file name: mbox.txt
#   zqian@umich.edu 195

fname = raw_input("Enter a file name: ")

if len(fname) == 0: fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except IOError as e:
    print "IO error {0}: {1}".format(e.errno, e.strerror)
    exit()

email_d = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        email_d[words[1]] = email_d.get(words[1], 0) + 1

email_lst = list()
email_tup = tuple()
for (key, val) in email_d.items():
    email_tup = email_tup + ((val, key),)
    email_lst.append((val, key))

email_tup = sorted(email_tup, reverse = True)
email_lst.sort(reverse=True)

print email_tup
print ""
print email_lst


