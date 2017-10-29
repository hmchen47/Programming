
# Exercise 7.1
#
# Write a program to read through a file and print the contents of the
# file (line by line) all in upper case. Executing the program will
# look as follows:
#
#  python shout.py
#  Enter a file name: mbox-short.txt
#  FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#  RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#  RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#   BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#   SAT, 05 JAN 2008 09:14:16 -0500
#
#  You can download the file from www.py4inf.com/code/mbox-short.txt
#

fname = raw_input("Enter a file name:")

try:
    fh = open(fname)
except IOError as e:
    print "Cannot open file:", fname
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()

for line in fh:
    print line.upper()

