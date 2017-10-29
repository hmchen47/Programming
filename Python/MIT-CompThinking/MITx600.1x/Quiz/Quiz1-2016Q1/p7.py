#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    return (interDict(d1, d2), diffDict(d1, d2))


def interDict(d1, d2):
    '''
    return a disctionary with commone keys in d1 and d2
    and their values based on a given function f

    arguments:
        d1: disctionary, first set of input
        d2: disctionary, second set of input
    returns: 
        dictionary with common keys in d1 and d2
        and values are based on provided function f
    '''
    newDict = {}
    for key in d1.keys():
        if key in d2.keys():
            # print d1[key], d2[key]
            newDict[key] = f(d1[key], d2[key])

    return newDict

def diffDict(d1, d2):
    '''
    return a disctionary with difference keys in d1 and d2
    and their values based on a given function f
    the len of d1 is always greater or equal to d2

    arguments:
        d1: disctionary, first set of input
        d2: disctionary, second set of input
    returns: 
        dictionary with difference keys in d1 and d2
        and values are based on provided function f
    '''
    newDict = {}
    for key in d1.keys():
        if key not in d2.keys():
            # if type(f(d1[key], 0)) is not bool:
            #     newDict[key] = f(d1[key], 0)
            # else: 
            newDict[key] = d1[key]

    for key in d2.keys():
        if key not in d1.keys():
            # if type(f(d2[key], 0)) is not bool:
            #     # print(abs(0 - d2[key]))
            #     newDict[key] = f(d2[key], 0)
            # else:
            newDict[key] = d2[key]

    return newDict



# def f(a, b):
    # return a + b
    # return a - b
    # return abs(a - b)
    # return a * b
    # return a > b
    # return a < b
    # return a == b
    # return a >= b

# print(dict_interdiff({1:30, 2:20, 3:30, 5:80}, {1:40, 2:50, 3:60, 4:70, 6:90}))
# f(a, b) = a + b -> ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}) 
# f(a, b) = a > b -> ({1: False, 2: False, 3: False}, {})
# f(a, b) = a - b -> ({1: -10, 2: -30, 3: -30}, {4: -70, 5: 80, 6: -90})
# print(dict_interdiff({1:30, 2:20, 3:30}, {1:40, 2:50, 3:60}))
# f(a, b) = a > b -> ({1: False, 2: False, 3: False}, {})
# f(a, b) = a - b -> ({1: -10, 2: -30, 3: -30}, {})
'''
missing test cases:
1. empty ddisctonary
2. non-overlapping element
3. 
'''

def f(a, b):
    return a > b
print(dict_interdiff({}, {}))
# ({}, {})

def f(a, b):
    return a >= b
print(dict_interdiff({1: 1}, {1: 1}))
# ({1: True}, {})

def f(a, b):
    return a + b
print(dict_interdiff({1: 2}, {2: 1}))
# ({}, {1: 2, 2: 1})

def f(a, b):
    return a + b
print(dict_interdiff({0: 0, 2: 5, 5: 2}, {0: 0, 2: 5}))
# ({0: 0, 2: 10}, {5: 2})

def f(a, b):
    return a + b
print(dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3}))
# ({1: 2, 2: 4, 3: 6}, {})

def f(a, b):
    return a - b
print(dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3}))
# ({1: 0, 2: 0, 3: 0}, {})

def f(a, b):
    return a != b
print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4, 5: 4}, {1: 1, 2: 2, 3: 3, 4: 5}))
# ({1: False, 2: False, 3: False, 4: True}, {5: 4})

def f(a, b):
    return a < b
print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}))
# ({1: False, 2: False, 3: False, 4: True}, {6: 2})

def f(a, b):
    return a < b
print(dict_interdiff({1: 0, 2: 1, 3: 2, 4: 3, 5: 0}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}))
# ({1: True, 2: True, 3: True, 4: True}, {5: 0, 6: 2})

def f(a, b):
    return min(a, b)
print(dict_interdiff({1: 1, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}))
# ({1: 0, 2: 0, 3: 0, 4: 0}, {0: 1, 5: 0, 6: 0, 7: 0})

def f(a, b):
    return a + b
print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4}))
# ({}, {1: 1, 2: 2, 3: 3, 4: 5, 5: 3, 6: 3, 7: 4, 8: 4, 9: 1, 10: 0})

def f(a, b):
    return a > b
print(dict_interdiff({9: 1, 5: 3, 6: 3, 7: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}))
# ({}, {1: 1, 2: 2, 3: 3, 4: 5, 5: 3, 6: 3, 7: 4, 8: 4, 9: 1, 10: 0}

def f(a, b):
    return a + b
print(dict_interdiff({9: 1, 4: 4, 5: 3, 6: 3}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}))
# ({4: 9}, {1: 1, 2: 2, 3: 3, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0})

def f(a, b):
    return a + b
print(dict_interdiff({4: 4, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0}, {1: 1, 2: 2, 3: 3, 4: 5}))
# ({4: 9}, {1: 1, 2: 2, 3: 3, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0})


# def f(a, b):
#     return min(a, b)
# print(dict_interdiff({1: 1, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}))
# ({1: 0, 2: 0, 3: 0, 4: 0}, {0: 1, 5: 0, 6: 0, 7: 0})

# def f(a, b):
#     return a - b
# print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4}))
# # ({}, {1: 1, 2: 2, 3: 3, 4: 5, 5: 3, 6: 3, 7: 4, 8: 4, 9: 1, 10: 0})
