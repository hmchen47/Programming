
# 10.2 Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull 
# the hour out from the 'From ' line by finding the time and then splitting 
# the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below. Note that the autograder does not have 
# support for the sorted() function.
#

fname = raw_input("Enter file: ")

if len(fname) < 1: fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except IOError as e:
    print "IO Error ({0}): {1}".format(e.errno, e.strerror)
    exit()

hrdict = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()

# find hour with find function
#        colpos = words[5].find(':')
#        hrstr = (words[5])[0:colpos]
#        hrdict[hrstr] = hrdict.get(hrstr, 0) + 1

# find hour with column character in split function 
        timestr = words[5].split(':')
        hrdict[timestr[0]] = hrdict.get(timestr[0], 0) + 1

hrtup = hrdict.items()
hrtup.sort()

for (key, val) in hrtup:
    print key, val