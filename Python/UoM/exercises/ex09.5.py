#!/use/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.5 
# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from 
# (i.e. the whole e-mail address). At the end of the program print out 
# the contents of your dictionary.
#
# python schoolcount.py
#   Enter a file name: mbox-short.txt
#   {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#   'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = raw_input("Enter a file name: ")
try:
    fhandle = open(fname)
except IOError as e:
    print "IO error ({0}): {1}".format(e.errno, e.strerror)

domain_d = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        for letter in words[1]:
            atpos = words[1].find('@')
            domain = words[1][atpos+1:]
        domain_d[domain] = domain_d.get(domain, 0) + 1

print domain_d

