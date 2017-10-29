
#!/use/sbin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.4 
# Add code to the above program to figure out who has the most messages
# in the file.
# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Section 5.7.2) to 
# find who has the most messages and print how many messages the person 
# has.
#
# Enter a file name: mbox-short.txt
#   cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt
#   zqian@umich.edu 195

fname = raw_input("Enter a file name: ")
try:
    fhandle = open(fname)
except IOError as e:
    print "IO error ({0}): {1}".format(e.errno, e.strerror)
    exit()

mail_d = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        mail_d[words[1]] = mail_d.get(words[1], 0) + 1

bigcnt = None
bigmail = None
for mail,cnt in mail_d.items():
    if ((bigcnt == None) or (cnt > bigcnt)):
        bigcnt = cnt
        bigmail = mail

print bigmail, bigcnt
