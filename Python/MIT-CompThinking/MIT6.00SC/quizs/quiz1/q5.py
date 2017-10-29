#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Quiz 1 2011 - Q5
#
# The following code does not meet its specification. Correct it.

def addVectors(v1, v2):
    """assumes v1 and v2 are lists of ints.
    Returns a list containing the pointwise sum of
    the elements in v1 and v2. For example,
    addVectors([4,5], [1,2,3]) returns [5,7,3],and
    addVectors([], []) returns []. Does not modify inputs."""
    result = []             # creatre a new list
    if len(v1) > len(v2):
#        result = v1
        result += v1
        other = v2
    else:
#        result = v2
        result += v2
        other = v1

    for i in range(len(other)):
        result[i] += other[i]
    
    return result


if __name__ == '__main__':
    v1 = [4, 5]
    v2 = [1, 2, 3]
    print addVectors(v1, v2)
