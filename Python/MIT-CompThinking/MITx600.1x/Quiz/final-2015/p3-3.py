#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        print iteration, lst, out
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
    return out

sort3([4, 3 ,1, 6, 2, 8])