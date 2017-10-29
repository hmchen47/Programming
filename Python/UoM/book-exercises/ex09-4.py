#!/use/sbin/python
# -*- coding: utf-8 -*-
#
# 9.4 Write a program to read through the mbox-short.txt and figure out who 
# has the sent the greatest number of mail messages. The program looks for 
# 'From ' lines and takes the second word of those lines as the person who 
# sent the mail. The program creates a Python dictionary that maps the 
# sender's mail address to a count of the number of times they appear in 
# the file. After the dictionary is produced, the program reads through the 
# dictionary using a maximum loop to find the most prolific committer.

fname = raw_input("Enter file:")

if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fhandle= open(fname)
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()

name_count = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        name = words[1]
        name_count[name] = name_count.get(name, 0) + 1

bigcnt = None
bigname = None

for name,cnt in name_count.items():
    if ((bigcnt is None) or (cnt > bigcnt)):
        bigname = name
        bigcnt = cnt

print bigname, bigcnt
