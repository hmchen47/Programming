'''
purify

Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.

For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
'''


d = [4, 5, 5, 4]

def purify(x):
    tmpx = []
    for item in x:
        tmpx.append(item)
        
    for item in x:
        print item
        if (item%2 != 0):
            tmpx.remove(item)
            print tmpx
    return tmpx

print (purify(d))