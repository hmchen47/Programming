#!/use/sbin/python
# -*- coding: utf-8 -*-

# Exercise 9.3 
# Write a program to read through a mail log, and build a 
# histogram using a dictionary to count how many messages have come from 
# each email address and print the dictionary.
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except IOError as e:
    print "IO error ({0}): {1}".format(e.errno, e.strerror)
    exit()
   
mail_dict = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        mail_dict[words[1]] = mail_dict.get(words[1], 0) + 1

print mail_dict

