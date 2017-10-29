#!/usr/bin/env python2
# _*_ encodiung: utf-8 _*_

import copy

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    tmpDict = copy.deepcopy(aDict)
    dictlist = []
    #print tmpDict
    for key in aDict.keys():
        cnt = 0
        for tmpKey in tmpDict.keys():
            if tmpDict[tmpKey] == aDict[key]:
                cnt += 1

        if cnt > 1:
            for tmpkey in tmpDict.keys():
                if tmpDict[tmpkey] == aDict[key]:
                    tmpDict.pop(tmpkey, None)

    for key, value in tmpDict.iteritems():
        dictlist.append([key,value])
    sortedList = sorted(dictlist, key=lambda k: k[0])
    #print sortedList
    unique = []
    for idx in range(len(sortedList)):
        unique.append(sortedList[idx][0])

    return unique

#print uniqueValues({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 2, 'g':7})

#print uniqueValues({1: 1, 2: 2, 3: 3})
#   [1, 2, 3]
#print uniqueValues({1: 1, 2: 1, 3: 1})
#   []
#print uniqueValues({1: 1})
#   [1]
#print  uniqueValues({1: 1, 2: 1, 3: 3})
#   [3]
#print uniqueValues({2: 2, 3: 3, 4: 4})
#   [2, 3, 4]
#print uniqueValues({})
#print []
#print uniqueValues({2: 0, 3: 3, 6: 1})
#   [2, 3, 6]
#print uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
#   [1, 3, 8]
#print uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})
#   [0, 1, 2, 3, 5, 6, 7, 9, 10] 
#print uniqueValues({8: 3, 1: 3, 2: 2})
#   [2]
#print uniqueValues({2: 2, 5: 0, 7: 3})
#   [2, 5, 7] -> my [5, 2, 7]
print uniqueValues({5: 1, 7: 1})
#   []
print uniqueValues({0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0})
#   [3, 7, 9]
print uniqueValues({0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3})
#   [2, 3]
print uniqueValues({8: 1, 0: 4, 1: 1, 5: 2, 9: 4})
#   [5]