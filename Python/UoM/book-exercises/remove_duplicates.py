'''
remove_duplicates

Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1,1,2,2]) should return [1,2].

1. Don't remove every occurrence, since you need to keep a single occurrence of a number.
2. The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
3. Do not modify the list you take as input! Instead, return a new list.
'''

def remove_duplicates(x):
    tmpx = []
    for item in x:
        if (item in tmpx):
            continue
        else: 
            tmpx.append(item)
    return tmpx

print (remove_duplicates([1, 2, 3, 4, 3, 2, 1, 5, 4]))