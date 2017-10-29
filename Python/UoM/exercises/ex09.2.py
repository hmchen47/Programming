#!/use/sbin/python
# -*- coding: utf-8 -*-
#
# Exercise 9.2 
# Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines which start with 
# “From”, then look for the third word and then keep a running count of 
# each of the days of the week. At the end of the program print out the 
# contents of your dictionary (order does not matter).
#
# Sample Line:
#   From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
#   python dow.py
#    Enter a file name: mbox-short.txt
#   {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = raw_input("Enter a file name: ")
try:
    fhandle = open(fname)
except IOError as e:
    print "IOError ({0}): {1}".formate(e.errno, e.strerror)
    exit()

day_dict = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        day_inline = words[2]
        day_dict[day_inline] = day_dict.get(day_inline, 0) + 1

print day_dict
print""

# how to sort day in dictionary
day_d = sorted(day_dict.keys())
for key in day_d:
    print(key, day_dict[key])


# Sort a Python dictionary by value
# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
# 
# sorted by the second element in each tuple
#   sorted_x = sorted(x.items(), key=operator.itemgetter(1))
#
# sort on keys instead of values
#   sorted_x = sorted(x.items(), key=operator.itemgetter(0))
#

# OrderedDict Examples and Recipes
# https://docs.python.org/2/library/collections.html#collections.OrderedDict
#
# regular unsorted dictionary
#   d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
#
# dictionary sorted by key
#   OrderedDict(sorted(d.items(), key=lambda t: t[0]))
#
# dictionary sorted by value
#   OrderedDict(sorted(d.items(), key=lambda t: t[1]))
#
# dictionary sorted by length of the key string
#   OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

# Sorting Mini-HOW TO
# https://wiki.python.org/moin/HowTo/Sorting
#
# sorted(student_tuples, key=lambda student: student[2])   # sort by age

# Sorted
# http://www.dotnetperls.com/sort-python
#