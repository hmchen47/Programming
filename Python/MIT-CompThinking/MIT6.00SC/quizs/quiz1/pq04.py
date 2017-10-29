#!/usr/bin/python
# _*_ coding: utf-8 _*_

# practice quize 2010 - Q4


def addVectors(v1, v2):
    """ assumes v1 and v2 are lists of ints. Returns a list containing
    the pointwise sum of the elements in v1 and v2. E.g.,
    addVectors([4,5], [1,2,3]) returns [5,7,3],and
    addVectors([], []) returns []. Does not modify inputs."""

    new_Vec = []

    for cnt in range(max(len(v1), len(v2))):
        val_1, val_2 = 0, 0
        if cnt < len(v1):
            val_1 = v1[cnt]
        else:
            val_1 = 0

        if cnt < len(v2):
            val_2 = v2[cnt]
        else: 
            val_2 = 0

        new_Vec.append(val_1 + val_2)

    return new_Vec


if __name__ == '__main__':
    v1 = [4, 5]
    v2 = [1, 2, 3]
    print addVectors(v1, v2)

    v1=[]
    v2=[]
    print addVectors(v1, v2)
