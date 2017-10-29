#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def addVectors(v1, v2):
    vec = []
    for idx in range(max(len(v1), len(v2))):
        val1, vla2 = 0, 0
        if idx < len(v1):
            val1 = v1[idx]
        else:
            val1 = 0

        if idx < len(v2):
            val2 = v2[idx]
        else:
            val2 = 0

        vec.append(val1 + val2)

    return vec

print addVectors([4, 5], [1, 2, 3])
print addVectors([1, 2, 3], [4, 5, 6])
print addVectors([5, 6, 7], [1, 2])