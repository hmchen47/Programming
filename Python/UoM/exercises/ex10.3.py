#!/usr/bin/python
# _*_ config: utf-8 -*_

# Exercise 10.3 
# Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower 
# case and only count the letters a-z. Your program should not count 
# spaces, digits, punctuation or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter 
# frequency varies between languages. Compare your results with the tables 
# at wikipedia.org/wiki/Letter_frequencies.

fname = raw_input("Enter a file name: ")

try:
    fhandle = open(fname)
except IOError as e:
    print "IO Error {0}: {1}".format(e.errno, e.strerror)
    exit()

letter_dict = dict()
for line in fhandle:
    line.lower()
    for letter in line:
        if ((letter >= 'a' ) and (letter[0] <= 'z')):
            letter_dict[letter] = letter_dict.get(letter, 0) + 1

letter_lst = list()
tsum = 0
for (key, val) in letter_dict.items():
    letter_lst.append((val, key))
    tsum +=  val

print "Sum = ", tsum

letter_freq_tup = tuple()
for (key, val) in letter_dict.items():
    letter_freq_tup = letter_freq_tup + ((key, val, float(val)/float(tsum)),)

srt_letter_tup = sorted(letter_freq_tup)

for cnt in range(len(srt_letter_tup)):
    print "  ", srt_letter_tup[cnt][0], repr(srt_letter_tup[cnt][1]).rjust(10), \
        "\t", repr(srt_letter_tup[cnt][2]).ljust(12)


