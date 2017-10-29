#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import re

''' 
read through and parse a file with text and numbers
extract all the numbers in the file and compute the sum of the numbers

Sample file: 
    http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/regex_sum_42.txt 
    (There are 87 values with a sum=445822)
Actual data: 
    http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/regex_sum_186643.txt 
    (There are 74 values and the sum ends with 337)

Local file: regex_sum_42.txt & regex_sum_186643.txt
'''

def str2num(lst):
    '''
    Convert a string list with numbers to a integer list

    lst: a list with numbers in string

    returns: an interger list
    '''
    lstInt = []
    # print lst
    for idx in range(len(lst)):
        #print '####', lst[idx]
        if len(lst) != 0 and float(lst[idx]) != float('NaN'):
            lstInt.append(float(lst[idx]))
        else:
            print 'str2num: Check input list element', idx, lst[idx], \
                'with invalid number string'
    return lstInt

def extractNumStr(line, lst):
    '''
    extract the number string from the given line with RegExp

    line: a string with or without number string
    lst: a given list to store all number string

    returns: None
    '''
    lstNumStr = re.findall('[0-9]+', line)
    for numStr in lstNumStr:
        lst.append(numStr)

    return None

def readNconvert(fname):
    '''
    read a file with given filename, fname, and then convert the read lines
    with number string into 

    fname: file anme

    returns: a list, store the read number strings into numerica numbers
    '''
    # open the file
    try:
        fhandle = open(fname, 'r', 0)
    except IOError as e:
        print "Cannot open file:", fname
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        exit()

    # read file line by line and put into the strNum list
    strNum = []
    for line in fhandle:
        extractNumStr(line, strNum)

    # convert the strNum into numeric number list
    #print len(strNum)
    return str2num(strNum)


if __name__ == '__main__':
    sfile = 'regex_sum_42.txt'
    print 'Sample file', sfile, 'with sum =', int(sum(readNconvert(sfile)))

    afile = 'regex_sum_186643.txt'
    print 'Actual file', afile, 'with sum =', int(sum(readNconvert(afile)))
